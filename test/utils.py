def assert_event_handler(expected_event, mocked_handler):
    assert mocked_handler.call_count == 1
    actual_event = mocked_handler.call_args[0][0]
    assert actual_event == expected_event
