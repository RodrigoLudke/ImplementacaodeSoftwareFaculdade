from flask import Flask
from .hello.routes import hello_bp
from .models import db  # Importa a instância 'db' do models.py

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    db.init_app(app)
    
    with app.app_context():
        db.create_all()

    app.register_blueprint(hello_bp, url_prefix='/hello')

    return app