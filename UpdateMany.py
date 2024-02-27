from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pprint

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

    # Define the filter to select documents to update
    # For example, to select documents where marks are less than 50
    filter_criteria = {"marks": {"$lt": 50}}

    # Define the update operation
    # For example, to add 10 bonus marks to all students who have marks less than 50
    update_operation = {"$inc": {"bonus_marks": 10}}

    # Update all documents that match the filter criteria
    result = EAMCETMarks.update_many(filter_criteria, update_operation)

    # Print the number of documents matched and updated
    print(f"Documents matched: {result.matched_count}")
    print(f"Documents updated: {result.modified_count}")

    # Optionally, print one of the updated documents to verify the update
    updated_document = EAMCETMarks.find_one(filter_criteria)
    pprint.pprint(updated_document)

except Exception as e:
    print(e)
finally:
    client.close()
