import tkinter as tk
from tkinter import messagebox, simpledialog
from pymongo import MongoClient
from bson.objectid import ObjectId

# MongoDB connection parameters
MONGODB_URI = "mongodb+srv://romocromo90:SsphxApuBAlkdhFc@cluster0.atmpzxm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DATABASE_NAME = "portfolio_tracker"

# Connect to MongoDB
client = MongoClient(MONGODB_URI)
db = client[DATABASE_NAME]

# Tkinter application
class PortfolioTrackerApp:
    def __init__(self, master):
        self.master = master
        master.title("Portfolio Management")

        self.label = tk.Label(master, text="Welcome to Portfolio Management")
        self.label.pack()

        self.add_portfolio_frame = tk.Frame(master)
        self.add_portfolio_frame.pack()

        # Entry fields for adding portfolio
        tk.Label(self.add_portfolio_frame, text="Portfolio Name:").grid(row=0, column=0, sticky='e')
        self.portfolio_name_entry = tk.Entry(self.add_portfolio_frame)
        self.portfolio_name_entry.grid(row=0, column=1)

        tk.Label(self.add_portfolio_frame, text="Stock Symbol:").grid(row=1, column=0, sticky='e')
        self.symbol_entry = tk.Entry(self.add_portfolio_frame)
        self.symbol_entry.grid(row=1, column=1)

        tk.Label(self.add_portfolio_frame, text="Quantity:").grid(row=2, column=0, sticky='e')
        self.quantity_entry = tk.Entry(self.add_portfolio_frame)
        self.quantity_entry.grid(row=2, column=1)

        tk.Label(self.add_portfolio_frame, text="Transaction Type:").grid(row=3, column=0, sticky='e')
        self.transaction_type_var = tk.StringVar(master)
        self.transaction_type_var.set("Buy")
        self.transaction_type_dropdown = tk.OptionMenu(self.add_portfolio_frame, self.transaction_type_var, "Buy", "Sell")
        self.transaction_type_dropdown.grid(row=3, column=1)

        tk.Label(self.add_portfolio_frame, text="Date of Transaction (YYYY-MM-DD):").grid(row=4, column=0, sticky='e')
        self.date_entry = tk.Entry(self.add_portfolio_frame)
        self.date_entry.grid(row=4, column=1)

        tk.Label(self.add_portfolio_frame, text="Price per Share:").grid(row=5, column=0, sticky='e')
        self.price_entry = tk.Entry(self.add_portfolio_frame)
        self.price_entry.grid(row=5, column=1)

        self.add_button = tk.Button(self.add_portfolio_frame, text="Add Portfolio", command=self.add_portfolio)
        self.add_button.grid(row=6, columnspan=2)

        # Update and delete buttons
        self.update_button = tk.Button(master, text="Update Portfolio", command=self.update_portfolio)
        self.update_button.pack()

        self.delete_button = tk.Button(master, text="Delete Portfolio", command=self.delete_portfolio)
        self.delete_button.pack()

        self.get_portfolio_button = tk.Button(master, text="Get Portfolio", command=self.get_portfolio)
        self.get_portfolio_button.pack()

        self.portfolios_text = tk.Text(master, height=10, width=50)
        self.portfolios_text.pack()

    def add_portfolio(self):
        portfolio_name = self.portfolio_name_entry.get()
        symbol = self.symbol_entry.get()
        quantity = int(self.quantity_entry.get())
        transaction_type = self.transaction_type_var.get()
        date = self.date_entry.get()
        price = float(self.price_entry.get())

        transaction_data = {
            "symbol": symbol,
            "quantity": quantity,
            "transaction_type": transaction_type,
            "date": date,
            "price": price
        }

        portfolio_data = {
            "name": portfolio_name,
            "transactions": [transaction_data]
        }

        db.portfolios.insert_one(portfolio_data)
        messagebox.showinfo("Success", "Portfolio added successfully!")

    def get_portfolio(self):
        portfolio_name = simpledialog.askstring("Input", "Enter portfolio name:")
        if portfolio_name:
            portfolio = db.portfolios.find_one({"name": portfolio_name})
            if portfolio:
                self.portfolios_text.delete(1.0, tk.END)
                self.portfolios_text.insert(tk.END, f"Portfolio: {portfolio['name']}\n")
                for transaction in portfolio['transactions']:
                    self.portfolios_text.insert(tk.END, f"Symbol: {transaction['symbol']}, Quantity: {transaction['quantity']}, "
                                                         f"Transaction Type: {transaction['transaction_type']}, "
                                                         f"Date: {transaction['date']}, Price: {transaction['price']}\n")
            else:
                messagebox.showerror("Error", f"Portfolio '{portfolio_name}' not found!")
        else:
            messagebox.showwarning("Warning", "Please enter a portfolio name!")

    def update_portfolio(self):
        portfolio_name = simpledialog.askstring("Input", "Enter portfolio name:")
        if portfolio_name:
            portfolio = db.portfolios.find_one({"name": portfolio_name})
            if portfolio:
                new_symbol = self.symbol_entry.get()
                new_quantity = int(self.quantity_entry.get())
                new_transaction_type = self.transaction_type_var.get()
                new_date = self.date_entry.get()
                new_price = float(self.price_entry.get())

                new_transaction = {
                    "symbol": new_symbol,
                    "quantity": new_quantity,
                    "transaction_type": new_transaction_type,
                    "date": new_date,
                    "price": new_price
                }

                db.portfolios.update_one({"name": portfolio_name}, {"$push": {"transactions": new_transaction}})
                messagebox.showinfo("Success", "Portfolio updated successfully!")
            else:
                messagebox.showerror("Error", f"Portfolio '{portfolio_name}' not found!")
        else:
            messagebox.showwarning("Warning", "Please enter a portfolio name!")

    def delete_portfolio(self):
        portfolio_name = simpledialog.askstring("Input", "Enter portfolio name:")
        if portfolio_name:
            result = db.portfolios.delete_one({"name": portfolio_name})
            if result.deleted_count > 0:
                messagebox.showinfo("Success", f"Portfolio '{portfolio_name}' deleted successfully!")
            else:
                messagebox.showerror("Error", f"Portfolio '{portfolio_name}' not found!")
        else:
            messagebox.showwarning("Warning", "Please enter a portfolio name!")

def main():
    root = tk.Tk()
    app = PortfolioTrackerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
