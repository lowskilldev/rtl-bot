from datetime import datetime

from src.database.client import database, DB_COLLECTION
from src.constants import GroupType, date_format
from src.utils.time import add_delta

async def aggregate_payouts(
    start_date: datetime,
    end_date: datetime,
    group_type: GroupType = GroupType.MONTH
):
    upper_bound = add_delta(end_date, group_type)

    pipeline = [
        {
            "$densify": {
                "field": "dt",

                "range": {
                    "step": 1,
                    "unit": group_type,
                    "bounds": [start_date, upper_bound],
                },
            }
        },

        {
            "$match": {
                "dt": {
                    "$gte": start_date, 
                    "$lte": end_date
                }
            }
        },

        {
            "$group": {
                "_id": {
                    "$dateToString": {
                        "format": date_format[group_type],
                        "date": "$dt",
                    }
                },

                "total": {
                    "$sum": "$value"
                },
            }
        },

        {
            "$sort": {
                "_id": 1
            }
        },

        {
            "$facet": {
                "dates": [], 
                "sums": []
            }
        },

        {
            "$project": {
                "dataset": {
                    "$map": {
                        "input": "$sums",
                        "as": "item",
                        "in": "$$item.total",
                    }
                },

                "labels": {
                    "$map": {
                        "input": "$dates",
                        "as": "item",
                        "in": "$$item._id",
                    }
                },
            }
        },
    ]

    result = await database[DB_COLLECTION].aggregate(pipeline).to_list(length=1)

    return result[0]

