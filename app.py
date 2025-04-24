from flask import Flask, render_template, request, redirect, url_for, flash
from src.gestion import GestionInventario
from src.producto import Producto

app = Flask(__name__)
app.secret_key = 'unaFraseSugerente7732'

@app.route('/')
@app.route('/index')
def index():
    """ Página principal de la aplicación"""
    productos = GestionInventario.obtener_todos()
    return render_template('index.html', productos=productos)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    """ Página para añadir productos al inventario """
    if request.method == 'POST':
        nombre = request.form['nombre']
        cantidad = int(request.form['cantidad'])
        precio = float(request.form['precio'])
        categoria = request.form['categoria']

        producto = Producto(nombre, cantidad, precio, categoria)
        resultado = GestionInventario.agregar_producto(producto)

        if resultado:
            flash("✅ Producto agregado correctamente", "success")
        else:
            flash("❌ No se pudo agregar el producto (¿nombre duplicado?)", "danger")
        return redirect(url_for('index'))

    return render_template('agregar.html')
