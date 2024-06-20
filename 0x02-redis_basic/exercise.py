#!/user/bin/env python3
""" Redis exercise """
import redis
from typing import Union, Optional, Callable
from uuid import uuid4
from functools import wraps

def count_calls(method: Callable) -> Callable:
    """ Count the number of calls to a function """
    key = method.__qualname__
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper function """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper
