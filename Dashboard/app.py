import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():

    with open("dados.json", "r", encoding="utf-8") as arquivos:
        dados = json.load(arquivos)

    return render_template("index.html", dados=dados)

if __name__ == "__main__":
    app.run(debug=True)