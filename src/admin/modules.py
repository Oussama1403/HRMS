from flask import flash
from flask.wrappers import Request
from flask_login import current_user
from src.app import app,db
from src.models import *

def AdminOnly():
    matricule = current_user.matricule
    user = Matricules.query.filter_by(matricule=matricule).first()
    if user.is_admin == 0:
        flash("Accès administratif uniquement")
    return True if user.is_admin == 1 else False

def fullname_role():
    fullname = current_user.first_name + " " + current_user.last_name
    user = Matricules.query.filter_by(matricule=current_user.matricule).first()
    is_admin = 'Administrateur' if user.is_admin == 1 else 'Employé'
    return (fullname,is_admin)