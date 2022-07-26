# This is useful for n number of keys inside the object
import unittest
from keyObject import *

obj = {"p": {"q": {"r": {"s": "k"}}}}
key = "p/q/r/s"


class TestKeyObject(unittest.TestCase):
    def test_cal_success(self):
        self.assertEqual(cal(obj, key), 'k')

    def test_cal_fail(self):
        self.assertNotEqual(cal(obj, key), 'm')
