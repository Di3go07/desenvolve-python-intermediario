"""O arquivo __init__.py é usado para definir o que será executado quando o pacote for importado. Ele é muito útil caaso você queira fazer alguma inicialização ou configuração, como importações e variáveis, antes que os outros módulos no pacote sejam importados. """

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from logging.handlers import RotatingFileHandler
import os
import logging
from flask_mail import Mail
from flask_bootstrap import Bootstrap

app = Flask(__name__)
#estabelece a instância  Flask raiz de todos o projeto

app.config.from_object(Config)
#le as variáveis de configurações e aplica ao programa

db = SQLAlchemy(app)
migrate = Migrate(app, db)
#cria variáveis para o database e para suas migrattions 

login = LoginManager(app)
login.login_view = 'login'
#cria a variável da classe para fazer login

mail = Mail(app)

if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')
#cria um arquivo com os erros registrados 

bootstrap = Bootstrap(app)
#inicializa o Bootstrap

from app import routes, models, erros
# importa esse módulos de 'app' para registrá-las na aplicação