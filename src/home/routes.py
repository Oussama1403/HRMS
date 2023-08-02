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
    matricule = current_user.matricule
    fullname = current_user.first_name + " " + current_user.last_name
    email = current_user.email
    phone = current_user.phone 
    dep = current_user.dep_name
    address = current_user.address
    user = Matricules.query.filter_by(matricule=matricule).first()
    is_admin = 'Administrator' if user.is_admin == 1 else 'Employee'
    return render_template('home/home.html',matricule=matricule,fullname=fullname,email=email,phone=phone,address=address,dep = dep,role=is_admin)

