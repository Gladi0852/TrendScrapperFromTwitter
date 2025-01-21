from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()
url = os.getenv("mongo_url")

client = MongoClient(url, server_api=ServerApi('1'))

db = client["ScrappingTwitter"]
collection = db["trending_topics"]

def saveData(data):
    try:
        result = collection.insert_one(data)
        return result.inserted_id
    except Exception as e:
        return f"Error - {e}"

from bson import ObjectId  # Import ObjectId for working with MongoDB IDs

def getData(id):
    try:
        object_id = ObjectId(id)
        document = collection.find_one({"_id": object_id})
        if document:
            document["_id"] = str(document["_id"])
            return document
        else:
            return {"error": "No document found with the given ID"}
    except Exception as e:
        return {"error": f"Failed to fetch data: {e}"}
