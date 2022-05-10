from models.Jisho import Jisho
from models.User import User
from main import db
from schemas.JishoSchema import jisho_schema, jishos_schema
from flask import Blueprint, request, jsonify, abort, render_template, url_for, flash , redirect
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.auth_service import verify_user
from sqlalchemy.orm import joinedload
from forms import RegistrationForm, LoginForm, PostForm
from flask_login import login_user, current_user, logout_user, login_required


jishos = Blueprint('jishos', __name__)

@jishos.route("/")
@jishos.route("/home")
def home():
    # Retrieve all jishos
    jishos = Jisho.query.options(joinedload("user")).all()
    return render_template("home.html", jishos=jishos)
    
    

@jishos.route("/dashboard")
def dashboard():
    # Retrieve all jishos
    jishos = Jisho.query.options(joinedload("user")).all()
    return render_template("dashboard.html", jishos=jishos)
    
@jishos.route("/about")
def about():
    # Retrieve all jishos
    jishos = Jisho.query.options(joinedload("user")).all()
    return render_template("about.html", jishos=jishos)
    
@jishos.route("/help")
def help():
    # Retrieve all jishos
    jishos = Jisho.query.options(joinedload("user")).all()
    return render_template("help.html", jishos=jishos)


@jishos.route("/otakubb")
@login_required
def otakubb():
    # Retrieve all jishos
    jishos = Jisho.query.options(joinedload("user")).all()
    return render_template("otakubb.html", jishos=jishos)




@jishos.route("/jisho/new", methods=['GET', 'POST'])
@login_required
def new_jisho():
    form = PostForm()
    if form.validate_on_submit():
        jisho = Jisho(title=form.title.data, content=form.content.data, user=current_user)
        db.session.add(jisho)
        db.session.commit()
        flash('Your Jisho has been created!', 'success')
        return redirect(url_for('jishos.home'))
    return render_template('create_jisho.html', title='New Jisho', form=form, legend='New Jisho')


@jishos.route("/jisho/<int:jisho_id>")
def jisho(jisho_id):
    jisho = Jisho.query.get_or_404(jisho_id)
    return render_template('jisho.html', title=jisho.title, jisho=jisho)


@jishos.route("/jisho/<int:jisho_id>/update", methods=['GET', 'POST'])
@login_required
def update_jisho(jisho_id):
    jisho = Jisho.query.get_or_404(jisho_id)
    if jisho.user != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        jisho.title = form.title.data
        jisho.content = form.content.data
        db.session.commit()
        flash('Your jisho has been updated!', 'success')
        return redirect(url_for('jishos.jisho', jisho_id=jisho.id))
    elif request.method == 'GET':
        form.title.data = jisho.title
        form.content.data = jisho.content
    return render_template('create_jisho.html', title='Update Jisho', form=form, legend='Update Jisho')


@jishos.route("/jisho/<int:jisho_id>/delete", methods=['POST'])
@login_required
def delete_jisho(jisho_id):
    jisho = Jisho.query.get_or_404(jisho_id)
    if jisho.user != current_user:
        abort(403)
    db.session.delete(jisho)
    db.session.commit()
    flash('Your jisho has been deleted!', 'success')
    return redirect(url_for('jishos.home'))

