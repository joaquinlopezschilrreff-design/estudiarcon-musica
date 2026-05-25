from flask import Flask, render_template, request, redirect
import sqlite3
conexion = sqlite3.connect("usuarios.db")
cursor = conexion.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER, nombre TEXT, correo TEXT, password TEXT)")
app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def inicio():
    if request.method == "POST":
        correo = request.form["correo"]
        contraseña = request.form["password"]
        print("Flask recibio con exito la informacion")
        print(correo, contraseña)
        return redirect("/start")
    return render_template("login.html")


@app.route("/start", methods=["POST", "GET"])
def principal():
    return render_template("index.html")


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        r_correo = request.form["r_correo"]
        r_password = request.form["r_password"]
        r_confirmacion = request.form["r_confirmacion"]

        if r_password == r_confirmacion:
            r_password = request.form["r_password"]
            cursor.execute("INSERT INTO usuarios (nombre, correo, password) VALUES (?, ?, ?)", (username, r_correo, r_password))
    return render_template("register.html")


app.run(debug=True)
