#!/usr/bin/env python3
'''Task 0's module'''
import redis
import uuid
from typing import Union


class Cache:
    '''Cache class'''


    def __init__(self) -> None:
        '''init method'''
        self._redis = redis.Redis()
        self._redis.flushdb()


    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''sets a data and return the key'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
