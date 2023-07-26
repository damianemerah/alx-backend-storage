#!/usr/bin/env python3
'''Task 5's module'''
import redis
import requests


def request_count(method):
    '''decorator for counting'''
    @wraps(method)
    def invoker(url):
        '''decorator wrapper'''
        redis_ = redis.Redis()
        redis_.incr(f"count:{url}")
        cached_url = redis_.get(url)

        if cached_url:
            return cached_url.decode('utf-8')

        content = method(url)
        redis_.setex(cached_url, 10, content)
        return content
    return invoker


@request_count
def get_page(url: str) -> str:
    '''obtain the HTML content of a particular URL'''
    req = requests.get(url)
    return req.text
