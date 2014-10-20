from flask import Flask

from flask.ext.restful import Resource, Api

from service import Service

app = Flask(__name__)
api = Api(app)


api.add_resource(Service, '/api/v0.1/service')

if __name__ == "__main__":
    app.run(debug=True)
