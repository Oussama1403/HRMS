from .app import db
from flask_login import UserMixin

class Matricules(db.Model):
    matricule = db.Column(db.Integer,primary_key=True)
    is_admin = db.Column(db.Boolean)

class User(UserMixin,db.Model):
    matricule = db.Column(db.Integer,db.ForeignKey('matricules.matricule'),primary_key=True) #cle etranger
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    dep_name = db.Column(db.Integer,db.ForeignKey('departements.name')) #cle etranger
    address = db.Column(db.String(100))
    phone = db.Column(db.Integer)
    salaire = db.Column(db.Integer)
    is_admin = db.Column(db.Boolean,db.ForeignKey('matricules.is_admin'))

    def __init__(self,matricule,first_name,last_name,email,password,dep_name,address,phone,salaire,is_admin):
        self.matricule = matricule
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.dep_name = dep_name
        self.address = address
        self.phone = phone
        self.salaire = salaire
        self.is_admin = is_admin
    
    # override get_id function from UserMixin to return our custom user id (matricule)
    def get_id(self):
        return self.matricule

class Departements(db.Model):
    name = db.Column(db.String(20),primary_key=True)
    employee_count = db.Column(db.Integer)
    
    def __init__(self,name):
        self.name = name
    
class demande_conge(db.Model):
    matricule = db.Column(db.Integer,db.ForeignKey('matricules.matricule'),primary_key=True) #cle etranger
    type_conge = db.Column(db.String)
    date_deb = db.Column(db.DateTime)
    date_fin = db.Column(db.DateTime)
    motif = db.Column(db.String)
    status = db.Column(db.Boolean)

class avance_salaire(db.Model):
    matricule = db.Column(db.Integer,db.ForeignKey('matricules.matricule'),primary_key=True) #cle etranger
    montant = db.Column(db.Integer)
    motif = db.Column(db.String)    
    status = db.Column(db.Boolean)

