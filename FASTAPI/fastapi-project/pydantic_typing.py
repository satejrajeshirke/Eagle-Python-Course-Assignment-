from pydantic import BaseModel,Field
from typing import List,Dict,Tuple,Set,Optional,Annotated


class student(BaseModel):
    subjects:List[str]
    marks:Dict[str,int]
    student_info:Tuple[str,int]
    numbers:Set[int]
    ph_no:Optional[str] = None

    age:Annotated[int,Field(gt=0)]

student1=student(
    subjects=["Python", "FastAPI", "MongoDB"],
    marks={"Python": 85, "FastAPI": 90},
    student_info=("Satej", 21),
    numbers={10, 20, 30},
    phone="9876543210",
    age=21
)

print(student1)