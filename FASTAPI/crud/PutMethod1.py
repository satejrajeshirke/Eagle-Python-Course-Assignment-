from fastapi  import FastAPI
from pydantic import BaseModel,Field,EmailStr
from typing import Annotated,Optional
import json

app=FastAPI()

class student(BaseModel):
    name:Annotated[Optional[str],Field(titel="Enter YOur Name Here",default=None)]
    age:Annotated[Optional[str],Field(title="Enter Your Age Here",default=None)]
    email:Annotated[Optional[EmailStr],Field(title="Enter Your Email Here",default=None)]



@app.get("/")
def greet():
    return{"message":"Hello"}


@app.put("/edit/{roll}")
def opeartion(roll:int,updateinfo:student):
    with open("all_student12.json","r") as f:
        alldata=json.load(f)

    for i in alldata:
        if i["roll"]==roll:

            if updateinfo.name != None:
                i["name"]=updateinfo.name

            if updateinfo.age != None:
                i["age"]=updateinfo.age

            if updateinfo.email != None:
                i["email"]=updateinfo.age

    with open("all_student12.json","w") as f2:
        json.dump(alldata,f2)

    return{"meassage:","student updated"}



