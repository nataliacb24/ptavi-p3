#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
import urllib
import smallsmilhandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class KaraokeLocal():

    def inicializador(self, fich):
    
        parser = make_parser()
        self.kHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(self.kHandler)
        parser.parse(open(fich))
        self.datos_smil = self.kHandler.get_tags()


    def __str__(self):

        for eti_dicc in self.datos_smil:
            linea = ""
            etiqueta = eti_dicc['Tag']
            linea += etiqueta

            for atributo in eti_dicc:
                value = eti_dicc[atributo]
                linea += '\t' + atributo + "=" + value
            print(linea)


    def to_json(self, fich):
        #Convertir un fichero smil en uno json
        jsonfich = json.dumps(self.datos_smil)
        nombrefich = fich.split('.')[0] + '.json'
        with open(jsonfich, 'w') as fichjson:
            json.dump(jsonfich, fichjson)
    
    #def do_local(self, datos_smil):

    #    for linea in self.datos_smil:
    #        for atributo in linea.keys():
    #            if atributo == "src":
    #                if linea[atributo].split[':'][0] == 'http://':
    #                    urllib.request.urlretrieve(linea[atributo], linea[atributo].split('/')[-1])
    #                    linea[atributo] = linea[atributo].split('/')[-1]
    #        print(atributo)


if __name__ == "__main__":
                   
    try:
        fich = sys.argv[1]

    except IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil")
    
    karaoke = KaraokeLocal()
    karaoke.inicializador(fich)
    #print(karaoke)
    karaoke.to_json(fich)
#   karaoke.do_local()
