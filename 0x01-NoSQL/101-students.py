#!/usr/bin/env python3
"""Task 14's module"""


def top_students(mongo_collection):
    """returns all students sorted by average score:"""
    pipeline = [
        {
            "$project": {
                "name": 1,
                "_id": 1,
                "averageScore": {
                    "$avg": "$topics.score"
                }
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]

    return list(mongo_collection.aggregate(pipeline))
