from pydantic import BaseModel, Field
from typing import List, Optional


class Trend(BaseModel):
    """ Trend object . Trends are shown based on user's location
    likes and history. Sometimes it is category based and sometimes
    is location based. Header and title is always there, and some cases
    we also have the number of posts about that trend."""
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
    """An aggregation class containing list of instances of `UserBasicInfo`."""
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


class BasicTweetInfo(BaseModel):
    """Basic tweet information that can be collected without going to the tweet's url."""
    author: UserBasicInfo = Field(..., description="Basic information about the user who"
                                  " has posted given tweet")
    date: str = Field(..., description="When the tweet was created, in string form",
                      examples=["9:02 PM · Sep 3, 2023"])
    text: str = Field(..., description="Max 280 characters")
    language: str = Field(..., description="Language of the tweet",
                          examples=["Joined June 2015"])
    hashtags: Optional[List[str]] = Field(..., description="List of Hastag urls")
    mentions: Optional[List[str]] = Field(..., description="List of user profile urls who"
                                          " have been mentioned in the given tweet")
    image: Optional[str] = Field(..., description="Image url")
    number_of_replies: int = Field(None)
    number_of_reposts: int = Field(None)
    number_of_likes: int = Field(None)
    number_of_views: int = Field(None)
    replyting_to: Optional[str] = Field(..., description="Link to replying user")
    conversation_id: str = Field(..., description="Conversation id")


class Tweets(BaseModel):
    """An aggregation class containing list of instances of `Tweet`."""
    tweets: List[BasicTweetInfo] = Field(..., description="A list of tweets")


class TweetDetails(BaseModel):
    """All the information that can be collected with a tweet id"""
    basic_tweet_info: BasicTweetInfo = Field(None)
    quote: Optional[BasicTweetInfo] = Field(None, description="The original"
                                            "tweet which the given tweet quotes")
    replies: Optional[List[BasicTweetInfo]] = Field(None, description="List of tweets which are"
                                                    "replies of the given tweet")
    reposters: Optional[List[UserBasicInfo]] = Field(None, description="List of users who have "
                                                     "reposted the given tweet")
    likers: Optional[List[UserBasicInfo]] = Field(None, description="List of users who have"
                                                  "liked the given tweet")
