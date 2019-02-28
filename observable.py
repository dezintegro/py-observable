from collections import defaultdict
from collections.__init__ import UserList

from event import Event, EventType


class ObservableMixin:
    def __init__(self, *args):
        super().__init__(args)
        self._event_handlers = defaultdict(list)

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


class ObservableList(ObservableMixin, UserList):
    def append(self, item):
        super().append(item)
        self.raise_event(EventType.add, {"item": item})

    def insert(self, i, item):
        super().insert(i, item)
        self.raise_event(EventType.add, {"item": item})

    def pop(self, i=-1):
        item = super().pop(i)
        self.raise_event(EventType.delete, {"item": item})
        return item

    def remove(self, item):
        super().remove(item)
        self.raise_event(EventType.delete, {"item": item})

    def clear(self):
        prev_state = list(self.data)
        super().clear()
        self.raise_event(EventType.update, {"prev_state": prev_state})

    def extend(self, other):
        prev_state = list(self.data)
        super().extend(other)
        self.raise_event(EventType.update, {"prev_state": prev_state})
