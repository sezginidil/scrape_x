from pydantic import BaseModel, Field
from typing import List, Optional

class Trend(BaseModel):
    """User basic information, contains `id`, `username`, `fullname`, `profile_pic_url` and `is_verified`."""
    header:str = Field(None, description="category or location based", examples=["Trending in (location)", "(category) · Trending"])
    title: str = Field(None, description="title of the trend")
    numnber_of_posts: Optional[str] = Field(None, description="Shows number of post under the category", examples=["3,373 posts"])

class Trends(BaseModel):
    """An aggregation class to have the field `trends` for storing a list of instances of `Trend`."""
    trends: List[Trend] = Field(...,
                                description="A list of trends.",
                                examples=[[]])
                            