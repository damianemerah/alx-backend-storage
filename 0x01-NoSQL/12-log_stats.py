#!/usr/bin/env python3
"""Task 12's script to provide some stats about Nginx logs stored in MongoDB."""

from pymongo import MongoClient

def print_nginx_logs(nginx_collection):
    """Prints stats about nginx request logs"""
    # Get the total number of logs
    total_logs = nginx_collection.count_documents({})

    # Get the count of each method
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    method_counts = {}
    for method in methods:
        method_count = nginx_collection.count_documents({"method": method})
        method_counts[method] = method_count

    # Get the count of status checks
    status_check_count = nginx_collection.count_documents({"method": "GET", "path": "/status"})

    # Print the results
    print("{} logs".format(total_logs))
    print("Methods:")
    for method, count in method_counts.items():
        print("\tmethod {}: {}".format(method, count))
    print("{} status check".format(status_check_count))


def run():
    """Provides some stats about Nginx logs in the database."""
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    print_nginx_logs(nginx_collection)


if __name__ == '__main__':
    run()
