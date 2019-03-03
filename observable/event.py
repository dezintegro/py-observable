from enum import Enum
from collections import namedtuple


class EventType(Enum):
    any = -1
    add = 0
    delete = 1
    update = 2


Event = namedtuple('Event', ['action', 'source', 'payload'])
