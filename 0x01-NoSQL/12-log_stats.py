#!/usr/bin/env python3
"""12-log_stats - Provides statistics about Nginx logs stored in MongoDB."""
from pymongo import MongoClient


def log_stats():
    """Prints statistics about Nginx logs."""
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx

    # Count total logs
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # Print methods statistics
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = nginx_collection.count_documents({'method': method})
        print(f"\tmethod {method}: {count}")

    # Count documents where method=GET and path="/status"
    status_checks = nginx_collection.count_documents({'method': 'GET', 'path': '/status'})
    print(f"{status_checks} status check")


if __name__ == "__main__":
    log_stats()
