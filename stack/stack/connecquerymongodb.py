import pymongo
# This will help me in treacting with Mongodb with the help of python like creating Databases/collections etc

client=pymongo.MongoClient('mongodb://127.0.0.1:27017/') # this is mongo client that can be use to treact with MondoDB 3 elements are used : 1) protocol2)local host ip address3) port number
# Database Name
mydb=client['Employees_Data']
# Collection or Table name
information=mydb.employeeinformation
records=[{'firstname':'ankit',
         'lastname':'ghai',
         'department':'analytics'

},{'firstname':'ankit1',
         'lastname':'ghai1',
         'department':'analytics1'

},{'firstname':'ankit22',
         'lastname':'ghai22',
         'department':'analytics2',
         'qualification':'master',
         'age':32

}]

# Insert multiple records in the database
information.insert_many(records)

# Simple way of quering the MongoDb data source with by default return 1st record in the collection
for i in mydb.employeeinformation.find_one({}):
   print(i)


# Simple way of quering the MongoDb data source with by default return all record in the collection, just like select * from table_name in sql query
for i in mydb.employeeinformation.find():
    print(i)

# Simple way of querying the collection to fetch the records based on equality condition,Use {} to write the query inside it
# Just like select * from table_name where first_name='ankit
for i in mydb.employeeinformation.find({'firstname':'ankit'}):
    print(i)
# All the operator we are applying over the JASON documentwe will be getting result in the form of CURSOR on which we can apply for loop to get the 
# data as cursor is am like a iterable that can produce iterators
# JASON document using the Query operator ($in,$lt,$gt)
for i in mydb.employeeinformation.find({'qualification':{'$in':['phd','master']}}):
    print(i)

'''
Below we are using and & query operator to retrieve the data from the MongoDb database like using 'and' & '$lt'
'''
for i in mydb.employeeinformation.find({'qualification':'master','age':{'$lt':35}}):
    print(i)

# Query operator 'OR' & 'and'

for i in mydb.employeeinformation.find({'$or':[{'firstname':'ankit'},{'age':32}]}):
    print(i)


for i in mydb.eployeeinformation.find({'$and':[{'firsname':'ankit'},{'age':32}]}):
    print(i)

# Creating new collection inventory
inventory=mydb.inventory

# Adding records in the inventory collection.Here we have nested JASON documents

inventory.insert_many([
   { 'item': "journal", 'qty': 25, 'size': { 'h': 14, 'w': 21,'uom': "cm" }, 'status': "A" },
   { 'item': "notebook", 'qty': 50,'size': { 'h': 8.5, 'w': 11,'uom': "in" },'status': "A" },
   { 'item': "paper", 'qty': 100, 'size': { 'h': 8.5, 'w': 11,'uom': "in" },'status': "D" },
   { 'item': "planner", 'qty': 75, 'size': { 'h': 22.85,'w': 30,'uom': "cm" },'status': "D" },
   { 'item': "postcard", 'qty': 45, 'size': { 'h': 10, 'w': 15.25,'uom': "cm" },'status': "A" }
])

# Query nested JASON documents
for j in inventory.find({'size':{'h': 14, 'w': 21,'uom': "cm"}}):
    print(j)