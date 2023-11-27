from xmlrpc.client import DateTime
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
                                description="A list of trends.")


class UserBasicInfo(BaseModel):
    """Basic user information that can be collected without going to the profile of the user"""
    given_name: str = Field(...,
                            description="user's name, usually consists of first name and surname",
                            examples=["İdil Sezgin"])
    username: str = Field(...,
                          description="4-15 characters "
                          "Letters A-Z "
                          "Numbers 0-9 "
                          "Underscore symbol")
    user_photo: str = Field(...,
                            description="Url of the user avatar."
                            " Never null, if no avatar was chosen its the anonymous profile photo")
    user_bio: Optional[str] = Field(...,
                                    desctiption="0 - 160 characters"
                                    "Can contain @usernames, #hashtags and urls")
    private_account: bool = Field(False)
    verified_account: bool = Field(False)


class Users(BaseModel):
    users: List[UserBasicInfo] = Field(..., description="A list of users with basic info")


class UserDetailedInfo(UserBasicInfo):
    """All the information that can be collected from a profile"""
    header_photo: Optional[str] = Field(..., description="Url of the header photo")
    user_birth_date: Optional[str] = Field(..., description="User's birthday",
                                           examples=["Born September 13"])
    user_join_date: str = Field(..., description="User's join date to the platform",
                                examples=["Joined June 2015"])
    user_location: Optional[str] = Field(..., description="0-30 characters, could be any string")
    user_website: Optional[str] = Field(..., description="website url")
    number_of_followers: int = Field(None)
    number_of_following: int = Field(None)
    number_of_posts: int = Field(None)


class BasicTweet(BaseModel):
    date: DateTime = Field(None)
    text: str = Field(..., description="Max 280 characters")
    hashtags: Optional[str] = Field(..., description="Hastag in the url form")
    image: Optional[str] = Field(..., description="Image url")
    number_of_replies: int = Field(None)
    number_of_reposts: int = Field(None)
    number_of_likes: int = Field(None)
    number_of_views: int = Field(None)
    social_content: Optional[str] = Field(..., description="Link to retweeter")
    replyting_to: Optional[str] = Field(..., description="Hastag in the url form")


class Tweet(BaseModel):
    quotes: Optional[BasicTweet] = Field(None)
    replies: Optional[List[BasicTweet]] = Field(None)
    reposts: Optional[List[UserBasicInfo]] = Field(None)
    likes: Optional[List[UserBasicInfo]] = Field(None)


class Tweets(BaseModel):
    tweets: List[BasicTweet] = Field(..., description="A list of tweets")
