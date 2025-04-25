from flask import Flask, render_template, request, redirect, url_for, flash
from src.gestion import GestionInventario
from src.producto import Producto

app = Flask(__name__)
app.secret_key = 'frase_secreta_para_cambiar_de_informacion'

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

@app.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    resultado = GestionInventario.eliminar_producto(id)
    if resultado:
        flash("🗑️ Producto eliminado correctamente", "success")
    else:
        flash("❌ Error al eliminar el producto", "danger")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()