import unittest
from unittest import mock

from observable.event import Event, EventType
from observable.collections import ObservableList


def assert_event_handler(expected_event, mocked_handler):
    assert mocked_handler.call_count == 1
    actual_event = mocked_handler.call_args[0][0]
    assert actual_event.source == expected_event.source
    assert actual_event.action == expected_event.action
    assert actual_event.payload == expected_event.payload


class TestObservableList(unittest.TestCase):
    def setUp(self):
        self.item = 10
        self.mocked_handler = mock.MagicMock()
        self.observable = ObservableList([1, 2, 3, 10])

    def test_init_list(self):
        data = [1, 2, 3]
        observable = ObservableList(data)
        assert observable == data

    def test_set_item(self):
        self.observable.on(EventType.update, self.mocked_handler)
        self.observable[1] = self.item
        expected_event = Event(EventType.update, self.observable, {"item": self.item})
        assert_event_handler(expected_event, self.mocked_handler)

    def test_del_item(self):
        self.observable.on(EventType.delete, self.mocked_handler)
        del self.observable[-1]
        expected_event = Event(EventType.delete, self.observable, {"item": self.item})
        assert_event_handler(expected_event, self.mocked_handler)

    def test_append_item(self):
        self.observable.on(EventType.add, self.mocked_handler)
        self.observable.append(self.item)
        expected_event = Event(EventType.add, self.observable, {"item": self.item})
        assert_event_handler(expected_event, self.mocked_handler)

    def test_insert_item(self):
        self.observable.on(EventType.add, self.mocked_handler)
        self.observable.insert(0, self.item)
        expected_event = Event(EventType.add, self.observable, {"item": self.item})
        assert_event_handler(expected_event, self.mocked_handler)

    def test_pop_item(self):
        self.observable.on(EventType.delete, self.mocked_handler)
        self.observable.pop()
        expected_event = Event(EventType.delete, self.observable, {"item": self.item})
        assert_event_handler(expected_event, self.mocked_handler)

    def test_remove_item(self):
        self.observable.on(EventType.delete, self.mocked_handler)
        self.observable.remove(self.item)
        expected_event = Event(EventType.delete, self.observable, {"item": self.item})
        assert_event_handler(expected_event, self.mocked_handler)

    def test_clear(self):
        self.observable.on(EventType.update, self.mocked_handler)
        prev_state = list(self.observable)
        self.observable.clear()
        expected_event = Event(
            EventType.update, self.observable, {"prev_state": prev_state}
        )
        assert_event_handler(expected_event, self.mocked_handler)

    def test_extend(self):
        self.observable.on(EventType.update, self.mocked_handler)
        prev_state = list(self.observable)
        self.observable.extend([1, 2, 3])
        expected_event = Event(
            EventType.update, self.observable, {"prev_state": prev_state}
        )
        assert_event_handler(expected_event, self.mocked_handler)


if __name__ == "__main__":
    unittest.main()
