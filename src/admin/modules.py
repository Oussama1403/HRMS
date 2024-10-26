from flask import flash
from flask_login import current_user
from src.models import *

def AdminOnly():
    employee_id = current_user.employee_id
    if current_user.is_admin == 0:
        flash("Administrative access only")
    return True if current_user.is_admin == 1 else False

def fullname_role():
    fullname = current_user.first_name + " " + current_user.last_name
    is_admin = 'Administrator' if current_user.is_admin == 1 else 'Employee'
    return (fullname,is_admin)