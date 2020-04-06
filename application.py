from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from resources.store import Store, StoreList
from resources.user import UserRegister
from resources.item import Item, ItemList
from security import authenticate, identity

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.secret_key = 'rishav'
api = Api(application)

@application.before_first_request
def create_table():
    db.create_all()

jwt = JWT(application, authenticate, identity) #/auth

api.add_resource(Store,'/store/<string:name>')
api.add_resource(Item, '/item/<string:name>') #http://127.0.1.1:4999/student/Rolf
api.add_resource(ItemList, '/items')
api.add_resource(StoreList,'/stores')

api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(application)
    application.run(port=4999, debug=True)
