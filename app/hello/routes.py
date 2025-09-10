from flask import Blueprint, render_template, request, redirect, url_for
from ..models import Tarefa, User, db  # Importa a classe User do models.py

hello_bp = Blueprint('hello', __name__, url_prefix='/hello')

@hello_bp.route('/')
def index():
    usuarios = User.query.all()
    tarefas = Tarefa.query.all()
    return render_template('index.html', usuarios=usuarios, tarefas=tarefas)

@hello_bp.route('/novoUsuario', methods=['GET', 'POST'])
def novoUsuario():
    if request.method == 'POST':
        # Obtém os dados do formulário
        username = request.form['nome_usuario']
        email = request.form['email_usuario']

        # Cria uma nova instância do modelo User
        novo_usuario = User(username=username, email=email)

        # Adiciona o novo usuário à sessão do banco de dados
        db.session.add(novo_usuario)

        # Salva as mudanças no banco de dados
        db.session.commit()

        # Redireciona para a página principal após a criação
        return redirect('/hello')

    return "Método não permitido", 405

@hello_bp.route('/removerUsuario/<int:usuario_id>', methods=['POST'])
def removerUsuario(usuario_id):
    usuario = User.query.get(usuario_id)
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
    return redirect(url_for('hello.index'))

@hello_bp.route('/editarUsuario/<int:usuario_id>', methods=['GET', 'POST'])
def editarUsuario(usuario_id):
    usuario = User.query.get(usuario_id)
    if request.method == 'POST':
        # Atualiza os dados do usuário
        if usuario:
                usuario.username = request.form['nome_usuario']
                usuario.email = request.form['email_usuario']
                db.session.commit()
    return redirect(url_for('hello.index'))

@hello_bp.route('/novaTarefa', methods=['POST'])
def novaTarefa():
    if request.method == 'POST':
        descricao = request.form['descricao_tarefa']
        nova_tarefa = Tarefa(descricao=descricao)
        db.session.add(nova_tarefa)
        db.session.commit()
    return redirect(url_for('hello.index'))

@hello_bp.route('/removerTarefa/<int:tarefa_id>', methods=['POST'])
def removerTarefa(tarefa_id):
    tarefa = Tarefa.query.get(tarefa_id)
    db.session.delete(tarefa)
    db.session.commit()
    return redirect(url_for('hello.index'))

@hello_bp.route('/editarTarefa/<int:tarefa_id>', methods=['POST'])
def editarTarefa(tarefa_id):
    tarefa = Tarefa.query.get(tarefa_id)
    if request.method == 'POST':
        tarefa.descricao = request.form['descricao_tarefa']
        db.session.commit()
    return redirect(url_for('hello.index'))