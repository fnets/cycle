# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 13:12:14 2015

@author: mshirley
"""
from flask import render_template
from app import app
from util import get_entry

@app.route('/')
@app.route('/index')
def index():
    entry = get_entry()
    return render_template('index.html', title='Home', entry=entry)