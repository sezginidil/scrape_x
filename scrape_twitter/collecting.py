from pydantic import Json
from .schemas import (
    Trends
)


def collect_trends(n: int) -> Json:
    """
    Args:
       n (int): maximum number of trends, which should be collected

    Returns:
        Json: trends in json format.
    """
    return Trends.model_dump(mode="json")
