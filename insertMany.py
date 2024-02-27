from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime

uri = "mongodb+srv://abhilashgoudab:Abhi2506@cluster0.vod4mfv.mongodb.net/"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to a database, for example, 'StudentRecords'
    db = client.StudentRecords

    # Get reference to a collection, for example, 'EAMCETMarks'
    EAMCETMarks = db.EAMCETMarks

    # Inserting many students' EAMCET exam marks
    new_eamcet_marks = [
        {
            "student_name": "Student A",
            "Physics": 40,
            "Chemistry": 35,
            "Mathematics": 45,
            "TotalMarks": 120
        },
        {
            "student_name": "Student B",
            "Physics": 38,
            "Chemistry": 40,
            "Mathematics": 42,
            "TotalMarks": 120
        },
        {
            "student_name": "Student C",
            "Physics": 42,
            "Chemistry": 38,
            "Mathematics": 40,
            "TotalMarks": 120
        }
    ]

    # Write an expression that inserts the 'new_eamcet_marks' documents into the 'EAMCETMarks' collection.
    result = EAMCETMarks.insert_many(new_eamcet_marks)

    document_ids = result.inserted_ids
    print("# of documents inserted: " + str(len(document_ids)))
    print(f"_ids of inserted documents: {document_ids}")

except Exception as e:
    print(e)
finally:
    client.close()
