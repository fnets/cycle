# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 13:09:32 2015

@author: mshirley
"""

from flask import Flask

app = Flask(__name__)

from app import views
