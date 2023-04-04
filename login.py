import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017")
print("connected")
db=client["class"]
col=db["details"]
x=input("enter your user name")
y=int(input("enter your password"))
for d in col.find({"username":x}):
    if y==d['password']:
        print("login success")