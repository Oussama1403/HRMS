from flask import flash,request,render_template,url_for,redirect,send_from_directory,abort,after_this_request,session
from flask_login import login_user,logout_user,login_required,current_user


from .modules import *
from . import user

@user.route("/conge",methods=['POST','GET'])
@login_required
def conge():
    if request.method == 'POST':
        return DemandeConge()
    else:
        fullname,role = fullname_role()
        return render_template('user/demande_conge.html',fullname = fullname,role=role)

@user.route("/demande_avance",methods=['POST','GET'])
@login_required
def demande_avance():
    if request.method == 'POST':
        return DemandeAvance()
    fullname,role = fullname_role()
    return render_template('user/demande_avance.html',fullname = fullname,role=role)

@user.route('/suivie')
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
        return render_template('user/suivie.html',conge=list_conge,avance=list_avance,fullname = fullname,role=role)
    else:
       return render_template('user/suivie.html',conge=None,avance=None,fullname = fullname,role=role)

