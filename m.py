import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017")
print("connected")
db=client["class"]
col=db["details"]
users=[{
    "name":"ram",
    "age":"25",
    'adm':10,
    
},{
    "name":"raj",
    "age":"23",
    'adm':11,
},{
    "name":"sid",
    "age":"24",
    'adm':12,
}]
#col.insert_many(users)
#print(col.find_one())
for d in col.find({"name":{"$regex":"^r"},'age':{"$gt":"24","$lt":"27"}}):
    print(d)