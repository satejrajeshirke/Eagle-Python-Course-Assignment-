"""
4. Path Parameter  Find Student

Create APIs using path parameters to find a particular student.

Find student by name:
GET /student/{name}

Find student by roll:
GET /student/{roll}

"""
from fastapi import FastAPI
import json 

app=FastAPI()

@app.get("/")
def greet():
    return{"massage":"Student Management System"}

@app.get("/allstudents")
def allstudent():
    with open("All_student.json","r") as f:
        allstudent=json.load(f)
        return allstudent

@app.get("/student/name/{name}")
def studentfind(name):
    with open("All_student.json","r") as f1:
        allstudent=json.load(f1)

        for i in allstudent:
            if i["name"]==name:
                return i
            
        return {"massage":"user not found"}

@app.get("/student/roll/{roll}")
def studentfind(roll:int):
    with open("All_student.json","r") as f3:
        allstudent=json.load(f3)

        for i in allstudent:
            if i["roll"]==roll:
                return i
            
        return {"massage":"Roll not found"}

