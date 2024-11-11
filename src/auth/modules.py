from flask import request,render_template,flash,redirect,url_for
from flask_login import login_user
from src.app import db
from src.models import *
from src.home import home
from datetime import datetime


def LoginAccount():
    employee_id = request.form["employee_id"]         
    password = request.form["password"]
    user = User.query.filter_by(employee_id=employee_id).first()
    if not user or user.password != password:
        flash('Please verify your information and try again.')
        return render_template('auth/login.html')
    
    login_user(user,False)
    return redirect(url_for('home.home'))

def RegisterAccount():
    employee_id = request.form["employee_id"]
    first_name = request.form["inputFirstName"]
    last_name = request.form["inputLastName"]
    gender = request.form["inputGender"]
    date_of_birth_str = request.form["inputDOB"]
    date_of_birth = datetime.strptime(date_of_birth_str, '%Y-%m-%d').date()  # convert to python date object
    email = request.form["inputEmail"]
    password = request.form["inputPassword"]
    address = request.form["address"]
    dep = request.form["dep"]
    is_admin = request.form["is_admin"]
    phone = request.form["phone"]    

    # check if already registred
    row = User.query.filter_by(employee_id=employee_id).first()
    if row:
        flash("already registred")
        return render_template("auth/register.html")
    
    # create a new user with the form data.
    new_user = User(employee_id=employee_id,first_name=first_name,last_name=last_name,gender=gender,date_of_birth=date_of_birth,email=email,password=password,phone=phone,address=address,dep_name = dep,salaire=None,is_admin = True if "Yes" in is_admin else False)
    db.session.add(new_user)
    db.session.commit()
    flash("Your account has been successfully created !")
    return render_template("auth/register.html")