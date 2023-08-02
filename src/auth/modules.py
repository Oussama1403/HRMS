from flask import request,render_template,flash,redirect,url_for
from flask_login import login_user
from src.app import db
from src.models import *
from src.home import home

def LoginAccount():
    matricule = request.form["matricule"]         
    password = request.form["password"]
    user = User.query.filter_by(matricule=matricule).first()
    if not user or user.password != password:
        flash('Please verify your information and try again.')
        return render_template('auth/login.html')
    
    login_user(user,False)
    return redirect(url_for('home.home'))

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
        flash("invalid matricule")
        return render_template("auth/register.html")
    
    # check if already registred
    row = User.query.filter_by(matricule=matricule).first()
    if row:
        flash("already registred")
        return render_template("auth/register.html")
    
    # create a new user with the form data.
    is_admin = Matricules.query.filter_by(matricule=matricule).first().is_admin
    new_user = User(matricule=matricule,first_name=first_name,last_name=last_name,email=email,password=password,phone=phone,address=address,dep_name = dep,salaire=None,is_admin = is_admin)
    db.session.add(new_user)
    db.session.commit()
    flash("Your account has been successfully created !")
    return render_template("auth/register.html")