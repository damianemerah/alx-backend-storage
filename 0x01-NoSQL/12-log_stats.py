#!/usr/bin/env python3
"""Task 12's module"""
from pymongo import MongoClient


def print_nginx_logs(nginx_collection):
    """Prints stats about nginx request logs"""
    print("{} logs".format(nginx_collection.count_documents({})))
    print("Methods:")
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

    for method in methods:
        req_count = len(list(nginx_collection.find({"methods": method})))
        print("\tmethod {}: {}".format(method, req_count))
    status_check_count = len(list(
        nginx_collection.find({"methods": "GET", "path": "/status"})
    ))
    print("{} status check".format(status_check_count))


def run():
    """Provides some stats about Nginx log in db"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    print_nginx_logs(client.logs.nginx)


if __name__ == '__main__':
    run()
