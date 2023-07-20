from flask import request,render_template,flash,redirect,url_for
from flask_login import login_user,current_user
from src.app import db
from src.models import *
from datetime import datetime


def fullname_role():
    fullname = current_user.first_name + " " + current_user.last_name
    user = Matricules.query.filter_by(matricule=current_user.matricule).first()
    is_admin = 'Administrateur' if user.is_admin == 1 else 'Employé'
    return (fullname,is_admin)

def DemandeConge():
    matricule = current_user.matricule
    type_conge = request.form["leave-type"]
    try:
        date_deb = request.form["date_start"].strip()
        date_deb = datetime.strptime(date_deb, '%d/%m/%Y')   
        
        date_fin = request.form["date_end"].strip()
        date_fin = datetime.strptime(date_fin, '%d/%m/%Y')   
    except:
        flash("date erroné")        
        return render_template("user/demande_conge.html")

    motif = request.form["reason"] 
    try:
        new = demande_conge(matricule=matricule,type_conge=type_conge,date_deb=date_deb,date_fin=date_fin,motif=motif)
        db.session.add(new)
        db.session.commit()
        flash("demande de congé appliquée avec succès")
    except:
        flash("vous avez une demande de congé en attente")
   
    return render_template("user/demande_conge.html")

def DemandeAvance():
    matricule = current_user.matricule
    montant = request.form["montant"]
    motif = request.form["reason"] 
    try:
        new = avance_salaire(matricule=matricule,montant=montant,motif=motif)
        db.session.add(new)
        db.session.commit()
        flash("avance sur salaire appliquée avec succès")
    except:
        flash("vous avez une demande d'avance sur salaire en attente")
            
    return render_template("user/demande_avance.html")