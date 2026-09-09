from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Annotated
from pymongo import MongoClient

ConnectString = MongoClient("mongodb://localhost:27017/")
database = ConnectString["Student1"]
collection=database["allstudents"]

app=FastAPI()

class StudStruct(BaseModel):
    name:Annotated[str,Field(title="Enter Your Name")]
    roll:Annotated[str,Field(title="Enter YOur Age")]

@app.get("/")
def greet():
    return {"message":"Student Management System"}


@app.post("/register")
def newstudent(studentinfo:StudStruct):
    sname=studentinfo.name
    sroll=studentinfo.roll

    sinfo= {
        "name":sname,
        "roll":sroll
    }

    collection.insert_one(sinfo)

    return{"message":"new student added succesfully in student table "}