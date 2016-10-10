#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):

        self.ListaDicc = []
        self.DiccAtrib = {'root-layout': ['width', 'height', 
                          'background-color'],
                          'region': ['id', 'top', 'bottom', 'left', 'rigth'],
                          'img': ['src', 'region', 'begin', 'dur'],
                          'audio': ['src', 'begin', 'dur'],
                          'textstream': ['src', 'region']}

    def startElement(self, name, attrs):

        dicc = {}

        if name in self.DiccAtrib:
            dicc = {'Tag': name}
            for atribute in self.DiccAtrib[name]:
                dicc[atribute] = attrs.get(atribute, "")
            self.ListaDicc.append(dicc)

    def get_tags(self):
        # Metodo que me imprime la lista de diccionarios
        return self.ListaDicc


if __name__ == "__main__":

    parser = make_parser()
    kHandler = SmallSMILHandler()
    parser.setContentHandler(kHandler)
    parser.parse(open('karaoke.smil'))
    Lista_Dicc = kHandler.get_tags()

    for datos in Lista_Dicc:
        print(datos)
