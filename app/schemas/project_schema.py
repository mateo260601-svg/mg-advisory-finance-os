from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ProjectCreate(BaseModel):
    company_name: str = Field(..., min_length=2, max_length=160)
    project_type: str = Field(default="Investment case", max_length=80)
    currency: str = Field(default="EUR", max_length=8)
    fiscal_year_end: str = Field(default="December", max_length=20)


class Project(BaseModel):
    id: str
    company_name: str
    project_type: str
    currency: str
    fiscal_year_end: str
    created_at: datetime
    updated_at: datetime
    status: str = "active"
    notes: Optional[str] = None
