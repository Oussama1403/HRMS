from flask import request,render_template
from flask_login import login_required,current_user


from .modules import *
from . import user

@user.route("/request_leave",methods=['POST','GET'])
@login_required
def request_leave():
    if request.method == 'POST':
        return RequestLeave()
    else:
        fullname,role = fullname_role()
        return render_template('user/request_leave.html',fullname = fullname,role=role)

@user.route("/request_advance",methods=['POST','GET'])
@login_required
def request_advance():
    if request.method == 'POST':
        return RequestAdvance()
    fullname,role = fullname_role()
    return render_template('user/request_advance.html',fullname = fullname,role=role)

@user.route('/follow_up')
@login_required
def follow_up():
    fullname,role = fullname_role()

    employee_id = current_user.employee_id
    leave = demande_conge.query.filter_by(employee_id=employee_id).first()
    advance = avance_salaire.query.filter_by(employee_id=employee_id).first()
    leave_list = {}
    advance_list = {}
    if leave or advance:
        if leave:
            if leave.status == 1: 
                leave_status = 'Accepted'  
            elif leave.status == 0: 
                leave_status = 'Declined'
            else:
                leave_status = 'Pending'       
            leave_list = {'employee_id':leave.employee_id,'nom':User.query.filter_by(employee_id=leave.employee_id).first().first_name,'type':leave.type_conge,'date_deb':leave.date_deb,'date_fin':leave.date_fin,'motif':leave.motif,'status':leave_status}
        if advance:
            if advance.status == 1: 
                advance_status = 'Accepted'  
            elif advance.status == 0: 
                advance_status = 'Declined'
            else:
                advance_status = 'Pending'  
            advance_list = {'employee_id':advance.employee_id,'nom':User.query.filter_by(employee_id=advance.employee_id).first().first_name,'montant':advance.montant,'motif':advance.motif,'status':advance_status}
        return render_template('user/followup.html',leave=leave_list,advance=advance_list,fullname = fullname,role=role)
    else:
       return render_template('user/followup.html',conge=None,avance=None,fullname = fullname,role=role)

