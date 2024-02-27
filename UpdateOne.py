from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId

uri = "mongodb+srv://abhilashgoudab:Abhi2506@cluster0.vod4mfv.mongodb.net/"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to the desired database, for example, 'StudentRecords'
    db = client.StudentRecords

    # Get reference to the 'EAMCETMarks' collection
    EAMCETMarks = db.EAMCETMarks

    # Define the filter to find the document you want to update
    # For example, to update a document by its '_id':
    filter = {"_id": ObjectId("65de138954a8f66ae03eaaaa")}

    # Define the update operations
    # For example, to increment a student's marks by 5:
    update = {"$inc": {"marks": 5}}

    # Update one document in the 'EAMCETMarks' collection
    result = EAMCETMarks.update_one(filter, update)

    # Print the status of the update operation
    if result.matched_count > 0:
        print(f"Successfully matched and updated document: {result.modified_count} document(s) updated.")
    else:
        print("No documents matched the query. No documents were updated.")

except Exception as e:
    print(e)
finally:
    client.close()
