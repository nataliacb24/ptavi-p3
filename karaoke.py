#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
import urllib

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler


#def dow_local(datos_smil):

#    for linea in datos_smil:
#        for atributo in linea.keys():
#            if atributo == "src":
#                if linea[atributo].split[':'][0] == 'http://':
#                    urllib.request.urlretrieve(linea[atributo], linea[atributo].split('/')[-1])
#                    linea[atributo] = linea[atributo].split('/')[-1]
#        print(atributo)
    
def mifichero(datos_smil):

    for eti_dicc in datos_smil:
        linea = ""
        etiqueta = eti_dicc['Tag']
        linea += etiqueta

        for atributo in eti_dicc:
            value = eti_dicc[atributo]
            linea += '\t' + atributo + "=" + value
        print(linea)


def conver_json(datos_smil):
    #Convertir un fichero smil en uno json
    smilfich = sys.argv[1]
    nombrefich = open(smilfich.split('.')[0] + '.json', 'w')
    jsonfich = json.dumps(datos_smil)
    nombrefich.write(jsonfich)
    nombrefich.close()


if __name__ == "__main__":

    try:
        smilfich = sys.argv[1]

    except IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil")

    parser = make_parser()
    kHandler = SmallSMILHandler()
    parser.setContentHandler(kHandler)
    parser.parse(open(smilfich))
    datos_smil = kHandler.get_tags()

#    dow_local(datos_smil)
    mifichero(datos_smil)
    conver_json(datos_smil)
