from pydantic import BaseModel,Field

class user(BaseModel):
    age_gt:int = Field(gt=18)
    age_ge:int = Field(ge=18)
    age_lt:int =Field(lt=80)
    age_le:int =Field(le=80)

    name:str =Field(max_length=5)
    name1:str =Field(min_length=2)

    user_age:int = Field(default=25,description="NO value",title="This is an Title",examples=[25])

user1=user(age_gt=20,age_ge=18,age_lt=55,age_le=80,name="sat",name1="satej")

print(user1)
print(user1.user_age)