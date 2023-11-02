from datetime import datetime

from dotenv import load_dotenv
from database.client import database, DB_COLLECTION

from enums import GroupType

from utils.time import add_delta

load_dotenv()

date_format = dict(hour="%Y-%m-%dT%H:00:00", day="%Y-%m-%dT00:00:00", month="%Y-%m-01T00:00:00")

async def aggregate_payouts(
    start_date: datetime,
    end_date: datetime,
    group_type: str = "month"
):
    print("group_type->", group_type)

    # upper_bound = add_delta(end_date, group_type)
    upper_bound = end_date

    print(upper_bound)

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

