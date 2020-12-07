from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin
from flask_mysqldb import MySQL

app = Flask(__name__)
# mysql database
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "Ranti"

mysql = MySQL(app)
app.secret_key="mysecretkey"

@app.route("/")
def index_():
    return render_template("index_admin.html")


@app.route("/cliente_admin/")
def cliente_admin():
    cur = mysql.connection.cursor()
    cur.execute("select * from cliente")
    data = cur.fetchall()
    return render_template("/cliente_admin.html", cliente=data)


#cliente administrador 
@app.route("/add_cliente", methods=["POST"]) #lleva la informacion desde el formulario
def add_cliente():
        if request.method == "POST":
            nom = request.form["nombres"]
            dis = request.form["distrito"]
            direc = request.form["direccion"]
            em = request.form["email"]
            cel = request.form["telefono"]
            contra = request.form["contraseña"]
            print("INSERT", id, nom, dis, direc, em, cel, contra)
            cur = mysql.connection.cursor()
            cur.execute("insert into cliente(nombres, distrito, direccion, email, telefono, contrasena) values(%s,%s,%s,%s,%s,%s)", (nom, dis, direc, em, cel, contra))
            mysql.connection.commit()
            flash("Contacto Insertado Correctamente")
            return redirect (url_for("cliente_admin"))
        return "cliente"

@app.route("/edit_cliente/<id>")
def edit_cliente(id):
    cur = mysql.connection.cursor()
    cur.execute("select * from cliente where id = %s",{id})
    data = cur.fetchall()
    print(data[0])
    return render_template("/editcliente_admin.html",client=data[0])

@app.route("/delete_cliente/<string:id>")
def delete_cliente(id):
    cur = mysql.connection.cursor()
    cur.execute("delete from cliente where id = {0}".format(id))
    mysql.connection.commit()
    flash("Contacto Eliminado correctamente")
    return redirect(url_for("cliente_admin"))

@app.route("/update_cliente/<id>",methods=["POST"]) #envia la informacion
def update_cliente(id):
    if request.method == "POST":
        nom2 = request.form["nombre"]
        dis2 = request.form["distrito"]
        direc2 = request.form["direccion"]
        em2 = request.form["email"]
        cel2 = request.form["telefono"]
        contra2 = request.form["contraseña"]
        print("UPDATE", id, nom2, dis2, direc2, em2, cel2, contra2)
        cur = mysql.connection.cursor() #coneccion
        cur.execute("""
            update cliente
            set nombres = %s,   
            distrito =%s,
            direccion = %s,
            email = %s,
            telefono = %s,
            contrasena = %s
            where id = %s
        """,(nom2, dis2, direc2, em2, cel2, contra2,id) ) #realizando el cambio y pasando los datos
        mysql.connection.commit()
        flash("Vendedor Actualizado Correctamente")
        return redirect (url_for("cliente_admin")) #redirigia a la nueva pagina

@app.route("/vendedor_admin/")
def vendedor_admin():
    cur = mysql.connection.cursor()
    cur.execute("select * from vendedor")
    data = cur.fetchall()
    return render_template("/vendedor_admin.html", vendedor=data )

#vendedor administrador
@app.route("/add_vendedor", methods=["POST"]) #lleva la informacion desde el formulario
def add_vendedor():
        if request.method == "POST":
            nom2 = request.form["nombres"]
            ruc = request.form["RUC"]
            dis2 = request.form["distrito"]
            direc2 = request.form["direccion"]
            em2 = request.form["email"]
            cel2 = request.form["telefono"]
            contra2 = request.form["contraseña"]
            print("INSERT", id, nom2, ruc, dis2, direc2, em2, cel2, contra2)
            cur = mysql.connection.cursor()
            cur.execute("insert into vendedor(nombres, RUC, distrito, direccion, email, telefono, contrasena) values(%s,%s,%s,%s,%s,%s,%s)", (nom2, ruc, dis2, direc2, em2, cel2, contra2))
            mysql.connection.commit()
            flash("Vendedor Insertado Correctamente")
            return redirect (url_for("vendedor_admin"))
        return "vendedor"



@app.route("/edit_vendedor/<id>")
def edit_vendedor(id):
    cur = mysql.connection.cursor()
    cur.execute("select * from vendedor where id = %s",{id})
    data = cur.fetchall()
    print(data[0])
    return render_template("/editvendedor_admin.html",vend=data[0])

@app.route("/delete_vendedor/<string:id>")
def delete_vendedor(id):
    cur = mysql.connection.cursor()
    cur.execute("delete from vendedor where id = {0}".format(id))
    mysql.connection.commit()
    flash("Vendedor Eliminado correctamente")
    return redirect(url_for("vendedor_admin"))

@app.route("/update_vendedor<id>",methods=["POST"]) #envia la informacion
def update_vendedor(id):
    if request.method == "POST":
        nom2 = request.form["nombre"]
        ruc = request.form["RUC"]
        dis2 = request.form["distrito"]
        direc2 = request.form["direccion"]
        em2 = request.form["email"]
        cel2 = request.form["telefono"]
        contra2 = request.form["contraseña"]
        print("UPDATE", id, nom2, ruc, dis2, direc2, em2, cel2, contra2)
        cur = mysql.connection.cursor() #coneccion
        cur.execute("""
            update vendedor
            set nombres = %s,   
            RUC = %s,
            distrito =%s,
            direccion = %s,
            email = %s,
            telefono = %s,
            contrasena = %s
            where id = %s
        """,(nom2, ruc, dis2, direc2, em2, cel2, contra2,id) ) #realizando el cambio y pasando los datos
        mysql.connection.commit()
        flash("Vendedor Actualizado Correctamente")
        return redirect(url_for("vendedor_admin")) #redirigia a la nueva pagina
    

if __name__=="__main__":
    app.run(port=4000, debug=True)