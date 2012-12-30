# Create your views here.
#from django.http import HttpResponse
from models import Servidor
from django.shortcuts import render

#Importamos para poder llamar a MSM
from commands import getoutput
#Importamos Regular Expressions para poder obtener info de los servidores
import re

def index(request):
    #La vista index de los servidores se encarga de recuperar el estado de los mismos y mostrarlos en forma de lista
    listaServidores = []

    lineas = getoutput("msm server list").split("\n")

    for linea in lineas:
        resultadoMsm = re.search(r'\[\s*(?P<actividad>.+)\s*\].*"(?P<nombre>.+)".+(?P<estado>stopped|running).*', linea)
        if resultadoMsm is not None:
            #Se encontraton coincidencias
            # Y armamos el objeto con los datos
            servidor = Servidor()   #Instanciamos
            servidor.nombre = resultadoMsm.group('nombre') #El nombre que el grupo de la regex encontro
            servidor.online = (resultadoMsm.group('estado') == 'running') #Si coincide con lo que la regex econtro

            #Obtenemos el puerto, dado el nombre del server (Porque conocemos donde esta su server.properties)
            with open('/opt/msm/servers/{0}/server.properties'.format(resultadoMsm.group('nombre')), 'r') as f:
                for lineaConf in f.readlines():
                    resultadoConfig = re.match(r'^server-port=(?P<puerto>\d+)$', lineaConf)
                    if resultadoConfig is not None:
                        servidor.puerto = int(resultadoConfig.group('puerto'))

            listaServidores.append(servidor)    #Lo agregamos para pasar a la plantilla...

    return render(request, 'servidores/lista.html', {'listaServidores' : listaServidores})