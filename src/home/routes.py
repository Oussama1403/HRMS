""" App Routing """

from flask import flash,request,render_template,url_for,redirect,send_from_directory,abort,after_this_request,session
from src.models import *
from flask_login import login_user,login_required,current_user
from . import home

@home.route('/',methods=['GET'])
def base():
    return redirect(url_for('home.home'))

@home.route('/home',methods=['POST','GET'])
@login_required
def home():
    """Handle all incoming post/get requests"""
    employee_id = current_user.employee_id
    fullname = current_user.first_name + " " + current_user.last_name
    email = current_user.email
    date_of_birth = current_user.date_of_birth
    gender = current_user.gender
    phone = current_user.phone 
    dep = current_user.dep_name
    address = current_user.address
    is_admin = 'Administrator' if current_user.is_admin == True else 'Employee'
    return render_template('home/home.html',employee_id=employee_id,fullname=fullname,email=email,date_of_birth=date_of_birth,gender=gender,phone=phone,address=address,dep = dep,role=is_admin)

