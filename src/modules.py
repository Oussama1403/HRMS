"""Main project modules"""

from flask import request,render_template,flash
from flask.wrappers import Request
from .app import app,db
from .models import *

def RegisterAccount():
    pass