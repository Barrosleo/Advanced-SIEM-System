import unittest
from log_collection import collect_logs

class TestLogCollection(unittest.TestCase):
    def test_collect_logs(self):
        logs = collect_logs('../data/logs')
        self.assertGreater(len(logs), 0)

if __name__ == '__main__':
    unittest.main()
