"""handler"""
import json
import yaml
import sys
import urllib
import http.server
import socketserver

from src.functions.list_all import list_all


class Context:
    def __init__(self):
        self.function_name = 'asd'
        self.aws_request_id = 'asd'
        self.invoked_function_arn = 'asd'


class MockLambdaHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self, *args, **kwargs):

        self.url = urllib.parse.urlparse(self.path)

        functions = {
            '/v1/list_all': list_all
        }

        func = functions[self.url.path]

        res = func(self.make_event(), Context())

        self.send_response(res['statusCode'])
        self.send_header('Content-Type', 'application/json')
        for k, v in res['headers'].items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(res['body'].encode('utf-8'))

    def make_event(self):
        return {
            "queryStringParameters": self.get_query_string(),
            "headers": dict(self.headers.items()),
            "requestContext": {
                "authorizer": {
                    "claims": {
                        "sub": "6e7661cd-318b-462f-a9ee-78332fd47ee5",
                        "aud": "1ejfg8lluvk6cptu0u1t8pocov",
                        "event_id": "c049eb19-a01f-11e8-bf1c-9f61f6e82f32",
                        "email_verified": "true"
                    }
                }
            }
        }

    def get_query_string(self):
        if self.url.query is None or self.url.query == '':
            return {}
        return dict(map(lambda q: (q.split('=')[0], q.split('=')[1]), self.url.query.split('&')))



if __name__ == '__main__':
    http.server.HTTPServer(('', 8030), MockLambdaHandler).serve_forever()
