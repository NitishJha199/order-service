import unittest
from app import process_order

class TestOrderService(unittest.TestCase):
    def test_process_order_success(self):
        res = process_order("ORD-101", 49.99)
        self.assertEqual(res["status"], "CONFIRMED")

if __name__ == '__main__':
    unittest.main()
