import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017")
print("connected")
db=client["class"]
col=db["details"]
x=input("enter your user name")
y=int(input("enter your password"))
users={
    "username":x,
    "password":y,
}
col.insert_one(users)
