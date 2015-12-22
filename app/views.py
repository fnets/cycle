# -*- coding: utf-8 -*-
from flask import render_template
from app import app
from util import get_entry
from config import app_name

@app.route('/')
@app.route('/index')
def index():
    entry = get_entry()
    return render_template('index.html', title=app_name, entry=entry)