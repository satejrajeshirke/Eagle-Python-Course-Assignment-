from fastapi import FastAPI
from pymongo import MongoClient



connectionstring=MongoClient("mongodb://localhost:27017/")
database=connectionstring["Student1"]
collection=database["allstudents"]

app=FastAPI()

@app.get("/")
def greet():
    return{"message":"hello"}

@app.delete("/delete/{roll}")
def deletestud(roll:int):
    allstude=list(collection.find({},{"roll":1,"_id":0}))

    for i in allstude:
        if i["roll"]==roll:
            collection.delete_one({"roll":roll})
            return{"message":"student deleted"}
        
    return{"message":"student not found"}