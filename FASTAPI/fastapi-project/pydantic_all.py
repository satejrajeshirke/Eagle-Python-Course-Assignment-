from pydantic import BaseModel, Field
from typing import List, Tuple, Dict, Optional, Annotated, Set


class Student(BaseModel):

    subjects: List[str]

    marks: Dict[str, int]

    student_info: Tuple[str, int]

    numbers: Set[int]

    phone_no: Optional[str] = None

    age: Annotated[int, Field(gt=0)]

    user_age: int = Field(
        default=25,
        description="User age",
        title="Age",
        examples=[25]
    )

    name: str = Field(
        max_length=5,
        min_length=1
    )


student1 = Student(
    subjects=["Python", "FastAPI", "MongoDB"],
    marks={
        "Python": 85,
        "FastAPI": 90
    },
    student_info=("Satej", 21),
    numbers={10, 20, 30},
    phone_no="9876543210",
    age=21,
    name="Satej"
)


print(student1)

print("Subjects:", student1.subjects)
print("Marks:", student1.marks)
print("Student Info:", student1.student_info)
print("Numbers:", student1.numbers)
print("Phone:", student1.phone_no)
print("Age:", student1.age)
print("User Age:", student1.user_age)
print("Name:", student1.name)