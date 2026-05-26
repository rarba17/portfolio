from typing import Literal

from pydantic import BaseModel, Field


class Project(BaseModel):
    id: int
    title: str
    role: str
    stack: list[str]
    description: str
    live_url: str
    github_url: str
    mood: Literal["mustard", "plum", "rust", "slate"]


class Article(BaseModel):
    id: int
    title: str
    summary: str
    url: str
    published_at: str = Field(description="ISO date string")
