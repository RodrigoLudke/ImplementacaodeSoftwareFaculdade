# run.py
from app import create_app
# Cria a aplicação chamando a factory
app = create_app()
if __name__ == '__main__':
# Executa o servidor de desenvolvimento do Flask
# debug=True ativa o modo de depuração para reiniciar o servidor a cada alteração
    app.run(debug=True)
