import pymongo
from pymongo import MongoClient
import certifi

ca = certifi.where()

db_connect = MongoClient("mongodb+srv://admin:admin@checklst.xzwfyan.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca).checklst
# db_connect = MongoClient('localhost', 27017).checklst
