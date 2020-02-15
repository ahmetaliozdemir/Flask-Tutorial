from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Anasayfa"

@app.route("/sayfa/<string:id>")
def sayfa(id):
    return id

if __name__ == "__main__":
    app.run(debug = True)
