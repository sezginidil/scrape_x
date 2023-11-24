from pydantic import Json
from .schemas import (
    Trends, Users
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
        username (str): name of the user.
        n (int): maximum number of followers, which should be collected. By default,
        it's 100. If it's set to 0, collect all followers.

    Returns:
       Json: basic followers' user information of the given user in json format.
    """
    return Users().model_dump(mode="json")


def collect_following(username: str, n: int = 100) -> Json:
    """ Collect n following of the given user.

    Args:
        username (str): name of the user.
        n (int): maximum number of following, which should be collected. By default,
        it's 100. If it's set to 0, collect all followers.

    Returns:
        Json: basic following' user information of the given user in json format.
    """
    return Users().model_dump(mode="json")


def collect_users_with_keyword(keyword: str, n: int = 100) -> Json:
    """ Collect n following of the given user.

    Args:
        username (str): name of the user.
        n (int): maximum number of following, which should be collected. By default,
        it's 100. If it's set to 0, collect all followers.

    Returns:
        Json: basic user infotmation based related to given keyword in json format.
    """
    return Users().model_dump(mode="json")
