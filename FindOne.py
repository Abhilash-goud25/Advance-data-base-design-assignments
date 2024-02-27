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

    # Get reference to the collection that stores EAMCET marks, for example, 'EAMCETMarks'
    EAMCETMarks = db.EAMCETMarks

    # Define the document to find by its ObjectId
    document_to_find = {
        "_id": ObjectId("65de13b78c3e6aae2aa81ac6")  # Replace 'YourObjectIdHere' with the actual ObjectId string
    }

    # Find one document in the 'EAMCETMarks' collection
    result = EAMCETMarks.find_one(document_to_find)

    pprint.pprint(result)

except Exception as e:
    print(e)
finally:
    client.close()
