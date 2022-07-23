import pymongo

client = pymongo.MongoClient("mongodb+srv://surya1:surya123@cluster0.wiuod.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database = client['inventory']
colloction = database['inventory-table']

colloction.update_one({"item":"canvas"},{"$set":{"item":"surya"}})
d=colloction.find({"item":"surya"})
for i in d:
    print(i)