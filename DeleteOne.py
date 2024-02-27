from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
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

    # Specify the document to delete by its ObjectId
    document_to_delete = {"_id": ObjectId("65de13b78c3e6aae2aa81ac8")}  # Replace 'your_object_id_here' with the actual ObjectId

    # Search for the document before deletion
    print("Searching for target document before deletion: ")
    pprint.pprint(EAMCETMarks.find_one(document_to_delete))

    # Delete the specified document
    result = EAMCETMarks.delete_one(document_to_delete)

    # Search for the document after deletion to confirm it's been removed
    print("Searching for target document after deletion: ")
    pprint.pprint(EAMCETMarks.find_one(document_to_delete))

    # Output the result of the deletion
    print(f"Documents deleted: {result.deleted_count}")

except Exception as e:
    print(e)
finally:
    client.close()
