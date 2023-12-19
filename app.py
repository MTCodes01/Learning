from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Mock database storing user credentials (in practice, use a secure database)
users = {
    'MT@gmail.com': {'password': 'MT'},
    'MS@gmail.com': {'password': 'MS'}
}

@app.route('/')
def index():
    return render_template('index.html')  # Render your HTML form

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']  # Access the email input value from the form
        password = request.form['password']  # Access the password input value from the form

        # Check if the email exists in the mock database
        if email in users:
            # Check if the password matches the stored password for the email
            if password == users[email]['password']:
                # Redirect to a success page or perform actions for successful login
                return redirect(url_for('success'))
        
        # If email or password is incorrect, redirect to a login error page
        return redirect(url_for('login_error'))

@app.route('/success')
def success():
    return "Login Successful"

@app.route('/login_error')
def login_error():
    return "Invalid email or password. Please try again."

if __name__ == '__main__':
    app.run(debug=True)
