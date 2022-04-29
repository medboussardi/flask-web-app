from flask import Blueprint,render_template,request,flash

auth = Blueprint('auth',__name__)

@auth.route('/login',methods = ['GET','POST'])
def login():
    return render_template("login.html",boolean = False)


@auth.route('/logout')
def logout():
    return "<p> Log out </p>"

@auth.route('/sign-up',methods = ['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password')
        passowrd2 = request.form.get('password2')
        
        if len(email) < 4:
            flash('Email must be greather then 4 character',category='error')
        elif len(firstName) < 2:
            flash('First Name must be greather then 3 character',category='error')
        elif password1 != passowrd2:
            flash('Passwords don\'t match',category='error')
        elif len(password1) < 7:
            flash('passowrd at least shoudl be 7 characters',category='error')
        else:
            flash('Account created!',category='success')
        
    return render_template("sign_up.html")