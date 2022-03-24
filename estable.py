#Importando modulos
from flask import Flask, jsonify
from api import sistemaOp, procesos

#servidor
app = Flask(__name__)

#Ruta principal
@app.route('/', methods=['GET'])
def get_home():
    #Convertimos en json y respondemos con json
    return jsonify({"DATOS DEL SISTEMA OPERATIVO":sistemaOp, "PROCESOS CORRIENDO":procesos})

#Inicializar el servidor
if __name__ == '__main__':
    app.run(debug=True, port=8080)