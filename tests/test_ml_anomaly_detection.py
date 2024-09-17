import unittest
from ml_anomaly_detection import train_model

class TestMLAnomalyDetection(unittest.TestCase):
    def test_train_model(self):
        model = train_model('../data/log_features.csv')
        self.assertIsNotNone(model)

if __name__ == '__main__':
    unittest.main()
