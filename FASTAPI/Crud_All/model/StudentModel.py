from pydantic import BaseModel,Field
from typing import Annotated

class StudentStruct(BaseModel):
    roll:Annotated[int,Field(title="Enter Your Roll")]
    name:Annotated[str,Field(title="Enter Your Name")]
    age:Annotated[int,Field(title="Enter Your Age")]


    