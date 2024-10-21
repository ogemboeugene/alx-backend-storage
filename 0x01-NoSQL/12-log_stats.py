#!/usr/bin/env python3
'''
script that provides some stats about Nginx logs stored in MongoDB
'''


def nginx_stats():
    '''
    provides some stats about Nginx logs stored in MongoDB
    '''
    import pymongo

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["logs"]
    collection = db["nginx"]

    total_logs = collection.count_documents({})

    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents({
        "method": method}) for method in methods}

    print("Methods:")
    for method, count in method_counts.items():
        print(f"\tmethod {method}: {count}")

    status_check_count = collection.count_documents({
        "method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")


if __name__ == '__main__':
    nginx_stats()
