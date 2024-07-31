from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def HOME():
    return render_template('HOME.html')

@app.route('/about')
def ABOUT():
    return render_template('ABOUTUS.html')

@app.route('/signup')
def SIGNUP():
        if request.method == 'POST':
        # Get user input from the form
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']

        # Check if the username already exists in the database
        if username.find_one({'username': username}):
            return "Username already exists. Please choose a different one."

        # Create a new user document and insert it into the database
        new_user = {
            'username': username,
            'email': email,
            'password': password
        }
        username.insert_one(new_user)
        return render_template("SIGNUP.html")
    
@app.route('/log')
def LOGIN():
 return render_template('login.html')




if __name__ ==('_main_'):
    app.run(debug=True)