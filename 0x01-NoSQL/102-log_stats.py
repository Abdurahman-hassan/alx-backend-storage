#!/usr/bin/env python3
""" 12-log_stats module """
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx
    count = logs_collection.count_documents({})
    print("{} logs".format(count))
    print("Methods:")
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        meth_count = logs_collection.count_documents(
            {"method": {
                "$eq": method
            }})
        print("\tmethod {}: {}".format(method, meth_count))

    status_checks = logs_collection.count_documents(
        {"$and": [{
            "method": {
                "$eq": 'GET'
            }
        }, {
            "path": "/status"
        }]})
    print("{} status check".format(status_checks))

    # Top 10 IPs
    print("IPs:")
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = logs_collection.aggregate(pipeline)
    for ip in top_ips:
        print("\t{}: {}".format(ip["_id"], ip["count"]))
