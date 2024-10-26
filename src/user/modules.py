from flask import request,render_template,flash
from flask_login import current_user
from src.app import db
from src.models import *
from datetime import datetime


def fullname_role():
    fullname = current_user.first_name + " " + current_user.last_name
    is_admin = 'Administrator' if current_user.is_admin == 1 else 'Employee'
    return (fullname,is_admin)

def RequestLeave():
    employee_id = current_user.employee_id
    leave_type = request.form["leave-type"]
    reason = request.form["reason"] 
    try:
        date_start = request.form["date_start"].strip()
        date_start = datetime.strptime(date_start, '%d/%m/%Y')   
        
        date_end = request.form["date_end"].strip()
        date_end = datetime.strptime(date_end, '%d/%m/%Y')   
    except:
        flash("Wrong date")        
        return render_template("user/request_leave.html")    
    
    # check for pending request
    row = demande_conge.query.filter_by(employee_id=employee_id).first()
    if row:
        flash("You have a leave request pending")
        return render_template("user/request_leave.html")
    
    new = demande_conge(employee_id=employee_id,type_conge=leave_type,date_deb=date_start,date_fin=date_end,motif=reason)
    db.session.add(new)
    db.session.commit()
    flash("Leave request applied successfully")
    return render_template("user/request_leave.html")

def RequestAdvance():
    employee_id = current_user.employee_id
    requested_amount = request.form["requested_amount"]
    reason = request.form["reason"] 
    
    # check for pending request
    row = avance_salaire.query.filter_by(employee_id=employee_id).first()
    if row:
        flash("You have a salary advance request pending")
        return render_template("user/request_advance.html")
    
    new = avance_salaire(employee_id=employee_id,montant=requested_amount,motif=reason)
    db.session.add(new)
    db.session.commit()
    flash("Salary advance request applied successfully")
    return render_template("user/request_advance.html") 