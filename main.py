from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('login.html')

@app.route("/", methods = ['POST'])
def validate_info():

    username = request.form["username"] 
    password = request.form["password"]
    verify = request.form["verify"]
    email = request.form["email"]

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""    

    if username == "":
        username_error = "Please enter a username"
    elif len(username) < 3:
        username_error = "Usernames must be atleast 3 characters long"
    elif len(username) > 20:
        username_error = "Usernames must be under 20 characters long"
    elif " " in username:
        username_error = "Usernames may not contain a space"
    
    if password == "":
        password_error = "Please enter a password"
    elif len(password) < 3:
        password_error = "Passwords must be atleast 3 characters long"
    elif len(password) > 20:
        password_error = "Passwords must be under 20 characters long"
    elif " " in password:
        password_error = "Passwords may not contain a space"
    elif password != verify:
        password_error = "Your passwords need to match"

    if verify == "":
        verify_error = "Please confirm your password"
    elif len(verify) < 3:
        verify_error = "Passwords must be atleast 3 characters long"
    elif len(verify) > 20:
        verify_error = "Passwords must be under 20 characters long"
    elif " " in verify:
        verify_error = "Passwords may not contain a space"
    elif verify != password:
        verify_error = "Your passwords need to match"
    
    if (len(email) >= 1 and len(email) < 3) or len(email) > 20:
        email_error = "Please enter a valid email address"
    elif " " in email:
        email_error = "Please enter a valid email address"
    elif "@" in email and email.count("@") > 1:
        email_error = "Please enter a valid email address"
    elif len(email) > 0 and "@" not in email:
        email_error = "Please enter a valid email address"
    elif "." in email and email.count(".") > 1:
        email_error = "Please enter a valid email address"  
    elif len(email) >0 and "." not in email:
        email_error = "Please enter a valid email address" 
   
    if not username_error and not password_error and not verify_error and not email_error:
        return render_template ('welcome.html') 
    else:
        return render_template('login.html', username_error = username_error, 
        password_error = password_error,
        verify_error = verify_error,
        email_error = email_error,
        username = username,
        password = password,
        verify = verify,
        email = email)
        
app.run()