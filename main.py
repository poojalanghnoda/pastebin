from pymongo import MongoClient
from bson.objectid import ObjectId

def check_true_authenticate(username,password):
    res = coll.find({'username':username,'password':password})
    print(res.count())
    
    if(res.count()==0):
        print(False)
        return False
    else:
        print(True)
        return True
            
    
con = MongoClient('localhost',27017)
db = con.pasteDB

username = input()
password = input()
coll = db.collection


res  = check_true_authenticate(username, password)
if(res==True):
    data  = input()
    coll.update(
        {'username':username},
        {'$set':{'data':data}})
    print('Updated')
    
else:
    coll.insert({'username':username,'password':password})


