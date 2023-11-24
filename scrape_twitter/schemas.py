from pydantic import BaseModel, Field
from typing import List, Optional


class Trend(BaseModel):
    """
    Trend
    """
    header: str = Field(...,
                        description="category or location based",
                        examples=["Trending in (location)", "(category) · Trending"])
    title: str = Field(...,
                       description="title of the trend")
    number_of_posts: Optional[str] = Field(None,
                                           description="Shows number of post under the category",
                                           examples=["3,373 posts"])


class Trends(BaseModel):
    """An aggregation class containing list of instances of `Trend`."""
    trends: List[Trend] = Field(...,
                                description="A list of trends.",
                                examples=[[]])


class UserBasicInfo(BaseModel):
    """Basic user information that can be collected without going to the profile of the user"""
    given_name: str = Field(...,
                            description="user's name, usually consists of first name and surname",
                            examples=["İdil Sezgin"])
    username: str = Field(...,
                          description="4-15 characters"
                          "Letters A-Z"
                          "Numbers 0-9"
                          "Underscore symbol")
    user_photo: str = Field(...,
                            description="Url of the user avatar."
                            " Never null, if no avatar was chosen its the anonymous profile photo")
    user_bio: Optional[str] = Field(None,
                                    desctiption="0 - 160 characters"
                                    "Can contain @usernames, #hashtags and urls")
    private_account: bool = Field(False)
    verified_account: bool = Field(False)


class Users(BaseModel):
    users: List[UserBasicInfo] = Field(..., description="A list of users with basic info")
