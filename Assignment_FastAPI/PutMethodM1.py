from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Annotated, Optional
from pymongo import MongoClient

connectionstring = MongoClient("mongodb://localhost:27017/")
database = connectionstring["student11"]
collection = database["allstudentss"]

app = FastAPI()


class student(BaseModel):
    name: Annotated[Optional[str], Field(title="Enter Your Name", default=None)]
    age: Annotated[Optional[int], Field(title="Enter YOUR age", default=None)]
    email: Annotated[Optional[str], Field(title="Enter Your Email", default=None)]


@app.get("/")
def greet():
    return {"message": "hello"}


@app.put("/edit/{roll}")
def updateinfo(roll: int, updateinfo: student):

    data = {}

    if updateinfo.name != None:
        data["name"] = updateinfo.name

    if updateinfo.age != None:
        data["age"] = updateinfo.age

    if updateinfo.email != None:
        data["email"] = updateinfo.email

    collection.update_one(
        {"roll": roll},
        {"$set": data}
    )

    return {
        "message": "Student updated successfully"
    }

    