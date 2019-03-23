"""find module contains the top level function
to be called by aws for the find photos endpoint"""

from src.common import aws

def find(event, context):
    """list_all"""

    return aws.response({}, 200, 1001, 'Complete')
