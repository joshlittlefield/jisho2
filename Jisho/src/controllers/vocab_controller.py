from models.Vocab import Vocab
from models.Kanji import Kanji
from models.User import User
from main import db
from schemas.KanjiSchema import kanji_schema, kanjis_schema
from schemas.VocabSchema import vocab_schema, vocabs_schema
from flask import Blueprint, request, jsonify, abort, render_template, url_for, flash , redirect
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.auth_service import verify_user
from sqlalchemy.orm import joinedload
from forms import RegistrationForm, LoginForm, PostForm
from flask_login import login_user, current_user, logout_user, login_required


vocabs = Blueprint('vocabs', __name__)


@vocabs.route("/vocab")
@login_required
def vocab():
    # Retrieve all kanji
    vocabs = Vocab.query.all()
    return render_template("single_vocab_level.html", vocabs=vocabs)
    
    
    
@vocabs.route("/vocab/<int:vocab_id>")
@login_required
def single_vocab(vocab_id):
    vocabs = Vocab.query.get_or_404(vocab_id)
    return render_template('single_vocab_level.html', vocabs=vocabs)
    

@vocabs.route("/vocab/<int:single_heisig_level>")
@login_required
def single_vocab_level(single_heisig_level):
    
    kanjis = Kanji.query.filter_by(heisig_level=single_heisig_level).all()
    return render_template('single_vocab_level.html', single_heisig_level=single_heisig_level, vocabs=vocabs)
    
    

    
@vocabs.route("/sentence/<int:single_heisig_level>")
@login_required
def single_sentence_level(single_heisig_level):
    
    kanjis = Kanji.query.filter_by(heisig_level=single_heisig_level).all()
    return render_template('single_sentence_level.html', single_heisig_level=single_heisig_level, vocabs=vocabs)
    