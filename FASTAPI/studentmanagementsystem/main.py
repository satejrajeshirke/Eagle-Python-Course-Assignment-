from Routes.studentroutes import router

from fastapi import FastAPI

app=FastAPI()

app.include_router(router)

@app.get("/")
def Homepage():
    return{"message":"Student Management System"}