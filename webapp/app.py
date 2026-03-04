from flask import Flask, render_template, request, redirect, url_for, session, flash
import requests
import os
from datetime import datetime

# Configurar la aplicación Flask
app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'clave-por-defecto-cambiar')

# Configurar la URL de la API
API_URL = os.getenv('API_URL', 'http://api:8000')

@app.route('/')
def index():
    # Implementar página principal
    # Obtener productos destacados de la API
    return render_template('index.html')

@app.route('/products')
def products():
    # Implementar página de productos
    # Obtener lista de productos de la API
    try:
        response = requests.get(f"{API_URL}/api/v1/products/")
        if response.status_code == 200:
            products_list = response.json()
        else:
            products_list = []
    except:
        products_list = []
    return render_template('products.html', products=products_list)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Implementar lógica de login
        # Enviar datos a la API de autenticación
        pass
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Implementar lógica de registro
        # Enviar datos a la API de registro
        pass
    return render_template('register.html')

@app.route('/cart')
def cart():
    # Implementar página del carrito
    # Obtener carrito del usuario de la API
    return render_template('cart.html')

@app.route('/add-to-cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    # Implementar agregar producto al carrito
    # Enviar request a la API
    pass

@app.route('/logout')
def logout():
    # Implementar logout
    # Limpiar sesión
    session.clear()
    return redirect(url_for('index'))

# Función helper para hacer requests a la API
def api_request(endpoint, method='GET', data=None, headers=None):
    # Implementar función para hacer requests a la API
    url = f"{API_URL}{endpoint}"
    try:
        if method == 'GET':
            response = requests.get(url, headers=headers)
        elif method == 'POST':
            response = requests.post(url, json=data, headers=headers)
        elif method == 'PUT':
            response = requests.put(url, json=data, headers=headers)
        elif method == 'DELETE':
            response = requests.delete(url, headers=headers)
        return response
    except Exception as e:
        return None

# Función para verificar si el usuario está logueado
def is_logged_in():
    # Verificar si hay sesión activa
    return 'user_id' in session

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
