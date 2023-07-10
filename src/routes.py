""" App Routing """

from flask import flash,request,render_template,url_for,redirect,send_from_directory,abort,after_this_request,session
from .app import app,db
from .models import *
from flask_login import login_user,login_required,current_user
from .modules import *

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
@login_required
def demande_conge():
    fullname,role = fullname_role()
    return render_template('demande_conge.html',fullname = fullname,role=role)

@app.route("/demande_avance")
@login_required
def demande_avance():
    fullname,role = fullname_role()
    return render_template('demande_avance.html',fullname = fullname,role=role)

@app.route("/motdepass",methods=['POST','GET'])
def motdepass():
    return render_template('password.html')

@app.route("/gere_conge")
@login_required
def gere_conge():
    fullname,role = fullname_role()
    return render_template('gere_conge.html',fullname = fullname,role=role)

@app.route("/liste_employees")
@login_required
def liste_employees():
    fullname,role = fullname_role()
    users = User.query.all()
    list_users = []
    for user in users:
        list_users.append({"matricule":user.matricule,"firstname":user.first_name,"lastname":user.last_name,"dep":user.dep_name,"salaire":user.salaire})
    return render_template('liste_employees.html',list_users = list_users,fullname = fullname,role=role)

@app.route("/liste_dep")
@login_required
def liste_dep():
    fullname,role = fullname_role()
    deps = Departements.query.all()
    list_dep = []
    for dep in deps:
        dep_emp_count = len(User.query.filter_by(dep_name = dep.name).all()) 
        list_dep.append({"name":dep.name,"count":dep_emp_count})
    return render_template('liste_dep.html',list_dep = list_dep,fullname = fullname,role=role)


# AUTH VIEWS

@app.route("/login",methods=['POST','GET'])
def login():
    if request.method == 'POST':
        response = LoginAccount()
        return response
    else:
        return render_template('login.html')    

@app.route("/register",methods=['POST','GET'])
def register():
    # TODO:FORM VALIDATION
    if request.method == 'POST':
        response = RegisterAccount()
        return response
    else:
        return render_template('register.html')     

@app.route('/logout')
def logout():
    return 'Logout'   

# ERROR HANDLING

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

@app.errorhandler(500)
def server_error(error):
    return render_template("500.html"), 500

@app.errorhandler(401)
def access_denied(error):
    return render_template("401.html"), 401