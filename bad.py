from flask import Flask, request

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"  # Noncompliant

@app.route('/example')
def log():
    data = request.args["data"]
    app.logger.critical("%s", data) # Noncompliant
