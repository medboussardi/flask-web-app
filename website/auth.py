from ast import Pass
from flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import User
from werkzeug.security import generate_password_hash,check_password_hash
from . import db 
from flask_login import login_user,login_required,logout_user,current_user


auth = Blueprint('auth',__name__)

@auth.route('/login',methods = ['GET','POST'])
def login():
    if request.method == 'POST':  #taking user data
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        
        if user:
            if check_password_hash(user.password,password):
                flash('loged in successfully !!',category='sucess')
                login_user(user,remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('incorrect password',category='error')
        else:
            flash('Email does not exist.',category='error')
        
    return render_template("login.html",user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up',methods = ['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password')
        passowrd2 = request.form.get('password2')
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exist!',category='error')       
        elif len(email) < 4:
            flash('Email must be greather then 4 character',category='error')
        elif len(firstName) < 2:
            flash('First Name must be greather then 3 character',category='error')
        elif password1 != passowrd2:
            flash('Passwords don\'t match',category='error')
        elif len(password1) < 7:
            flash('passowrd at least shoudl be 7 characters',category='error')
        else:
            new_user = User(email=email,first_name=firstName,password=generate_password_hash(password1,method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user,remember=True)
            flash('Account created!',category='success')
            return redirect(url_for("views.home"))
        
    return render_template("sign_up.html",user=current_user)