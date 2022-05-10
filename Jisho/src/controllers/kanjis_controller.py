from models.Kanji import Kanji
from models.User import User
from main import db
from schemas.KanjiSchema import kanji_schema, kanjis_schema
from flask import Blueprint, request, jsonify, abort, render_template, url_for, flash , redirect
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.auth_service import verify_user
from sqlalchemy.orm import joinedload
from forms import RegistrationForm, LoginForm, PostForm
from flask_login import login_user, current_user, logout_user, login_required


kanjis = Blueprint('kanjis', __name__)


@kanjis.route("/kanji")
@login_required
def kanji():
    # Retrieve all kanji
    kanjis = Kanji.query.all()
    return render_template("kanji.html", kanjis=kanjis)
    
    
    
@kanjis.route("/kanji/<int:kanji_id>")
@login_required
def single_kanji(kanji_id):
    kanjis = Kanji.query.get_or_404(kanji_id)
    return render_template('single_kanji.html', kanjis=kanjis)
    

@kanjis.route("/heisig_level/<int:single_heisig_level>")
@login_required
def single_heisig_level(single_heisig_level):
    
    kanjis = Kanji.query.filter_by(heisig_level=single_heisig_level).all()
    return render_template('single_heisig_level.html', single_heisig_level=single_heisig_level, kanjis=kanjis)
    
    
@kanjis.route("/vocab/<int:single_heisig_level>")
@login_required
def single_vocab_level(single_heisig_level):
   
    kanjis = Kanji.query.filter_by(heisig_level=single_heisig_level).all()
    return render_template('single_vocab_level.html', single_heisig_level=single_heisig_level, kanjis=kanjis)
    
@kanjis.route("/sentence/<int:single_heisig_level>")
@login_required
def single_sentence_level(single_heisig_level):
    
    kanjis = Kanji.query.filter_by(heisig_level=single_heisig_level).all()
    return render_template('single_sentence_level.html', single_heisig_level=single_heisig_level, kanjis=kanjis)
    