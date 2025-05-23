from flask import Flask, request, jsonify, render_template, redirect
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

mascotas = []

@app.route('/')
def inicio():
    return render_template('index.html')

# Ruta para registrar mascota (GET muestra formulario, POST procesa)
@app.route('/registro', methods=['GET', 'POST'])
def registrar_mascota():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        especie = request.form.get('especie')
        raza = request.form.get('raza')
        edad = request.form.get('edad')
        
        if not nombre or not especie or not raza or not edad:
            return "Faltan datos", 400

        mascota = {
            'nombre': nombre,
            'especie': especie,
            'raza': raza,
            'edad': edad
        }
        mascotas.append(mascota)
        
        return redirect('/lista')

    # Si es GET mostrar el formulario
    return render_template('formulario.html')

@app.route('/lista', methods=['GET'])
def lista_mascotas():
    return render_template('lista.html', mascotas=mascotas)

@app.route('/dashboard')
def dashboard():
    total = len(mascotas)
    return render_template('dashboard.html', total=total)

if __name__ == '__main__':
    app.run(debug=True)
