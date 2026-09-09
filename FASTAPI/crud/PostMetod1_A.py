from fastapi import FastAPI
import json
from typing import Annotated
from pydantic import BaseModel,Field

app=FastAPI()

class StudentStruct(BaseModel):
    name:Annotated[str,Field(title="Enter your Name")]
    roll:Annotated[int,Field(title="Enter Your RollNO")]

@app.get("/")
def greet():
    return{"Message":"Student Management System"}

@app.post("/register")
def register(studentinfo:StudentStruct):
    sname=studentinfo.name
    sroll=studentinfo.roll


    sinfo={
        "name":sname,
        "roll":sroll
    }

    with open("All_stud.json","r") as f:
        alldata=json.load(f)
        alldata.append(sinfo)

    with open("All_stud.json","w") as f2:
        json.dump(alldata,f2)

    return {"message":"new user added sucess fully"}



    







