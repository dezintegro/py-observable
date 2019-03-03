import unittest
from unittest import mock

from observable.event import Event, EventType
from observable.collections import ObservableDict


def assert_event_handler(expected_event, mocked_handler):
    assert mocked_handler.call_count == 1
    actual_event = mocked_handler.call_args[0][0]
    assert actual_event.source == expected_event.source
    assert actual_event.action == expected_event.action
    assert actual_event.payload == expected_event.payload


class TestObservableDict(unittest.TestCase):
    def setUp(self):
        self.key = "foo"
        self.value = 1
        self.mocked_handler = mock.MagicMock()
        self.observable = ObservableDict({"foo": self.value, "bar": 2, "baz": 3})

    def test_init_kwargs(self):
        kwargs = {"foo": self.value, "bar": 2, "baz": 3}
        observable = ObservableDict(**kwargs)
        assert observable == kwargs

    def test_init_dict(self):
        data = {"foo": self.value, "bar": 2, "baz": 3}
        observable = ObservableDict(data)
        assert observable == data

    def test_set_item(self):
        self.observable.on(EventType.add, self.mocked_handler)
        self.observable["test"] = self.value
        expected_event = Event(
            EventType.add, self.observable, {"key": "test", "value": self.value}
        )
        assert_event_handler(expected_event, self.mocked_handler)

    def test_del_item(self):
        self.observable.on(EventType.delete, self.mocked_handler)
        del self.observable[self.key]
        expected_event = Event(EventType.delete, self.observable, {"key": self.key})
        assert_event_handler(expected_event, self.mocked_handler)

    def test_pop_item(self):
        self.observable.on(EventType.delete, self.mocked_handler)
        self.observable.pop(self.key)
        expected_event = Event(EventType.delete, self.observable, {"key": self.key})
        assert_event_handler(expected_event, self.mocked_handler)

    def test_popitem(self):
        self.observable.on(EventType.delete, self.mocked_handler)
        self.observable.popitem()
        expected_event = Event(EventType.delete, self.observable, {"key": self.key})
        assert_event_handler(expected_event, self.mocked_handler)

    def test_clear(self):
        self.observable.on(EventType.update, self.mocked_handler)
        prev_state = dict(self.observable)
        self.observable.clear()
        expected_event = Event(
            EventType.update, self.observable, {"prev_state": prev_state}
        )
        assert_event_handler(expected_event, self.mocked_handler)

    def test_extend(self):
        self.observable.on(EventType.update, self.mocked_handler)
        prev_state = dict(self.observable)
        self.observable.update({"test": 10})
        expected_event = Event(
            EventType.update, self.observable, {"prev_state": prev_state}
        )
        assert_event_handler(expected_event, self.mocked_handler)


if __name__ == "__main__":
    unittest.main()
