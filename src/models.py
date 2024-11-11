from .app import db
from flask_login import UserMixin

class User(UserMixin,db.Model):
    employee_id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    gender = db.Column(db.String(20))
    date_of_birth = db.Column(db.Date)  # New date of birth field
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    dep_name = db.Column(db.Integer,db.ForeignKey('departements.name')) #foreign key
    address = db.Column(db.String(100))
    phone = db.Column(db.Integer)
    salaire = db.Column(db.Integer)
    is_admin = db.Column(db.Boolean)

    def __init__(self,employee_id,first_name,last_name,gender,date_of_birth,email,password,dep_name,address,phone,salaire,is_admin):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.date_of_birth = date_of_birth  
        self.email = email
        self.password = password
        self.dep_name = dep_name
        self.address = address
        self.phone = phone
        self.salaire = salaire
        self.is_admin = is_admin
    
    # override get_id function from UserMixin to return our custom user id (matricule)
    def get_id(self):
        return self.employee_id

class Departements(db.Model):
    name = db.Column(db.String(20),primary_key=True)
    employee_count = db.Column(db.Integer)
    
    def __init__(self,name):
        self.name = name
    
class demande_conge(db.Model):
    employee_id = db.Column(db.Integer,primary_key=True)
    type_conge = db.Column(db.String)
    date_deb = db.Column(db.DateTime)
    date_fin = db.Column(db.DateTime)
    motif = db.Column(db.String)
    status = db.Column(db.Boolean)

class avance_salaire(db.Model):
    employee_id = db.Column(db.Integer,primary_key=True)
    montant = db.Column(db.Integer)
    motif = db.Column(db.String)    
    status = db.Column(db.Boolean)

