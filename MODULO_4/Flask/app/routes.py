"""Este arquivo dita qual lógica executar quando o cliente passa algum endpoint da URL"""

from app import app                                                        #importa a instância app do Flask do módulo app
from flask import render_template, flash, redirect,  url_for
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import User
from flask_login import logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse
from app import db
from app.forms import RegistrationForm
from datetime import datetime, timezone
from app.forms import EditProfileForm
from app.forms import EmptyForm
from app.forms import PostForm
from app.models import Post
from app.forms import ResetPasswordRequestForm
from app.email import send_password_reset_email
from app.forms import ResetPasswordForm

@app.before_request                                                   #função ativada toda vez que uma URL é chamada
def before_request():
    if current_user.is_authenticated:                                #atualiza o last_seen do usuário
        current_user.last_seen = datetime.now(timezone.utc)
        db.session.commit()

@app.route('/',  methods=['GET', 'POST'])
@app.route('/index',  methods=['GET', 'POST'])
@login_required                 #função que exige um login antes de acessar a página                                                                         
def index():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.post.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('index'))
    
    page = request.args.get('page', 1, type=int)
    posts = current_user.followed_posts().paginate(
        page=page, 
        per_page=app.config['POSTS_PER_PAGE'], 
        error_out=False
    )
    next_url = url_for('index', page=posts.next_num) \
    if posts.has_next else None
    prev_url = url_for('index', page=posts.prev_num) \
    if posts.has_prev else None

    return render_template('index.html', title='Home', form=form, posts=posts.items, next_url=next_url, prev_url=prev_url)  
    #passa o arquivo do template e seus argumentos

#a função decorada dita que esses endpoints passados acionam esta função index()

@app.route('/login', methods=['GET', 'POST']) #metodos HTTP que a url suporta enviar
def login():
    if current_user.is_authenticated:                                               #verifica se o user ja esta registrado ao entrar na pagina de login
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()      #verifica se o nome de usuário existe no banco
        if user is None or not user.check_password(form.password.data):        #verifica se a senha é a mesma
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':                    #processa o que será feito após o @login_required
            next_page = url_for('index')
        return redirect(url_for('index'))                                            #caso esteja tudo correto, direciona para home
    return render_template('login.html', title='Sign In', form=form)           

@app.route('/logout')                                                                 #permite o usuário se desconectar 
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])                               #cria um usuario no banco de dados
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))                                           #redireciona à página de login após registro
    return render_template('register.html', title='Register', form=form)

@app.route('/user/<username>')                                                    #link para um perfil
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    
    page = request.args.get('page', 1, type=int)
    posts = user.posts.order_by(Post.timestamp.desc()).paginate(page=page, per_page=app.config['POSTS_PER_PAGE'], error_out=False)
    next_url = url_for('user', username=user.username, page=posts.next_num) \
    if posts.has_next else None
    prev_url = url_for('user', username=user.username, page=posts.prev_num) \
    if posts.has_prev else None

    form = EmptyForm()    #botao de Follow e Unfollow                                                          

    return render_template('user.html', title=user.username, user=user, posts=posts.items, next_url=next_url, prev_url=prev_url, form=form)

@app.route('/edit_profile', methods=['GET', 'POST'])                            #alterar informações do perfil
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():                                                    #se o formulario for validado
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('index'))
    elif request.method == 'GET':                                                    #popula os campos com informações do banco
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile',form=form)

#FOLLOW E UNFOLLOW 
@app.route('/follow/<username>', methods=['POST'])
@login_required
def follow(username):
    form = EmptyForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first()
        if user is None:
            flash('User {} not found.'.format(username))
            return redirect(url_for('index'))
        if user == current_user:
            flash('You cannot follow yourself!')
            return redirect(url_for('user', username=username))
        current_user.follow(user)
        db.session.commit()
        flash('You are now following {}!'.format(username))
        return redirect(url_for('user', username=username))
    else:
        return redirect(url_for('index'))
    
@app.route('/unfollow/<username>', methods=['POST'])
@login_required
def unfollow(username):
    form = EmptyForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first()
        if user is None:
            flash('User {} not found.'.format(username))
            return redirect(url_for('index'))
        if user == current_user:
            flash('You cannot unfollow yourself!')
            return redirect(url_for('user', username=username))
        current_user.unfollow(user)
        db.session.commit()
        flash('You are not following {}.'.format(username))
        return redirect(url_for('user', username=username))
    else:
        return redirect(url_for('index'))
    
@app.route('/explore')
@login_required
def explore():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
        page=page, 
        per_page=app.config['POSTS_PER_PAGE'], 
        error_out=False
    )
    
    next_url = url_for('explore', page=posts.next_num) \
    if posts.has_next else None
    prev_url = url_for('explore', page=posts.prev_num) \
    if posts.has_prev else None
    return render_template("index.html", title='Explore', posts=posts.items,next_url=next_url, prev_url=prev_url)

@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('Check your email for the instructions to reset your password')
        return redirect(url_for('login'))
    return render_template('reset_password_request.html', title='Reset Password', form=form)

@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('login'))
    return render_template('reset_password.html', form=form)