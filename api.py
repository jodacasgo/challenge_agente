#Importando modulos 
import platform
import os
import socket
import getpass
import platform


#Informacion del sistema operativo 
sistemaOp = [platform.uname()]
procesos = [os.popen('wmic process get description, processid').read()]
nameServer=socket.gethostname()
ipServidor=  socket.gethostbyname(nameServer)
infoProcess=sistemaOp[0].processor
sessionUser=getpass.getuser()
#print(procesos, sistemaOp) 