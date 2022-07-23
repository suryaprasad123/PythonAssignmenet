import pymongo

data =  [
        {
            "item": "canvas",
            "qty": 100,
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mat",
            "qty": 85,
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mousepad",
            "qty": 25,
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
            "status": "P",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "P",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketchbook",
            "qty": 80,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketch pad",
            "qty": 95,
            "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
            "status": "A",
        },
    ]

# data =  [{
#             "item": "canvas",
#             "qty": 100,
#             "size": {"h": 8.5, "w": 11, "uom": "in"},
#             "status": "D",
#         },
#         {
#             "item": "canvas",
#             "qty": 100,
#             "size": {"h": 9.5, "w": 11, "uom": "in"},
#             "status": "D",
#         }
# ]

client = pymongo.MongoClient("mongodb+srv://surya1:surya123@cluster0.wiuod.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database = client['inventory']
colloction = database['inventory-table']
colloction.insert_many(data)

#record=colloction.find({"status":"A"})
# record=colloction.find({"status": {"$in":["A","P"]}})
# record=colloction.find({"status": {"$gt":"C"}})
#record=colloction.find({"qty": {"$gt":75}})
#record=colloction.find({"qty": {"$gte":75}})
#record=colloction.find({"item": "sketch pad","qty":95})
#record=colloction.find({"item": "sketch pad","qty":{"$gte":75}})
#record=colloction.find({"$or":[{"item":"sketch pad"},{"qty":{"$gte":75}}]})
record=colloction.find({"$or":[{"item":"sketch pad"},{"qty":{"$gte":75}}]})
for i in record:
    print(i)
