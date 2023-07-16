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



@app.route("/gere_conge",methods=['POST','GET'])
@login_required
def gere_conge():
    result = AdminOnly()
    if result == False:
        return redirect(url_for('home'))
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
        return redirect(url_for('gere_conge'))
    
    else:          
        
        fullname,role = fullname_role() # fix: store this in the session instance.
        result = demande_conge.query.all()
        list_conge = []
        for conge in result:
            list_conge.append({'matricule':conge.matricule,'nom':User.query.filter_by(matricule=conge.matricule).first().first_name,'type':conge.type_conge,'date_deb':conge.date_deb,'date_fin':conge.date_fin,'motif':conge.motif})
        return render_template('gere_conge.html',fullname = fullname,role=role,list_conge=list_conge)

@app.route("/gere_avance",methods=['POST','GET'])
@login_required
def gere_avance():
    result = AdminOnly()
    if result == False:
        return redirect(url_for('home'))
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
        return redirect(url_for('gere_avance'))
    
    else:
        fullname,role = fullname_role()
        result = avance_salaire.query.all()
        list_avance = []
        for avance in result:
            list_avance.append({'matricule':avance.matricule,'nom':User.query.filter_by(matricule=avance.matricule).first().first_name,'montant':avance.montant,'motif':avance.motif})
        return render_template('gere_avance.html',fullname = fullname,role=role,list_avance=list_avance)

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


@app.route("/liste_employees",methods=['POST','GET'])
@login_required
def liste_employees():
    result = AdminOnly()
    if result == False:
        return redirect(url_for('home'))    
    if request.method == 'POST':
        return redirect(url_for('edit_employee',matricule=request.form["matricule"]))
    fullname,role = fullname_role()
    users = User.query.all()
    list_users = []
    for user in users:
        list_users.append({"matricule":user.matricule,"firstname":user.first_name,"lastname":user.last_name,"dep":user.dep_name,"salaire":user.salaire})
    return render_template('liste_employees.html',list_users = list_users,fullname = fullname,role=role)

@app.route("/edit_employee/<matricule>",methods=['POST','GET'])
@login_required
def edit_employee(matricule):
    result = AdminOnly()
    if result == False:
        return redirect(url_for('home'))    
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
            
            # To update data, modify attributes on the model objects:
            
            user = User.query.filter_by(matricule=matricule).first()
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.address = address
            user.dep_name = dep
            user.phone = phone
            
            db.session.commit()
            flash("Account details have been saved successfully")            
            return redirect(url_for('edit_employee',matricule=matricule))
        if request.form['submit_b'] == "Supprimer":
            
            user = User.query.filter_by(matricule=matricule).first()
            db.session.delete(user)
            db.session.commit()
            flash("User account successfully deleted")
            return redirect(url_for('liste_employees'))            
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
        return render_template('profile.html',matricule=matricule,fullname = firstname + " " + lastname,firstname=firstname,lastname=lastname,email=email,phone=phone,address=address,dep = dep)

@app.route("/liste_dep")
@login_required
def liste_dep():
    result = AdminOnly()
    if result == False:
        return redirect(url_for('home'))
    fullname,role = fullname_role()
    deps = Departements.query.all()
    list_dep = []
    for dep in deps:
        dep_emp_count = len(User.query.filter_by(dep_name = dep.name).all()) 
        list_dep.append({"name":dep.name,"count":dep_emp_count})
    return render_template('liste_dep.html',list_dep = list_dep,fullname = fullname,role=role)


@app.route("/motdepass",methods=['POST','GET'])
def motdepass():
    return render_template('password.html')

# AUTH VIEWS

@app.route("/login",methods=['POST','GET'])
def login():
    if request.method == 'POST':
        response = LoginAccount()
        return response
    else:
        return render_template('login.html')    

@app.route("/register",methods=['POST','GET'])
def register():
    # TODO:FORM VALIDATION
    if request.method == 'POST':
        response = RegisterAccount()
        return response
    else:
        return render_template('register.html')     

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

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