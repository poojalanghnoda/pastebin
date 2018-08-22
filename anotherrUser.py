from pymongo import MongoClient
from bson.objectid import ObjectId
con = MongoClient('localhost',27017)
db = con.pasteDB

username = input()
password = input()
coll = db.collection

def dataToOterUser(username,password):
    out = coll.find({'username':username,'password':password})
    for i in out:
        print(i['data'])
        
dataToOterUser(username,password)
con.close()
