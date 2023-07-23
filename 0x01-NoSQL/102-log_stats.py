#!/usr/bin/env python3
"""Task 15's module"""


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


def print_top_ips(server_collection):
    """Prints stats for top 10 HTTP IPs in a collection"""
    print("IPs:")
    reqest_logs = server_collection.aggregate([
        {
            "$group": {
                "_id": "$ip",
                "totalRequests": {"$sum": 1}
            }
        },
        {
            "$sort": {"totalRequests": -1}
        },
        {"$limit": 10}
    ])

    for log in request_logs:
        ip = log['_id']
        ip_request_count = log['totalRequests']
        print("\t{}: {}".format(ip, ip_request_count))


def run():
    '''Provides some stats about Nginx logs stored in Mongodb'''
    client = MongoClient('mongdb://127.0.0.1:27017')
    print_nginx_logs(client.logs.nginx)
    print_top_ips(client.logs.nginx)


if __name__ == '__main__':
    run()
