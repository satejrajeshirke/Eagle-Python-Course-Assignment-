from pydantic import BaseModel,Field
from typing import Annotated,Optional


class UpdateStruct(BaseModel):
    name: Annotated[Optional[str],Field(title="Enter your rollno",default=None)]
    age: Annotated[Optional[int],Field(title="Enter your rollno",default=None)]







