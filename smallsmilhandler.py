#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):

        self.root_layout = {}
        self.region = {}
        self.img = {}
        self.audio = {}
        self.textstream = {}
        self.ListaDicc = []

    def startElement(self, name, attrs):

        if name == 'root-layout':
            self.root_layout = {'Tag': 'root-layout',
                                'width': attrs.get('width',""),
                                'height': attrs.get('height', ""),
                                'background-color': attrs.get('background-color',"")}
            self.ListaDicc.append(self.root_layout)

        elif name == 'region':
            self.region = {'Tag': 'region',
                           'id': attrs.get('id',""),
                           'top': attrs.get('top', ""),
                           'bottom': attrs.get('bottom', ""),
                           'left': attrs.get('left', ""),
                           'rigth': attrs.get('right', "")}
            self.ListaDicc.append(self.region)

        elif name == 'img':
            self.img = {'Tag': 'img',
                        'src': attrs.get('src', ""),
                        'region': attrs.get('region', ""),
                        'begin': attrs.get('begin',""),
                        'dur': attrs.get('dur',"")}
            self.ListaDicc.append(self.img)

        elif name == 'audio':
            self.audio ={'Tag': 'audio',
                         'src': attrs.get('src',""),
                         'begin': attrs.get('begin',""),
                         'dur': attrs.get('dur',"")}
            self.ListaDicc.append(self.audio)

        elif name == 'textstream':
            self.textstream = {'Tag': 'teststream',
                               'src': attrs.get('src',""),
                               'region': attrs.get('region',"")}
            self.ListaDicc.append(self.textstream)

    def get_tags(self):
    #Metodo que me imprime la lista de diccionarios
        return self.ListaDicc


if __name__ == "__main__":

    parser = make_parser()
    kHandler = SmallSMILHandler()
    parser.setContentHandler(kHandler)
    parser.parse(open('karaoke.smil'))
    Lista_Dicc = kHandler.get_tags()

    for datos in Lista_Dicc:
        print(datos)
