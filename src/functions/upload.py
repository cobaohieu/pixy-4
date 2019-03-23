"""upload module contains the top level function
to be called by aws for the upload photos endpoint"""

from cgi import parse_header, parse_multipart
from io import BytesIO

import boto3

from src.common import aws


def upload(event, context):
    """list_all"""

    bucket = boto3.resource('s3').Bucket('pixy-photos')

    c_type, c_data = parse_header(event['headers']['Content-Type'])
    assert c_type == 'multipart/form-data'
    img = parse_multipart(BytesIO(event['body'].decode('base64')), c_data)

    with open('/tmp/output', 'wb') as data:
        data.write(img)
        bucket.upload_file('/tmp/output', key)

    return aws.response({}, 200, 1001, 'Complete')
