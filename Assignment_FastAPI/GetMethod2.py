"""
3. GET – Get All Students

Create a GET API:

GET /allstudents
"""

from pydantic import BaseModel,Field
from fastapi import FastAPI
from pymongo import MongoClient


ConnectString=MongoClient("mongodb://localhost:27017/")
database=ConnectString["Student1"]
connection=database["allstudents"]

app=FastAPI()

@app.get("/allstudents")
def studentdata():
    alldata=list(connection.find({},{"name":1,"roll":1,"_id":0}))

    return alldata


