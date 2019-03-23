import json
import unittest

from src.common import aws


class TestAws(unittest.TestCase):

    def test_response_without_body(self):

        expected = {
            'statusCode': 222,
            'headers': {},
            'body': json.dumps({
                'message': 'mylilpony',
                'code': 333
            })
        }

        res = aws.response(body=None, http_status=222, code=333, message='mylilpony')

        self.assertEqual(res, expected)

    def test_response_with_body(self):

        expected = {
            'statusCode': 222,
            'headers': {},
            'body': json.dumps({
                'message': 'mylilpony',
                'code': 333,
                'response': {
                    'pony_id': 444
                }
            })
        }

        res = aws.response(body={ 'pony_id': 444 }, http_status=222, code=333, message='mylilpony')

        self.assertEqual(res, expected)
