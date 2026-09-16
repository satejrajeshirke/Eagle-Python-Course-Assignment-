from fastapi import APIRouter
from Controller.StudentController import Createstudent
from model.StudentModel import StudentStruct
from model.StudentUpdate import updateStruct
from Database.dbconnection import collection


router=APIRouter()


@router.post("/createstudent")
def create(student:StudentStruct):
    return Createstudent(student)
    


@router.get("/allstudent")
def Getstudent():
    alldata=list(collection.find({},{"_id":0}))
    return alldata


@router.put("/edit/{roll}")
def UpdateStudent(roll:int,student:updateStruct):
    alldata=list(collection.find({},{"_id":0}))


    updatedstudent={}

    for i in alldata:
        if i["roll"]==roll:

            if student.name != None:
                updatedstudent["name"]=student.name

            if student.age != None:
                updatedstudent["age"]=student.age

        collection.update_one(
            {"roll":roll},
            {"$set":updatedstudent}
        )

        return{"message":"Student Updated"}


@router.delete("/delete/{roll}")
def deletestudent(roll:int):
    alldata=list(collection.find({},{"_id":0}))

    for i in alldata:
        if i["roll"]==roll:
            collection.delete_one({"roll":roll})
            return {"message":"student deleted"}



