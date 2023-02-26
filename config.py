import pymongo
import certifi

con_str = "mongodb+srv://Gary_FullStack:peach123@cluster0.o4hmh4x.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())
db = client.get_database("onlinestore34")
