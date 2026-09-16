from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Annotated
import json
from pymongo import MongoClient


ConnectString=MongoClient("mongodb://localhost:27017/")
database=ConnectString["Student1"]
collection=database["allstudents"]

app=FastAPI()

class Student(BaseModel):
    name:str = Field(title="Enter Your Name")
    roll:int =Field(title="Enter Your Roll")




@app.get("/")
def greet():
    return {"Message":"Student Managment"}


@app.post("/register")
def register(student:Student):
    sname=student.name
    sroll=student.roll

    sinfo={
        "name":sname,
        "roll":sroll
    }
    

    with open("all_stud3.json","r") as f:
        alldata=json.load(f)
        alldata.append(sinfo)

    with open("all_stud3.json","w") as f2:
        json.dump(alldata,f2)


    
    collection.insert_one(sinfo)

    return{
        "massage":"new student succesfully added in mongo and json",
        "student":student
    }

