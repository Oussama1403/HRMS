"""Main project modules"""

from flask import request,render_template,flash,redirect,url_for
from flask.wrappers import Request
from flask_login import login_user,login_required,current_user
from .app import app,db
from .models import *

def LoginAccount():
    matricule = request.form["matricule"]         
    password = request.form["password"]
    user = User.query.filter_by(matricule=matricule).first()
    if not user or user.password != password:
        flash('Veuillez vérifier vos informations et réessayer.')
        return render_template('login.html')
    
    login_user(user,False)
    return redirect(url_for('home'))

def RegisterAccount():
    matricule = request.form["matricule"]         
    first_name = request.form["inputFirstName"]
    last_name = request.form["inputLastName"]
    email = request.form["inputEmail"]
    password = request.form["inputPassword"]
    address = request.form["address"]
    dep = request.form["dep"]
    phone = request.form["phone"]
    # check for valid matricule
    row = Matricules.query.filter_by(matricule=matricule).first()
    if not row:
        flash("matricule invalid")
        return render_template("register.html")
    
    # check if already registred
    row = User.query.filter_by(matricule=matricule).first()
    if row:
        flash("already registred")
        return render_template("register.html")
    
    # create a new user with the form data.
    new_user = User(matricule=matricule,first_name=first_name,last_name=last_name,email=email,password=password,phone=phone,address=address,dep_name = dep,salaire=None)
    db.session.add(new_user)
    db.session.commit()
    flash("Your account has been successfully created !")
    return render_template("register.html")

def fullname_role():
    fullname = current_user.first_name + " " + current_user.last_name
    user = Matricules.query.filter_by(matricule=current_user.matricule).first()
    is_admin = 'Administrateur' if user.is_admin == 1 else 'Employé'
    return (fullname,is_admin)