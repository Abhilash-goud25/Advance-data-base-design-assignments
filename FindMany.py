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

    # Get reference to the collection that stores EAMCET marks, for example, 'EAMCETMarks'
    EAMCETMarks = db.EAMCETMarks

    # Define your query criteria (if needed)
    # For example, to find all documents where the student scored more than 90 marks:
    query = {"marks": {"$gt": 90}}

    # Find multiple documents in the 'EAMCETMarks' collection
    # If you want to retrieve all documents, pass an empty dictionary: EAMCETMarks.find({})
    results = EAMCETMarks.find(query)

    # Print each document
    for document in results:
        pprint.pprint(document)

except Exception as e:
    print(e)
finally:
    client.close()
