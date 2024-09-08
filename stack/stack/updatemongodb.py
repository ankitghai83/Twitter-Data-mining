#UPDATE JSON DOCUMENT using update_one() ;update_many() ; replace_one()
'''
pymongo.collection.Collection.update_one()
pymongo.collection.Collection.update_many()
pymongo.collection.Collection.replace_one()
'''

import pymongo
# Connecting to the mongoDB database
client=pymongo.MongoClient('mongodb://127.0.0.1:27017/')

mydb=client['Employees']
inventory_new=mydb.inventory_new
'''inventory_new.insert_many([
    {"item": "canvas",
     "qty": 100,
     "size": {"h": 28, "w": 35.5, "uom": "cm"},
     "status": "A"},
    {"item": "journal",
     "qty": 25,
     "size": {"h": 14, "w": 21, "uom": "cm"},
     "status": "A"},
    {"item": "mat",
     "qty": 85,
     "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
     "status": "A"},
    {"item": "mousepad",
     "qty": 25,
     "size": {"h": 19, "w": 22.85, "uom": "cm"},
     "status": "P"},
    {"item": "notebook",
     "qty": 50,
     "size": {"h": 8.5, "w": 11, "uom": "in"},
     "status": "P"},
    {"item": "paper",
     "qty": 100,
     "size": {"h": 8.5, "w": 11, "uom": "in"},
     "status": "D"},
    {"item": "planner",
     "qty": 75,
     "size": {"h": 22.85, "w": 30, "uom": "cm"},
     "status": "D"},
    {"item": "postcard",
     "qty": 45,
     "size": {"h": 10, "w": 15.25, "uom": "cm"},
     "status": "A"},
    {"item": "sketchbook",
     "qty": 80,
     "size": {"h": 14, "w": 21, "uom": "cm"},
     "status": "A"},
    {"item": "sketch pad",
     "qty": 95,
     "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
     "status": "A"}])


# Update_one operation
inventory_new.update_one({"item": "sketch pad"},
                     {'$set':{'size.uom':'m','status':'P'},
                      '$currentDate':{'lastModified':True}})'''


# Update_many operation

#inventory_new.update_many({'qty':{'$lt':50}},{'$set':{"size.uom":'in','status':'p'},'$currentDate':{'lastmodifiedDate':True}})

# replace_one : This will replace the selected items' complete record with what we want

inventory_new.replace_one({'item':'paper'},{'item':'paper','instock':[{'warehouse':'A','qty':60},{'warehouse':'B','qty':40}]})
