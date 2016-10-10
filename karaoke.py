#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
import urllib.request
import smallsmilhandler

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class KaraokeLocal():

    def __init__(self, fich):
        #Inicializar
        parser = make_parser()
        kHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(kHandler)
        parser.parse(open(fich))
        self.datos_smil = kHandler.get_tags()


    def __str__(self):
        #Escribir datos
        linea = ""
        for eti_dicc in self.datos_smil:
            etiqueta = eti_dicc['Tag']
            linea += etiqueta

            for atributo in eti_dicc:
                if atributo != 'Tag' :
                    value = eti_dicc[atributo]
                    linea += '\t' + atributo + "=" + value + '\n'
        return(linea)


    def do_json(self, fich):
        #Convertir un fichero smil en uno json
        jsonfich = json.dumps(self.datos_smil)
        nombrefich = fich.split('.')[0] + '.json'
        with open(nombrefich, 'w') as fichjson:
            json.dump(jsonfich, fichjson)


    def do_local(self):
        #Guardar en local
        for linea in self.datos_smil:
            for atributos in linea:
                if linea[atributos][:7] == 'http://':
                    url = linea[atributos].split('/')[-1]
                    urllib.request.urlretrieve(linea[atributos], url)
                    linea[atributos] = url


if __name__ == "__main__":

    fich = sys.argv[-1]
    if len(sys.argv) == 2 and fich.split('.')[-1] == 'smil':
        karaoke = KaraokeLocal(fich)
        print(karaoke)
        karaoke.do_json(fich)
        karaoke.do_local()
        print(karaoke)
    else:
        sys.exit("Usage: python3 karaoke.py file.smil")
