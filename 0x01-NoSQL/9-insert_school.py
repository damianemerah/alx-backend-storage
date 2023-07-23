"""
Write a Python function that inserts a new document
in a collection based on kwargs:

Prototype: def insert_school(mongo_collection, **kwargs):
mongo_collection will be the pymongo collection object
Returns the new _id
"""


def insert_school(mongo_collection, **kwargs):
    """Insert kwargs to mongo_collection"""
    return mongo_collection.insert_one(kwargs).inserted_id
