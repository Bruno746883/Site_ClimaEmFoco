from flask import Flask, render_template, send_from_directory, jsonify
from sec_fun import N_E_R

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html',N_E_P = N_E_R)

@app.route("/pais")
def pais():
    return render_template('pais.html')

if __name__ == "__main__":
    app.run(debug=True)
