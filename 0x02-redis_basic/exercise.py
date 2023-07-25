#!/usr/bin/env python3
'''Task 0's module'''
import redis
import uuid
from typing import Union, Callable


class Cache:
    '''Cache class'''


    def __init__(self) -> None:
        '''init method'''
        self._redis = redis.Redis()
        self._redis.flushdb(True)


    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''sets a data and return the key'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key


    def get(key: str, fn: Callable = None) -> Union[str, float, int, byte]:
        '''converts the data back to desired format'''
        data = self._redis.get(key)
        if fn is not None:
            return fn(key)
        return data


    def get_str(self, key: str) -> str:
        '''Retrieves a string value from a Redis data storage'''
        return self.get(key, fn=lambda d: d.decode('utf-8'))


    def get_int(self, key: int) -> int:
         '''Retrieves an int value from a Redis data storage'''
         return self.get(key, fn= int(x))
