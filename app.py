from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from mailing_service import send_email

app = Flask(__name__)

Bootstrap(app=app)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route('/read-form', methods=['POST'])
def read_form():
    data = request.form
    if not data:
        return "FAIL"
    try:
        send_email(
            email=data.get("email"),
            name=data.get("name"),
            subject=data.get("subject"),
            message=data.get("message")
        )
        return "OK"
    except:
        return "FAIL"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
