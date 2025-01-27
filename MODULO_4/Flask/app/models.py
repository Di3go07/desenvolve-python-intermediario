""" Este arquivo contém os modelos do banco de dados SQL escritos em Python como classes """

from datetime import datetime, timezone
from hashlib import md5
from time import time
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from sqlalchemy import func, select
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from app import app, db, login


#cria a tabela de assossiação dos seguidores
followers = sa.Table(
    'followers',
    db.metadata,
    sa.Column('follower_id', sa.Integer, sa.ForeignKey('user.id'),
              primary_key=True),
    sa.Column('followed_id', sa.Integer, sa.ForeignKey('user.id'),
              primary_key=True)
)

class User(UserMixin, db.Model):                                               #cria a tabela do database
    id = db.Column(db.Integer, primary_key=True)                             #o field representa uma coluna dessa tabela 
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    posts = db.relationship('Post', backref='author', lazy='dynamic')      #se refere à sua relação com a classe post
    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def set_password(self, password):                                          #função que adiciona uma senha criptografa
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):                                        #função que verifica se as senhas batem
        return check_password_hash(self.password_hash, password)
    
    def avatar(self, size):                                                        #função que adiciona um avatar ao perfil
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()       #essa biblioteca permite cada email ter seu próprio avatar
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)
    
    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)
    
    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user):
        return self.followed.filter(followers.c.followed_id == user.id).count() > 0

    def followed_posts(self):
        followed = Post.query.join(followers, (followers.c.followed_id == Post.user_id)).filter(followers.c.follower_id == self.id)
        #retorna os posts apenas dos seguindo
        own = Post.query.filter_by(user_id=self.id)
        #retorna seus próprios posts
        total_posts = followed.union(own).order_by(Post.timestamp.desc())
        return total_posts
    
    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
        {'reset_password': self.id, 'exp': time() + expires_in},
        app.config['SECRET_KEY'], algorithm='HS256').encode('utf-8')
    
    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)

@login.user_loader                                                                #mantem o usuário logado no site
def load_user(id):
    return User.query.get(int(id))

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.now(timezone.utc))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #refere-se a sua foreing key em User 

    def __repr__(self):
        return '<Post {}>'.format(self.body)
    
