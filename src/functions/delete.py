"""delete module contains the top level function
to be called by aws for the delete photos endpoint"""

from src.common import aws

def delete(event, context):
    """list_all"""

    return aws.response({}, 200, 1001, 'Complete')
