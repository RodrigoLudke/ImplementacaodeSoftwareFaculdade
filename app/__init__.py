# app/__init__.py
from flask import Flask
from .hello.routes import hello_bp # Importa o blueprint que criamos
def create_app():
# Cria a instância da aplicação Flask
    app = Flask(__name__)
# Registra o blueprint na aplicação
    app.register_blueprint(hello_bp)
# Retorna a aplicação configurada
    return app
