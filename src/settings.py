import os
import pymongo

mongodb_settings = "mongodb+srv://cleanair-user:{}@cluster0.cijb1.mongodb.net/clean_air?retryWrites=true&w=majority".format(os.environ['MONGODB_PASS'])
client = pymongo.MongoClient(mongodb_settings)
db = client.clean_air
