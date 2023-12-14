from pydantic import Json
from .schemas import (
    Trends, Users, UserDetailedInfo, Tweets, TweetWithInteraction
)


def collect_trends(n: int) -> Json:
    """
    Args:
       n (int): maximum number of trends, which should be collected

    Returns:
        Json: trends in json format.
    """
    return Trends().model_dump(mode="json")


def collect_followers(username: str, n: int = 100) -> Json:
    """ Collect n followers of the given user.

    Args:
        username (str): username of the user.
        n (int): maximum number of followers, which should be collected. By default,
         it's 100. If it's set to 0, collect all followers.

    Returns:
       Json: basic followers' information of the given user in json format.
    """
    return Users().model_dump(mode="json")


def collect_following(username: str, n: int = 100) -> Json:
    """ Collect n following of the given user.

    Args:
        username (str): username of the user.
        n (int): maximum number of following, which should be collected. By default,
         it's 100. If it's set to 0, collect all following.

    Returns:
        Json: basic following' information of the given user in json format.
    """
    return Users().model_dump(mode="json")


def collect_users_with_keyword(keyword: str, n: int = 100) -> Json:
    """ Collect n users related to given keyword

    Args:
        keyword (str): keyword
        n (int): maximum number of users

    Returns:
        Json: basic user infotmation based related to given keyword in json format.
    """
    return Users().model_dump(mode="json")


def collect_user_info(username: str) -> Json:
    """ Collect all collectable information from user's profile.

    Args:
        username (str): username of the user

    Returns:
        Json: detailed user infotmation
    """
    return UserDetailedInfo().model_dump(mode="json")


def collect_tweets_of_user(username: str, n: int = 100) -> Json:
    """ Collect n tweets of the given user.

    Args:
        username (str): username of the user.
        n (int): maximum number of tweets, which should be collected. By default,
         it's 100. If it's set to 0, collect all tweets.

    Returns:
        Json: tweet objects in json format.
    """
    return Tweets().model_dump(mode="json")


def collect_media_of_user(username: str, n: int = 100) -> Json:
    """ Collect n tweets of the given user with media.

    Args:
        username (str): username of the user.
        n (int): maximum number of tweets, which should be collected. By default,
         it's 100. If it's set to 0, collect all tweets.

    Returns:
        Json: tweet objects with media in json format.
    """
    return Tweets().model_dump(mode="json")


def collect_likes_of_user(username: str, n: int = 100) -> Json:
    """ Collect n tweets the given user has liked.

    Args:
        username (str): username of the user.
        n (int): maximum number of tweets, which should be collected. By default,
         it's 100. If it's set to 0, collect all tweets.

    Returns:
        Json: tweet objects with media in json format.
    """
    return Tweets().model_dump(mode="json")


def collect_tweets_with_keyword(keyword: str, n: int = 100) -> Json:
    """ Collect n tweets related to given keyword

    Args:
        keyword (str): keyword
        n (int): maximum number of tweets

    Returns:
        Json: tweet objects in json format.
    """
    return Tweets().model_dump(mode="json")


def collect_tweets_with_hashtag(hashtag: str, n: int = 100) -> Json:
    """ Collect n tweets which include given hashtag

    Args:
        hashtag (str): hashtag
        n (int): maximum number of tweets

    Returns:
        Json: tweet objects in json format.
    """
    return Tweets().model_dump(mode="json")


def collect_tweet_with_id(id: str) -> Json:
    """ Collect all information related to given tweet id.

    Args:
        id (str): username of the user.

    Returns:
        Json: detailed tweet object
    """
    return TweetWithInteraction().model_dump(mode="json")
