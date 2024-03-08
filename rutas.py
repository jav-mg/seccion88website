from config import *

# ~~~ rutas ~~~
@app.route("/")
def home():
    cafes = QUERY_buscaTodosLosCafes()
    return render_template("index.html", cafes=cafes)

@app.route("/nuevoCafe")
def nuevoCafe():        
    return render_template('new.html')

@app.route("/saveCafe", methods=["POST"])
def saveCafe():
    name = request.form['name']
    map_url = ""
    imgUrl = request.form['imgUrl']
    location = request.form['location']
    sockets = False
    if request.form['sockets'] == "true":
        sockets = True
    toilet = False
    if request.form['toilet'] == "true":
        toilet = True
    wifi = False
    if request.form['wifi'] == "true":
        wifi = True
    calls = False
    if request.form['calls'] == "true":
        calls = True
    seats = request.form['seats']
    coffeePrice = request.form['coffeePrice']    

    QUERY_insertaNuevoCafe(name, map_url, imgUrl, location, sockets, toilet, wifi, calls, seats, coffeePrice)    
    return redirect(url_for("home"))

@app.route("/eliminarCafe/<id>", methods=["GET"])
def eliminarCafe(id):    
    print(id, file=sys.stdout)
    QUERY_eliminarCafe(id)
    return redirect(url_for("home"))
    