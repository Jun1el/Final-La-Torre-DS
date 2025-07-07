from flask import Flask
app = Flask(__name__)
# definimos una ruta para el microservicio y poder conectar con la app legacy 
@app.route("/")
def home():
    return "Hola este es el nuevo microservicio"

if __name__ == "__main__":
    # Iniciamos la app Flask en el puerto 8000
    app.run(host="0.0.0.0", port=8000)
