from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<icerikurl>")
def icerik(icerikurl=None):
    return render_template("icerik.html",icerikurl=icerikurl)

@app.route("/<konu>/<icerikurl>")
def konu(icerikurl=None,konu=None):
    return render_template("icerik.html",icerikurl=icerikurl,konu=konu)

@app.route("/sayfa/<sayfaadi>")
def sayfa(sayfaadi=None):
    iyazi = "<h1>İçerik Yazı</h1>"
    return render_template("sayfa.html",sayfaadi=sayfaadi,iyazi=iyazi)

@app.route("/dizi")
def dizi():
    numbers = [1,2,3,4,5,6,7,8,9]
    return render_template("dizi.html",numbers=numbers)

@app.route("/islem")
def islem():
    return render_template("get-post.html")

@app.route("/toplama",methods = ["GET","POST"])
def toplama():
    if request.method == "POST":
        number1 = request.form.get("number1")
        number2 = request.form.get("number2")
        return render_template("toplama.html" ,total = int(number1) + int(number2))
    else:
        return render_template("toplama.html")
    

if __name__ == "__main__":
    app.run(debug = True)
