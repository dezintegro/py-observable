from collections import defaultdict
from typing import Union

from .event import EventType, Event


class ObservableMixin:

    data: Union[list, dict]

    def __init__(self, init_arg=None, **kwds):
        self._event_handlers = defaultdict(list)
        super().__init__(init_arg, **kwds)

    def on(self, event_type: EventType, observer: callable):
        self._event_handlers[event_type].append(observer)

    def off(self, event_type: EventType, observer: callable):
        if observer in self._event_handlers[event_type]:
            self._event_handlers[event_type].remove(observer)

    def raise_event(self, event_type: EventType, payload: dict = None):
        event = Event(event_type, self, payload)
        observers = (
            *self._event_handlers[EventType.any],
            *self._event_handlers[event_type],
        )
        for observer in observers:
            observer(event)
