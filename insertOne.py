from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime
from pprint import pprint

uri = "mongodb+srv://abhilashgoudab:Abhi2506@cluster0.vod4mfv.mongodb.net/"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to your database, for example, 'StudentRecords'
    db = client.StudentRecords

    # Get reference to your collection, for example, 'EAMCET_Marks'
    EAMCET_Marks = db.EAMCET_Marks

    # Define a new document for EAMCET exam marks
    new_eamcet_marks = {
        "student_name": "Abhilash",
        "hall_ticket_number": "1234567890"
        "maths_marks": 80,  # Assuming out of 100
        "physics_marks": 70,  # Assuming out of 100
        "chemistry_marks": 75,  # Assuming out of 100
        "total_marks": 225,
        "exam_date": datetime.datetime.now().strftime("%Y-%m-%d")  # Current date in YYYY-MM-DD format
    }

    # Insert the 'new_eamcet_marks' document into the 'EAMCET_Marks' collection
    result = EAMCET_Marks.insert_one(new_eamcet_marks)

    document_id = result.inserted_id
    pprint(f"_id of inserted document: {document_id}")

except Exception as e:
    print(e)
finally:
    # Close the connection to MongoDB
    client.close()
