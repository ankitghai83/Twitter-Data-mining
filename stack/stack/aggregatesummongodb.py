'''
Mongodb Aggregate And Group these are like an operator in the MongoDB
avg
sum
project

'''
#import pymongo library
import pymongo

client=pymongo.MongoClient('mongodb://127.0.0.1:27017/')

#'access database Student'
mydb=client['Student']

# Access the collection in the above database
student=mydb['studentscores']
data = [ 
    {"user":"Krish", "subject":"Database", "score":80}, 
    {"user":"Amit",  "subject":"JavaScript", "score":90}, 
    {"user":"Amit",  "title":"Database", "score":85}, 
    {"user":"Krish",  "title":"JavaScript", "score":75}, 
    {"user":"Amit",  "title":"Data Science", "score":60},
    {"user":"Krish",  "title":"Data Science", "score":95}] 

# Insert records in the collection studentscores, Uncomment below instruction if you want to insert the records
#student.insert_many(data)


# Find # of subjects that students have under their name
agg_result=student.aggregate([{'$group':{'_id':'$user',"Total_Subject":{'$sum':1}}}]) # '_id' can't be customised as that unique in Mongodb to identify the records
for i in agg_result:
    print(i)

# Find Total score based on users
agg_score=student.aggregate([{'$group':{'_id':'$user','Total_Marks':{'$sum':'$score'}}}])
for j in agg_score:
    print(j)

# Calculate the average score by user

avg_score=student.aggregate([{'$group':{'_id':'$user','student_avg_score':{'$avg':'$score'}}}])
for x in avg_score:
    print(x)

# Working with Datetime
import  datetime as datetime
# Prep data :
data=[{ "_id" : 1, "item" : "abc", "price" : 10, "quantity" : 2, "date" : datetime.datetime.utcnow()},
{ "_id" : 2, "item" : "jkl", "price" : 20, "quantity" : 1, "date" : datetime.datetime.utcnow() },
{ "_id" : 3, "item" : "xyz", "price" : 5, "quantity" : 5, "date" : datetime.datetime.utcnow() },
{ "_id" : 4, "item" : "abc", "price" : 10, "quantity" : 10, "date" : datetime.datetime.utcnow() },
{ "_id" : 5, "item" : "xyz", "price" : 5, "quantity" : 10, "date" :datetime.datetime.utcnow() }]

# Creating collection,uncomment line #57 to insert more data
stores=mydb['storedata']
#stores.insert_many(data)

# Calculating overall average quantity & overall average cost of the item

agg_result=stores.aggregate([{'$group':{'_id':'$item','avg_cost':{'$avg':{'$multiply':['$price','$quantity']}},'avg_qty':{'$avg':'$quantity'}}}])

for y in agg_result:
    print(y)


# Using $project : It is just like select column_name from table_name in sql server

#### $Project

data=[{
  "_id" : 1,
  "title": "abc123",
  "isbn": "0001122223334",
  "author": { "last": "zzz", "first": "aaa" },
  "copies": 5
},
{
  "_id" : 2,
  "title": "Baked Goods",
  "isbn": "9999999999999",
  "author": { "last": "xyz", "first": "abc", "middle": "" },
  "copies": 2
}
]

dummy_data=mydb['data']
# Inserting data in the collection
#dummy_data.insert_many(data)

for k in dummy_data.aggregate([{'$project':{'title':1,'isbn':1}}]):
    print(k)