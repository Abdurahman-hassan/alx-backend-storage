#!/usr/bin/env python3
""" 0x02-redis_basic """
import redis
import requests
from typing import Callable
from functools import wraps

# Initialize Redis client
redis_client = redis.Redis(host='localhost', port=6379, db=0)


def cache_page(expiration: int = 10) -> Callable:
    """
    Decorator to cache the HTML content of a URL with an expiration time.
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(url: str) -> str:
            cached_page = redis_client.get(url)
            if cached_page:
                return cached_page.decode('utf-8')

            page_content = func(url)
            redis_client.setex(url, expiration, page_content)
            return page_content

        return wrapper

    return decorator


def count_accesses(func: Callable) -> Callable:
    """
    Decorator to count how many times a particular URL was accessed.
    """

    @wraps(func)
    def wrapper(url: str) -> str:
        count_key = f"count:{url}"
        redis_client.incr(count_key)
        return func(url)

    return wrapper


@cache_page(expiration=10)
@count_accesses
def get_page(url: str) -> str:
    """
    Obtain the HTML content of a particular URL and return it.
    """
    response = requests.get(url)
    return response.text
