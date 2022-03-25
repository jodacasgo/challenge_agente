#Importando modulos
from api import sistemaOp, procesos, ipServidor, infoProcess, sessionUser, nameServer
import requests

def getInfoMachine():
    urlApi = "http://127.0.0.1:8000/meli"
    payload = {
        "id": 1,
        "ipServidor": str(ipServidor),
        "infoProcess": str(infoProcess),
        "sessionUser": str(sessionUser),
        "nameServer": str(nameServer),
        "systemOper": str(sistemaOp),
        "processRun": str(procesos),
    }
    
    r = requests.post(urlApi, json=payload, headers= {'content-type': 'application/json'})
    if(r.status_code == requests.codes.ok):
        print(r.json())
    else:
        print("Hubo un error procesando la peticion")

getInfoMachine()