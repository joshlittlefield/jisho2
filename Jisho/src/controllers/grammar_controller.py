from models.Grammar import Grammar
from models.User import User
from main import db
from schemas.GrammarSchema import grammar_schema, grammars_schema
from flask import Blueprint, request, jsonify, abort, render_template, url_for, flash , redirect
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.auth_service import verify_user
from sqlalchemy.orm import joinedload
from forms import RegistrationForm, LoginForm, PostForm
from flask_login import login_user, current_user, logout_user, login_required


grammars = Blueprint('grammars', __name__)



    
@grammars.route("/grammar/<int:single_grammar_level>")
@login_required
def single_grammar_level(single_grammar_level):
   
    grammars = Grammar.query.filter_by(grammar_level=single_grammar_level).all()
    return render_template('single_grammar_level.html', single_grammar_level=single_grammar_level, grammars=grammars)
    

    