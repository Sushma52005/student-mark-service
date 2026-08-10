from pydantic import BaseModel, Field


class Student(BaseModel):
    id: int = Field(gt=0)
    name: str
    maths: int = Field(ge=0, le=100)
    physics: int = Field(ge=0, le=100)
    chemistry: int = Field(ge=0, le=100)