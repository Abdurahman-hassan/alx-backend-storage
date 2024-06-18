#!/usr/bin/env python3
""" 10-update_topics """
import pymongo


def update_topics(mongo_collection, name, topics):
    """ Update a document in Python """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
