import unittest
from unittest import mock

from event import Event, EventType
from observable import ObservableList


class TestObservable(unittest.TestCase):
    def test_add_event(self):
        item = 1
        mocked_handler = mock.MagicMock()
        observable = ObservableList(2, 3)
        observable.on(EventType.add, mocked_handler)
        observable.append(item)
        expected_event = Event(EventType.add, observable, {"item": item})
        actual_event = mocked_handler.call_args[0][0]
        assert actual_event.source == expected_event.source
        assert actual_event.action == expected_event.action
        assert actual_event.payload == expected_event.payload


if __name__ == "__main__":
    unittest.main()
