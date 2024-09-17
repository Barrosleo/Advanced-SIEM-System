import unittest
from event_response import respond_to_events

class TestEventResponse(unittest.TestCase):
    def test_respond_to_events(self):
        alerts = ["ERROR Failed login attempt"]
        respond_to_events(alerts, '../models/anomaly_detector.pkl')
        # This test is more of an integration test and would need a real environment to fully validate

if __name__ == '__main__':
    unittest.main()
