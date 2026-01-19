from flask import Flask
from flask_restx import Api

from app.api.v1.places import api as places_ns
from app.api.v1.users import api as users_ns
from app.api.v1.amenities import api as amenities_ns


def create_app(config_class="config.DevelopmentConfig"): #update to receive a configuration
    app = Flask(__name__)
    app.config.from_object(config_class)

----------------------
    from yourapplication.model import db
    db.init_app(app)

    from yourapplication.views.admin import admin
    from yourapplication.views.frontend import frontend
    app.register_blueprint(admin)
    app.register_blueprint(frontend)
-----------------------
    
    api = Api(
        app,
        version='1.0',
        title='HBnB API',
        description='HBnB Application API',
        doc='/api/v1/'
    )

    # Register namespaces
    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(places_ns, path='/api/v1/places')
    api.add_namespace(amenities_ns, path='/api/v1/amenities')

    return app
