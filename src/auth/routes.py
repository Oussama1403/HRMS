from flask import flash,request,render_template,url_for,redirect,send_from_directory,abort,after_this_request,session
from flask_login import login_user,logout_user,login_required,current_user


from .modules import *
from . import auth

@auth.route("/login",methods=['POST','GET'])
def login():
    if request.method == 'POST':
        response = LoginAccount()
        return response
    else:
        return render_template('auth/login.html')    

@auth.route("/register",methods=['POST','GET'])
def register():
    # TODO:FORM VALIDATION
    if request.method == 'POST':
        response = RegisterAccount()
        return response
    else:
        return render_template('auth/register.html')     

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route("/motdepass",methods=['POST','GET'])
def motdepass():
    return render_template('auth/password.html')