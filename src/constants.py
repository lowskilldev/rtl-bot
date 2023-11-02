from enum import auto

from src.enums import AutoName

class GroupType(AutoName):
    HOUR = auto()
    DAY = auto()
    MONTH = auto()

date_format = {
    GroupType.HOUR: "%Y-%m-%dT%H:00:00", 
    GroupType.DAY: "%Y-%m-%dT00:00:00", 
    GroupType.MONTH: "%Y-%m-01T00:00:00"
}
