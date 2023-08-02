from flask import flash,request,render_template,url_for,redirect
from flask_login import login_required
from src.app import db
from src.models import *
from .modules import *
from . import admin

@admin.route("/manage_leave",methods=['POST','GET'])
@login_required
def manage_leave():
    result = AdminOnly()
    if result == False:
        return redirect(url_for('home.home'))
    if request.method == 'POST':
        
        matricule=request.form["matricule"]
        conge = demande_conge.query.filter_by(matricule=matricule).first()
        if request.form['submit_b'] == "Accept":
            conge.status = 1
            flash("Leave requst is accepted")        
        if request.form['submit_b'] == 'Decline':
            conge.status = 0
            flash("Leave request is declined")        
        
        db.session.commit()
        return redirect(url_for('admin.manage_leave'))
    
    else:          
        
        fullname,role = fullname_role() # fix: store this in the session instance.
        result = demande_conge.query.all()
        print(result)
        leave_list = []
        for leave in result:
            leave_list.append({'matricule':leave.matricule,'firstname':User.query.filter_by(matricule=leave.matricule).first().first_name,'type':leave.type_conge,'start_date':leave.date_deb,'end_date':leave.date_fin,'reason':leave.motif})
        return render_template('admin/manage_leave.html',fullname = fullname,role=role,leave_list=leave_list)

@admin.route("/manage_advances",methods=['POST','GET'])
@login_required
def manage_advances():
    result = AdminOnly()
    if result == False:
        return redirect(url_for('home.home'))
    if request.method == 'POST':
        
        matricule=request.form["matricule"]
        advance = avance_salaire.query.filter_by(matricule=matricule).first()
        if request.form['submit_b'] == "Accept":
            advance.status = 1
            flash("Salary advance request is accepted")        
        if request.form['submit_b'] == 'Decline':
            advance.status = 0
            flash("Salary advance request is declined")        
        
        db.session.commit()
        return redirect(url_for('admin.manage_advances'))
    
    else:
        fullname,role = fullname_role()
        result = avance_salaire.query.all()
        advances_list = []
        for advance in result:
            advances_list.append({'matricule':advance.matricule,'firstname':User.query.filter_by(matricule=advance.matricule).first().first_name,'requested_amount':advance.montant,'reason':advance.motif})
        return render_template('admin/manage_advances.html',fullname = fullname,role=role,advances_list=advances_list)

@admin.route("/list_employees",methods=['POST','GET'])
@login_required
def list_employees():
    result = AdminOnly()
    if result == False:
        return redirect(url_for('home.home'))    
    if request.method == 'POST':
        return redirect(url_for('admin.edit_employee',matricule=request.form["matricule"]))
    fullname,role = fullname_role()
    users = User.query.all()
    list_users = []
    for user in users:
        list_users.append({"matricule":user.matricule,"firstname":user.first_name,"lastname":user.last_name,"dep":user.dep_name,"salary":user.salaire})
    return render_template('admin/list_employees.html',list_users = list_users,fullname = fullname,role=role)

@admin.route("/edit_employee/<matricule>",methods=['POST','GET'])
@login_required
def edit_employee(matricule):
    result = AdminOnly()
    if result == False:
        return redirect(url_for('home.home'))    
    if request.method == 'POST':
        # update user made if apply changes button is pressed or delete user if delete button if pressed.
        if request.form['submit_b'] == "Apply":
            
            # get data.       
            first_name = request.form["firstname"]
            last_name = request.form["lastname"]
            email = request.form["email"]
            address = request.form["address"]
            dep = request.form["dep"]
            phone = request.form["phone"]
            salary = request.form["salary"]
            
            # To update data, modify attributes on the model objects:
            user = User.query.filter_by(matricule=matricule).first()
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.address = address
            user.dep_name = dep
            user.phone = phone
            user.salaire = salary
            db.session.commit()
            
            flash("Account details have been saved successfully")            
            return redirect(url_for('admin.edit_employee',matricule=matricule))
        if request.form['submit_b'] == "Delete":
            
            user = User.query.filter_by(matricule=matricule).first()
            db.session.delete(user)
            db.session.commit()
            flash("User account successfully deleted")
            return redirect(url_for('admin.list_employees'))            
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
        salary = user.salaire
        return render_template('admin/edit.html',matricule=matricule,fullname = firstname + " " + lastname,firstname=firstname,lastname=lastname,email=email,phone=phone,address=address,dep = dep,salary=salary)

@admin.route("/list_dep")
@login_required
def list_dep():
    result = AdminOnly()
    if result == False:
        return redirect(url_for('home.home'))
    fullname,role = fullname_role()
    deps = Departements.query.all()
    list_dep = []
    for dep in deps:
        dep_emp_count = len(User.query.filter_by(dep_name = dep.name).all()) 
        list_dep.append({"name":dep.name,"count":dep_emp_count})
    return render_template('admin/list_dep.html',list_dep = list_dep,fullname = fullname,role=role)
