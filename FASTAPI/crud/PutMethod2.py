from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Annotated,Optional
import json

app=FastAPI()

class student(BaseModel):
    name:Annotated[Optional[str],Field(title="Enter Your Name",default=None)]
    age:Annotated[Optional[int],Field(title="Enter Your Roll",default=None)]
    email:Annotated[Optional[str],Field(title="Enter Your age",default=None)]



@app.get("/")
def greet():
    return{"message":"Hello"}


@app.put("/edit/{roll}")
def updateinfo(roll:int,updateinfo:student):
    with open("All_student456.json","r") as f:
        alldata=json.load(f)

    for i in alldata:
        if i["roll"]==roll:

            if updateinfo.name != None:
                i["name"]=updateinfo.name

            if updateinfo.age != None:
                i["age"] = updateinfo.age

            if updateinfo.email != None:
                i["email"]  = updateinfo.email


    with open ("All_student456.json","w") as f2:
        json.dump(alldata,f2)

    return{"messge":"new student added succesfully"}