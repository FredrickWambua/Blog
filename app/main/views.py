import os
from flask import render_template,redirect,url_for,abort,request,flash
from app.models import User, Blog, Comment
from .forms import UpdateProfile, CreateBlog
from .. import main
from app.requests import get_quotes
from flask_login import login_required,current_user
from ..email import mail_message
import secrets
from .. import db
from PIL import Image


@main.route('/')
def index():
    quotes = get_quotes()
    page = request.args.get('page',1, type = int )
    blogs = Blog.query.order_by(Blog.posted.desc()).paginate(page = page, per_page = 3)
    return render_template('index.html', quote = quotes,blogs=blogs)