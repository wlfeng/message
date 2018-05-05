import json

from tornado.web import RequestHandler, StaticFileHandler


class BaseHandler(RequestHandler):
    @property
    def db(self):
        return self.application.db

    def prepare(self):
        if self.request.headers.get('Content-Type', '').startswith('application/json'):
            self.json_args = json.loads(self.request.body)
        else:
            self.json_args = {}

    def set_default_headers(self):
        self.set_header('Content-Type', 'application/json;charset=utf-8')


class StaticFileBaseHandler(StaticFileHandler):
    def __init__(self, *args, **kwargs):
        super(StaticFileHandler, self).__init__(*args, **kwargs)
        self.xsrf_token
