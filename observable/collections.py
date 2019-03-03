from collections import UserDict, UserList

from observable.event import EventType
from observable.mixins import ObservableMixin


class ObservableList(ObservableMixin, UserList):
    def __setitem__(self, i, item):
        super().__setitem__(i, item)
        self.raise_event(EventType.update, {"item": item})

    def __delitem__(self, i):
        item = self.data[i]
        super().__delitem__(i)
        self.raise_event(EventType.delete, {"item": item})

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


class ObservableDict(ObservableMixin, UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.raise_event(EventType.add, {"key": key, "value": value})

    def __delitem__(self, key):
        super().__delitem__(key)
        self.raise_event(EventType.delete, {"key": key})

    def clear(self):
        prev_state = dict(self.data)
        super().clear()
        self.raise_event(EventType.update, {"prev_state": prev_state})

    def update(self, *args, **kwds):
        prev_state = dict(self.data)
        super().update(*args, **kwds)
        self.raise_event(EventType.update, {"prev_state": prev_state})
