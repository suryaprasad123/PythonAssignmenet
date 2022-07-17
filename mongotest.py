import pymongo

client = pymongo.MongoClient("mongodb+srv://surya:surya@cluster0.zehne.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


d = {
    "name": "surya prasad",
    "email": "surya@ineuron.ai",
    "surname": "pradhan"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
