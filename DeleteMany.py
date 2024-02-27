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

    # Print count of documents before deletion for reference
    initial_count = EAMCETMarks.count_documents({})
    print(f"Initial document count: {initial_count}")

    # Use an empty query object to match all documents in the collection
    query = {}

    # Delete all documents in the collection
    result = EAMCETMarks.delete_many(query)

    # Print the number of documents deleted
    print(f"Documents deleted: {result.deleted_count}")

    # Optionally, verify the collection is empty by counting documents post-deletion
    final_count = EAMCETMarks.count_documents({})
    print(f"Final document count (should be 0): {final_count}")

except Exception as e:
    print(e)
finally:
    client.close()
