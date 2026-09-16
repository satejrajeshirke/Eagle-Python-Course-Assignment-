from pydantic import BaseModel,Field
from typing import Annotated,Optional


class updateStruct(BaseModel):
        name:Annotated[Optional[str],Field(title="Enter Your Name:",default=None)]
        age:Annotated[Optional[int],Field(title="Enter You Age:",default=None)]

