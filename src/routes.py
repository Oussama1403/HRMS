""" App Routing """

from flask import flash,request,render_template,url_for,redirect,send_from_directory,abort,after_this_request,session
from .app import app,db
from .models import *
from flask_login import login_user,login_required,current_user

#from .modules import *

@app.route('/',methods=['GET'])
def base():
    return redirect(url_for('home'))

@app.route('/home',methods=['POST','GET'])
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
    is_admin = 'Administrateur' if user.is_admin == 1 else 'Employé'
    return render_template('home.html',matricule=matricule,fullname=fullname,email=email,phone=phone,address=address,dep = dep,role=is_admin)
    

@app.route("/demande_conge")
def demande_conge():
    return render_template('demande_conge.html')
@app.route("/demande_avance")
def demande_avance():
    return render_template('demande_avance.html')

@app.route("/motdepass")
def motdepass():
    return render_template('password.html')

@app.route("/gere_conge")
def gere_conge():
    return render_template('gere_conge.html')

@app.route("/liste_employees")
def liste_employees():
    return render_template('liste_employees.html')

@app.route("/liste_dep")
def liste_dep():
    return render_template('liste_dep.html')

# auth

@app.route("/login",methods=['POST','GET'])
def login():
    if request.method == 'POST':
        matricule = request.form["matricule"]         
        password = request.form["password"]
        user = User.query.filter_by(matricule=matricule).first()
        if not user or user.password != password:
            flash('Veuillez vérifier vos informations et réessayer.')
            return render_template('login.html')
        
        login_user(user,False)
        return redirect(url_for('home'))

    else:
        return render_template('login.html')    

@app.route("/register",methods=['POST','GET'])
def register():
    # TODO:FORM VALIDATION

    if request.method == 'POST':
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
        new_user = User(matricule=matricule,first_name=first_name,last_name=last_name,email=email,password=password,phone=phone,address=address,dep_name = dep)
        db.session.add(new_user)
        db.session.commit()
        flash("Your account has been successfully created !")
        return render_template("register.html")
    
    else:
        return render_template('register.html')     

@app.route('/logout')
def logout():
    return 'Logout'   

# error handling

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

@app.errorhandler(500)
def server_error(error):
    return render_template("500.html"), 500
