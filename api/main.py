from flask import Flask
from flask.ext.restful import Api
from resources.service import Service, ServiceList

prefix = '/api/v0.1'
app = Flask(__name__)
api = Api(app, prefix=prefix)

api.add_resource(Service,
                 '/services',
                 '/services/<string:key>'
                 )
api.add_resource(ServiceList,
                 '/services/list'
                 )

if __name__ == "__main__":
    app.run(debug=True)
