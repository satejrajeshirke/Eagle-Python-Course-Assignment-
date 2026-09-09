from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Annotated
import json 

app=FastAPI()

class Studentstruct(BaseModel):
    name:Annotated[str,Field(title="Enter Your Name")]
    roll:Annotated[int,Field(title="Enter Your Roll")]


@app.get("/")
def greet():
    return{"message":"student Managemnet System"}


@app.post("/register")
def register(Studentinfo:Studentstruct):

    sname=Studentinfo.name
    sroll=Studentinfo.roll

    sinfo= {
        "name":sname,
        "roll":sroll
    }

    with open("All_student.json","r") as f:
        alldata=json.load(f)
        alldata.append(sinfo)
        
    with open("All_student.json","w") as f2:
        json.dump(alldata,f2)

    return {"Message":"New Stundet added"}

