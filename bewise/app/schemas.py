from datetime import datetime

from pydantic import BaseModel


class ApplicationCreate(BaseModel):
    user_name: str
    description: str


class ApplicationDB(BaseModel):
    id: int
    user_name: str
    description: str
    created_at: datetime

    class Config:
        orm_mode = True
        from_attributes = True
