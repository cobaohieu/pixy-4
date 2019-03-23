"""aws contains helpful functions for pre and post processing
data inside aws lambda"""

import json


def response(body=None, http_status=200, code=2001, message=''):
    """response takes in data and returns an aws lambda friendly
    object that lambda will read and convert to the http response"""

    output = {
        'statusCode': http_status,
        'headers': {},
        'body': {
            'message': message,
            'code': code
        }
    }

    if body is not None:
        output['body']['response'] = body

    output['body'] = json.dumps(output['body'])

    return output
