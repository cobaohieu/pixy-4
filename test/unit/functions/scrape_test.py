import json
import unittest

from src.functions.list_all import list_all


class TestListAll(unittest.TestCase):

    def test_list_all(self):

        res = list_all(None, None)

        self.assertEqual(res['statusCode'], 200)
