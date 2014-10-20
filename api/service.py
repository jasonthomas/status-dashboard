import redis
from flask import request
from flask.ext.restful import Resource


class Service(Resource):
    def __init__(self, host='localhost'):
        self.conn = redis.Redis(host)

    def add_service(self, key, name, description=None, url=None):
        service_key = '/services/%s' % key
        self.conn.hset(service_key, 'name', name)
        self.conn.hset(service_key, 'description', description)
        self.conn.hset(service_key, 'url', url)
        return service_key

    def post(self):
        data = request.get_json()
        try:
            service_key = self.add_service(data['key'], data['name'],
                                           data['description'], data['url'])
            return {"success": "true", "resource": service_key}
        except:
            return {"success": "false"}
