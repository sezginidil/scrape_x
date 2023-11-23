from pydantic import BaseModel, Field
from typing import List, Optional


class Trend(BaseModel):
    """
    Trends
    """
    header: str = Field(None,
                        description="category or location based",
                        examples=["Trending in (location)", "(category) · Trending"])
    title: str = Field(None,
                       description="title of the trend")
    number_of_posts: Optional[str] = Field(None,
                                           description="Shows number of post under the category",
                                           examples=["3,373 posts"])


class Trends(BaseModel):
    """An aggregation class containing list of instances of `Trend`."""
    trends: List[Trend] = Field(...,
                                description="A list of trends.",
                                examples=[[]])
