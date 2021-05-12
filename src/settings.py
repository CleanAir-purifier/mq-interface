import os
import pymongo

mongodb_settings = f"mongodb+srv://cleanair-user:{os.getenv('MONGODB_PASS')}"\
    + "@cluster0.cijb1.mongodb.net/clean_air?retryWrites=true&w=majority"

client = pymongo.MongoClient(mongodb_settings)
db = client.clean_air
