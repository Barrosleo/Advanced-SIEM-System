import unittest
from log_analysis import analyze_logs

class TestLogAnalysis(unittest.TestCase):
    def test_analyze_logs(self):
        logs = ["INFO User logged in", "WARNING Disk space low", "ERROR Failed login attempt"]
        alerts = analyze_logs(logs)
        self.assertEqual(len(alerts), 2)

if __name__ == '__main__':
    unittest.main()
