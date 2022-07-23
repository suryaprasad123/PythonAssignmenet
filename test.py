import pymongo

client = pymongo.MongoClient("mongodb+srv://surya1:surya123@cluster0.wiuod.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client['myinfo']
colloction = database['surya-db']

# record=colloction.find()
# for i in record:
#     print(i)

# record1 = colloction.find({"companyName": "iNeuron"})
record1 = colloction.find({"courseOffered": {"$gt":"E"}})
for i in record1:
    print(i)
