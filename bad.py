from flask import Flask, request

app = Flask(__name__)

@app.route('/example')
def log():
    data = request.args["data"]
    app.logger.critical("%s", data) # Noncompliant
