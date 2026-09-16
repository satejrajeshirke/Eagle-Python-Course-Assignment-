from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("MongoDbUrl")

ConnectionString=MongoClient(url)

database=ConnectionString["Student1000"]
collection=database["allstudents"]