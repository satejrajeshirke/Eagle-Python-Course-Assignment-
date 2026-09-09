"""
1. Create a POST API to store student details.

Each student should contain:

name
roll
age
year
email
subjects with marks
hobbies
Any other useful student information

Example student data:

{
    "name": "demo",
    "roll": 101,
    "age": 21,
    "year": "Final Year",
    "email": "demo@gmail.com",
    "subjects": {
        "python": 85,
        "java": 78,
        "database": 90
    },
    "hobbies": ["coding", "cricket", "reading"]
}

Use Pydantic BaseModel to define and validate the student structure.

"""

from fastapi import FastAPI
from pydantic import BaseModel,Field,EmailStr
from typing import Annotated,Dict,Set

app=FastAPI()


class Student(BaseModel):
    name:str = Field(min_length=2)
    roll:int= Field(gt=0)
    age:int =Field(ge=1)
    year:str 
    email:EmailStr
    subjects:dict[str,int]
    hobbies:set[str]

@app.post("/studentdata")
def studentdata(student:Student):
    return {
        "message":"student details stored sucessfully",
            "Student":student
    }


