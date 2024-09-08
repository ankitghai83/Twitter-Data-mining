import pymongo

# Connecting to cloud based MongoDb database via MongoDb Atlas
client=pymongo.MongoClient('mongodb+srv://ankitghai:EQiUd2Zj8lr2CWpF@cluster0.4kqjy.mongodb.net/')

# Acccess Database student
mydatabase =client['Students']

# Creating the collection
collection=mydatabase['studentscores']

#Creating the datasource
data = [ 
    {"user":"Krish", "subject":"Database", "score":80}, 
    {"user":"Amit",  "subject":"JavaScript", "score":90}, 
    {"user":"Amit",  "title":"Database", "score":85}, 
    {"user":"Krish",  "title":"JavaScript", "score":75}, 
    {"user":"Amit",  "title":"Data Science", "score":60},
    {"user":"Krish",  "title":"Data Science", "score":95}] 

# inserting the data inthe collection

#collection.insert_many(data)

# Calculate the score obtained by each user
score_obtained=collection.aggregate([{'$group':{'_id':'$user','Total_score':{'$sum':'$score'}}}])
for i in score_obtained:
    print(i)