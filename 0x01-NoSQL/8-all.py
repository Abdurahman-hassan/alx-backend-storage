#!/usr/bin/python3
""" 8-all """
import pymongo


def list_all(mongo_collection):
    """ list all documents in Python"""
    if not mongo_collection:
        return []
    return mongo_collection.find()
