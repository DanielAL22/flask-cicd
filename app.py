from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "¡Hola desde Flask en Raspberry Pi accesible desde internet con un dominio duckdns y actualizado con un pipeline CD!"
