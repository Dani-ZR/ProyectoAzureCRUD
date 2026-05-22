from flask import Flask, render_template, request, redirect
import pyodbc

app = Flask(__name__)

conexion = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=tcp:serverestudiantesucc.database.windows.net,1433;"
    "DATABASE=DBEstudiantes;"
    "UID=admins;"
    "PWD=proyectofinalDD*;"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Connection Timeout=30;"
)

@app.route('/')
def inicio():

    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM estudiantes")

    estudiantes = cursor.fetchall()

    return render_template("index.html", estudiantes=estudiantes)

@app.route('/agregar', methods=['POST'])
def agregar():

    nombre = request.form['nombre']
    correo = request.form['correo']
    edad = request.form['edad']
    carrera = request.form['carrera']

    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO estudiantes(nombre, correo, edad, carrera)
        VALUES (?, ?, ?, ?)
    """, (nombre, correo, edad, carrera))

    conexion.commit()

    return redirect('/')

@app.route('/eliminar/<int:id>')
def eliminar(id):

    cursor = conexion.cursor()

    cursor.execute(
        "DELETE FROM estudiantes WHERE id = ?",
        (id,)
    )

    conexion.commit()

    return redirect('/')
@app.route('/editar/<int:id>')
def editar(id):

    cursor = conexion.cursor()

    cursor.execute(
        "SELECT * FROM estudiantes WHERE id = ?",
        (id,)
    )

    estudiante = cursor.fetchone()

    return render_template(
        "editar.html",
        estudiante=estudiante
    )

@app.route('/actualizar/<int:id>', methods=['POST'])
def actualizar(id):

    nombre = request.form['nombre']
    correo = request.form['correo']
    edad = request.form['edad']
    carrera = request.form['carrera']

    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE estudiantes
        SET nombre = ?,
            correo = ?,
            edad = ?,
            carrera = ?
        WHERE id = ?
    """, (nombre, correo, edad, carrera, id))

    conexion.commit()

    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)