"""Este é o arquivo toplevel que define a instância da aplicação Flask, necessário para que o framework saiba como encontrar e executar a aplicação corretamente"""

from app import app, db
from app.models import User, Post
#ao importar, ele automaticamente realiza toda o código presente no __init__.py  

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
#fornece um contexto ao shell para referenciar objetos da aplicação python