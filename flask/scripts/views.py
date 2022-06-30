from flask import render_template, request, redirect,session,flash,url_for
from models import games,users
from app import db, app

@app.route('/create', methods = ['POST',])
def create():
    name     = request.form['name']
    category = request.form['category']
    console  = request.form['console']
    
    game = games.query.filter_by(name = name).first()

    if game:
        return redirect(url_for('index'))

    new_game = games(name = name,category = category, console = console) 
    db.session.add(new_game)
    db.session.commit()

    return redirect(url_for('index'))
    

@app.route('/games')
def index():
    lista = games.query.order_by(games.id)
    return render_template('lista.html', titulo='Jogos',jogos = lista)

@app.route('/new')
def novo():
    if 'logged_user' not in session or session['logged_user'] == None:
        return redirect(url_for('login', next = url_for('novo')))
    return render_template('novo.html',titulo = 'Novo Jogo')

@app.route('/login')
def login():
    next = request.args.get('next')
    return render_template('login.html',next=next)

@app.route('/logout')
def logout():
    session['logged_user'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))


@app.route('/auth', methods=["POST",])
def auth():
    user = users.query.filter_by(id = request.form['user']).first()
    if user and (request.form['password'] == user.password):
        
        session['logged_user'] = user.id
        flash(user.id + ' logou com sussesso!')
        next_page = request.form['next']
        return redirect(next_page)
    else:
        flash('Usuário não logado')
        return redirect(url_for('login'))  




@app.route('/edit/<int:id>')
def edit(id):
    if 'logged_user' not in session or session['logged_user'] == None:
        return redirect(url_for('login', next = url_for('novo')))

    game = games.query.filter_by(id=id).first()    
    return render_template('edit.html',titulo='Update game',game = game)


@app.route('/update', methods=['POST',])
def update():
    jogo = games.query.filter_by(id=request.form['id']).first()
    jogo.name = request.form['nome']
    jogo.category = request.form['categoria']
    jogo.console = request.form['console']

    db.session.add(jogo)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/delete/<int:id>')
def delete(id):
    if 'logged_user' not in session or session['logged_user'] == None:
        return redirect(url_for('login', next = url_for('novo')))

    games.query.filter_by(id=id).delete()
    db.session.commit()
    flash("Jogo deletado")

    return redirect(url_for('index'))
