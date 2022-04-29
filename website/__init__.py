import imp
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'HLEJ3JFKD3K+DQKLFSJ\LQSl'
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views,url_prefix='/')
    auth.register_blueprint(views,url_prefix='/')
    return app

