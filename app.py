from flask import Flask, request, render_template
import csv, datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form.get("email")
    user_type = request.form.get("type")
    consent = request.form.get("consent")
    if not all([email, user_type, consent]):
        return "Missing fields", 400
    ip = request.remote_addr
    time = datetime.datetime.utcnow().isoformat()
    with open("submissions.csv", "a") as file:
        file.write(f"{time},{email},{user_type},{ip}\n")
    return render_template("thankyou.html", email=email)

if __name__ == '__main__':
    app.run(debug=True)
