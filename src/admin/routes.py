from flask import flash,request,render_template,url_for,redirect
from flask_login import login_user,logout_user,login_required,current_user
from src.app import app,db
from src.models import *
from .modules import *
from . import admin
#from src.home import home

@admin.route("/gere_conge",methods=['POST','GET'])
@login_required
def gere_conge():
    result = AdminOnly()
    if result == False:
        return redirect(url_for('home.home'))
    if request.method == 'POST':
        
        matricule=request.form["matricule"]
        conge = demande_conge.query.filter_by(matricule=matricule).first()
        if request.form['submit_b'] == "Accepter":
            conge.status = 1
            flash("Congé est accepté")        
        if request.form['submit_b'] == 'Refuser':
            conge.status = 0
            flash("Congé est refusé")        
        
        db.session.commit()
        return redirect(url_for('admin.gere_conge'))
    
    else:          
        
        fullname,role = fullname_role() # fix: store this in the session instance.
        result = demande_conge.query.all()
        print(result)
        list_conge = []
        for conge in result:
            list_conge.append({'matricule':conge.matricule,'nom':User.query.filter_by(matricule=conge.matricule).first().first_name,'type':conge.type_conge,'date_deb':conge.date_deb,'date_fin':conge.date_fin,'motif':conge.motif})
        return render_template('admin/gere_conge.html',fullname = fullname,role=role,list_conge=list_conge)

@admin.route("/gere_avance",methods=['POST','GET'])
@login_required
def gere_avance():
    result = AdminOnly()
    if result == False:
        return redirect(url_for('home.home'))
    if request.method == 'POST':
        
        matricule=request.form["matricule"]
        avance = avance_salaire.query.filter_by(matricule=matricule).first()
        if request.form['submit_b'] == "Accepter":
            avance.status = 1
            flash("Avance est accepté")        
        if request.form['submit_b'] == 'Refuser':
            avance.status = 0
            flash("Avance est refusé")        
        
        db.session.commit()
        return redirect(url_for('admin.gere_avance'))
    
    else:
        fullname,role = fullname_role()
        result = avance_salaire.query.all()
        list_avance = []
        for avance in result:
            list_avance.append({'matricule':avance.matricule,'nom':User.query.filter_by(matricule=avance.matricule).first().first_name,'montant':avance.montant,'motif':avance.motif})
        return render_template('admin/gere_avance.html',fullname = fullname,role=role,list_avance=list_avance)

@admin.route("/liste_employees",methods=['POST','GET'])
@login_required
def liste_employees():
    result = AdminOnly()
    if result == False:
        return redirect(url_for('home.home'))    
    if request.method == 'POST':
        return redirect(url_for('admin.edit_employee',matricule=request.form["matricule"]))
    fullname,role = fullname_role()
    users = User.query.all()
    list_users = []
    for user in users:
        list_users.append({"matricule":user.matricule,"firstname":user.first_name,"lastname":user.last_name,"dep":user.dep_name,"salaire":user.salaire})
    return render_template('admin/liste_employees.html',list_users = list_users,fullname = fullname,role=role)

@admin.route("/edit_employee/<matricule>",methods=['POST','GET'])
@login_required
def edit_employee(matricule):
    result = AdminOnly()
    if result == False:
        return redirect(url_for('home.home'))    
    if request.method == 'POST':
        # update user made if apply changes button is pressed or delete user if delete button if pressed.
        if request.form['submit_b'] == "Appliquer":
            
            # get data.       
            
            first_name = request.form["firstname"]
            last_name = request.form["lastname"]
            email = request.form["email"]
            address = request.form["address"]
            dep = request.form["dep"]
            phone = request.form["phone"]
            salaire = request.form["salaire"]
            # To update data, modify attributes on the model objects:
            
            user = User.query.filter_by(matricule=matricule).first()
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.address = address
            user.dep_name = dep
            user.phone = phone
            user.salaire = salaire
            db.session.commit()
            flash("Account details have been saved successfully")            
            return redirect(url_for('admin.edit_employee',matricule=matricule))
        if request.form['submit_b'] == "Supprimer":
            
            user = User.query.filter_by(matricule=matricule).first()
            db.session.delete(user)
            db.session.commit()
            flash("User account successfully deleted")
            return redirect(url_for('admin.liste_employees'))            
    else:
        # request user by matricule and get fullname,email,phone,dep,adress
        # send to profile page
        user = User.query.filter_by(matricule = matricule).first()
        matricule = user.matricule
        firstname = user.first_name 
        lastname = user.last_name
        email = user.email
        phone = user.phone 
        dep = user.dep_name
        address = user.address
        salaire = user.salaire
        return render_template('admin/edit.html',matricule=matricule,fullname = firstname + " " + lastname,firstname=firstname,lastname=lastname,email=email,phone=phone,address=address,dep = dep,salaire=salaire)

@admin.route("/liste_dep")
@login_required
def liste_dep():
    result = AdminOnly()
    if result == False:
        return redirect(url_for('home.home'))
    fullname,role = fullname_role()
    deps = Departements.query.all()
    list_dep = []
    for dep in deps:
        dep_emp_count = len(User.query.filter_by(dep_name = dep.name).all()) 
        list_dep.append({"name":dep.name,"count":dep_emp_count})
    return render_template('admin/liste_dep.html',list_dep = list_dep,fullname = fullname,role=role)
