"""list_all module contains the top level function
to be called by aws for the list photos endpoint"""

from src.common import aws

def list_all(event, context):
    """list_all"""

    return aws.response({}, 200, 1001, 'Complete')
