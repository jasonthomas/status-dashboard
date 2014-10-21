import redis
import time
from flask import request
from flask.ext.restful import Resource


class Service(Resource):
    def __init__(self, host='localhost'):
        self.conn = redis.Redis(host)
        self.keyprefix = '/services/'

    def add_service(self, key, name, description=None, url=None):
        service_key = '{0}{1}'.format(self.keyprefix, key)
        if self.get_service(key):
            return {"success": False, "reason": "Service already exists"}
        else:
            self.conn.hset(service_key, 'name', name)
            self.conn.hset(service_key, 'description', description)
            self.conn.hset(service_key, 'url', url)
            self.conn.hset(service_key, 'state', 'green')
            self.conn.hset(service_key, 'latest_event', None)
            self.conn.hset(service_key, 'latest_incident', None)
            self.conn.hset(service_key, 'last_updated', int(time.time()))

            return {"success": True, "resource": service_key}

    def get_service(self, key):
        service_key = '{0}{1}'.format(self.keyprefix, key)
        return self.conn.hgetall(service_key)

    def delete_service(self, key):
        service_key = '{0}{1}'.format(self.keyprefix, key)
        if self.conn.delete(service_key):
            return {"success": True}
        else:
            return {"success": False}

    def get(self, key):
        return self.get_service(key)

    def post(self):
        data = request.get_json()
        try:
            result = self.add_service(data['key'], data['name'],
                                      data['description'], data['url'])
            return result
        except:
            return {"success": "false"}

    def delete(self, key):
        result = self.delete_service(key)
        return result


class ServiceList(Resource):
    def __init__(self, host='localhost'):
        self.conn = redis.Redis(host)
        self.keyprefix = '/services/'

    def get(self):
        return self.conn.keys('{0}*'.format(self.keyprefix))
