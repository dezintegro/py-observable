from enum import Enum


class EventType(Enum):
    any = -1
    add = 0
    delete = 1
    update = 2


class Event:
    def __init__(self, action: EventType, source: object, payload: dict = None):
        self._action = action
        self._payload = payload
        self._source = source

    @property
    def action(self):
        return self._action

    @property
    def source(self):
        return self._source

    @property
    def payload(self):
        return self._payload
