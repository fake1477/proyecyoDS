from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
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
def index():
    return render_template("index.html")

@app.route("/cliente/")
def cliente():
    return render_template("cliente.html")

#@app.route("/signup_cliente",methods=["POST"])
#def signup_post_cliente():
 #       nom = request.form.get("nombres")
  #      dis = request.form.get("distrito")
   #     direc = request.form.get("direccion")
    #   em = request.form.get("email")
     #   cel = request.form.get("telefono")
      #  contra = request.form.get("contraseña")



@app.route("/cuenta/")
def cuenta():
    cur = mysql.connection.cursor()
    cur.execute("select * from cliente")
    data = cur.fetchall()
    return render_template("cuenta.html", cliente=data)

@app.route("/add_registro_cliente", methods=["POST"])
def add_registro_cliente():
        if request.method == "POST":
            nom = request.form["nombres"]
            dis = request.form["distrito"]
            direc = request.form["direccion"]
            em = request.form["email"]
            cel = request.form["telefono"]
            contra = request.form["contraseña"]
            
            cur2 = mysql.connection.cursor()
            cur2.execute("select email from cliente")
            clientes = cur2.fetchall()

            cur3 = mysql.connection.cursor()
            cur3.execute("select email from vendedor")
            vendedores = cur3.fetchall()
            em_cliente=None
            em_vendedor=None
            
            #print(str(users))
            #for email in users :
             #   if (email[0] == em):
              #      print("correo existe")
               #     return "El correo ya existe"
            
            for email in clientes :
                if (email[0] == em):
                    em_cliente = email[0]
            for email2 in vendedores:
                if (email2[0] == em):
                    em_vendedor = email2[0]

            if em_cliente == em or em_vendedor == em:
                print("elige otro correo")             
                return redirect(url_for("cliente"))

            print("INSERT", id, nom, dis, direc, em, cel, contra)
            cur = mysql.connection.cursor()
            cur.execute("insert into cliente(nombres, distrito, direccion, email, telefono, contrasena) values(%s,%s,%s,%s,%s,%s)", (nom, dis, direc, em, cel, contra))
            mysql.connection.commit()
            flash("Contacto Insertado Correctamente")
            return redirect (url_for("index"))
        return "cliente"


@app.route("/vendedor/")
def vendedor():
    return render_template("vendedor.html")

@app.route("/add_registro_vendedor", methods=["POST"])
def add_registro_vendedor():
        if request.method == "POST":
            nom2 = request.form["nombres"]
            ruc = request.form["RUC"]
            dis2 = request.form["distrito"]
            direc2 = request.form["direccion"]
            em2 = request.form["email"]
            cel2 = request.form["telefono"]
            contra2 = request.form["contraseña"]
#validando correo
            cur2 = mysql.connection.cursor()
            cur2.execute("select email from cliente")
            clientes = cur2.fetchall()

            cur3 = mysql.connection.cursor()
            cur3.execute("select email from vendedor")
            vendedores = cur3.fetchall()
            em_cliente=None
            em_vendedor=None    
            for email in clientes :
                if (email[0] == em2):
                    em_cliente = email[0]
            for email2 in vendedores:
                if (email2[0] == em2):
                    em_vendedor = email2[0]

            if em_cliente == em2 or em_vendedor == em2:
                print("elige otro correo")    
                flash("Use otro correo porfavor")         
                return redirect(url_for("vendedor"))


            print("INSERT", id, nom2, ruc, dis2, direc2, em2, cel2, contra2)
            cur = mysql.connection.cursor()
            cur.execute("insert into vendedor(nombres, RUC, distrito, direccion, email, telefono, contrasena) values(%s,%s,%s,%s,%s,%s,%s)", (nom2, ruc, dis2, direc2, em2, cel2, contra2))
            mysql.connection.commit()
            return redirect (url_for("index"))
        return "vendedor"


@app.route("/login", methods=[ "POST"])
def login():
    if request.method == "POST":
        em2 = request.form["email"]
        contra2 = request.form["contraseña"]
        print ("usuario ",em2, contra2)
        cur = mysql.connection.cursor()
        cur2 = mysql.connection.cursor()
        #cur2 = mysql.connection.cursor()
        #cur3 = mysql.connection.cursor()
        #cur.execute("select id from cliente where email = %s",{em2})
        #id_user = cur.fetchall()[0][0]
        #datos del usuario
        query = "select email, contrasena from cliente ;"
        cur.execute(query)
        clientes = cur.fetchall() 

        query2 = "select email, contrasena from vendedor ;"
        cur2.execute(query2)
        vendedores = cur2.fetchall() 
        #where email = %s and contrasena = %s",{em2,contra2})        
        email=None
        contrasena=None
        email2=None
        contrasena2=None

        for email_, contrasena_ in clientes:
            if email_ == em2 and contrasena_ == contra2:
                email = email_
                contrasena = contrasena_
                print (email," **", contrasena)
        
        for email2_, contrasena2_ in vendedores:
            if email2_ == em2 and contrasena2_ == contra2:
                email2 = email2_
                contrasena2 = contrasena2_
                print (email2," **", contrasena2)




        #print(usuario, contraseña)
        if (email == em2 and contrasena == contra2) or (email2 == em2 and contrasena2 == contra2):
            print("correcto", email, "** ", contrasena)
            return "datos correctos"
            flash("datos correctos")

        else:
            return "Contraseña incorrecta"
            flash("usuario no existente")
         





if __name__=="__main__":
    app.run(port=3000, debug=True)