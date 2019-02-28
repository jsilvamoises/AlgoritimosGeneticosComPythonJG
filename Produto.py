# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 13:52:11 2019

@author: Usuario
"""

class Produto():
    def __init__(self, nome,espaco,valor):
        self.nome = nome
        self.espaco = espaco
        self.valor = valor
        
    def toString(self):
        print("Nome: {}, Espaço:{}, Valor: {}".format(self.nome,self.espaco,self.valor))
        
