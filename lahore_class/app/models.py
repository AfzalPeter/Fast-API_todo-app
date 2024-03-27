# models.py
from typing import Optional
from sqlmodel import Field, SQLModel

class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content: str = Field(index=True)
