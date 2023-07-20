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


@app.route("/conge",methods=['POST','GET'])
@login_required
def conge():
    if request.method == 'POST':
        return DemandeConge()
    else:
        fullname,role = fullname_role()
        return render_template('demande_conge.html',fullname = fullname,role=role)

@app.route("/demande_avance",methods=['POST','GET'])
@login_required
def demande_avance():
    if request.method == 'POST':
        return DemandeAvance()
    fullname,role = fullname_role()
    return render_template('demande_avance.html',fullname = fullname,role=role)

@app.route('/suivie')
@login_required
def suivie():
    fullname,role = fullname_role()

    matricule = current_user.matricule
    conge = demande_conge.query.filter_by(matricule=matricule).first()
    avance = avance_salaire.query.filter_by(matricule=matricule).first()
    list_conge = {}
    list_avance = {}
    if conge or avance:
        if conge:
            if conge.status == 1: 
                conge_status = 'Accepté'  
            elif conge.status == 0: 
                conge_status = 'Refusé'
            else:
                conge_status = 'Attente'       
            list_conge = {'matricule':conge.matricule,'nom':User.query.filter_by(matricule=conge.matricule).first().first_name,'type':conge.type_conge,'date_deb':conge.date_deb,'date_fin':conge.date_fin,'motif':conge.motif,'status':conge_status}
        if avance:
            if avance.status == 1: 
                avance_status = 'Accepté'  
            elif avance.status == 0: 
                avance_status = 'Refusé'
            else:
                avance_status = 'Attente'  
            avance_status = 'Accepté' if avance.status == 1 else 'Refusé'
            list_avance = {'matricule':avance.matricule,'nom':User.query.filter_by(matricule=avance.matricule).first().first_name,'montant':avance.montant,'motif':avance.motif,'status':avance_status}
        return render_template('suivie.html',conge=list_conge,avance=list_avance,fullname = fullname,role=role)
    else:
       return render_template('suivie.html',conge=None,avance=None,fullname = fullname,role=role)


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