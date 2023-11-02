from enum import Enum, auto

class AutoName(str, Enum):
    def _generate_next_value_(self, *args):
        return self.lower()
    
    def __repr__(self):
        return f"enums.{self}"
