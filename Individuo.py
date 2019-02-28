# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 14:55:50 2019

@author: Usuario
"""
from random import random

class Individuo():
    def __init__(self,espacos,valores,nomes, limite_espacos,geracao=0):
        self.espacos = espacos
        self.valores = valores
        self.limite_espacos = limite_espacos
        self.geracao = geracao;
        self.nota_avaliacao = 0
        self.geracao = geracao
        self.nomes = nomes
        self.cromossomo = []
        self.espaco_usado = 0
        
        self.initCromossomo()
    # =======================================    
    def initCromossomo(self):
        for i in range(len(self.espacos)):
            if(random() < 0.5):
                self.cromossomo.append("0")
            else:
                self.cromossomo.append("1")
    # =======================================           
    def avaliacao(self):
        nota = 0
        soma_espacos = 0
        
        for i in range(len(self.cromossomo)):
             if self.cromossomo[i] == "1":
                 nota += self.valores[i]
                 soma_espacos += self.espacos[i]
        if soma_espacos > self.limite_espacos:
            nota = 1
        self.nota_avaliacao = nota
        self.espaco_usado = soma_espacos
    # =======================================
    def printResultAvalicacao(self):
        print("Nota.........: %s"%self.nota_avaliacao)
        print("Espaco Usado.: %s"%self.espaco_usado)
    # =======================================    
    def crossover(self,outro_individuo):
        corte = round(random() * len(self.cromossomo))
        
        filho1 = outro_individuo.cromossomo[0:corte] + self.cromossomo[corte::]
        filho2 =  self.cromossomo[0:corte] + outro_individuo.cromossomo[corte::]
        
        filhos = [
                Individuo(self.espacos,self.valores,self.nomes,self.limite_espacos,self.geracao + 1),
                Individuo(self.espacos,self.valores,self.nomes,self.limite_espacos,self.geracao + 1)
                ]
        
        filhos[0].cromossomo = filho1
        filhos[1].cromossomo = filho2
        
        return filhos
    # =======================================
    def mutacao(self,taxa_mutacao):
        #print("Antes da Mutacao    %s"%self.cromossomo)
        for i in range(len(self.cromossomo)):
            if random() < taxa_mutacao:
                if self.cromossomo[i] == "1":
                    self.cromossomo[i] = "0"
                else:
                    self.cromossomo[i] = "1"
        #print("Depois da mutaçaõ   %s"%self.cromossomo)
        return self
    # =======================================           
    def printValues(self):       
        print("valor....:",self.valores)
        print("Espaçoes.:",self.espacos)
        print("Cromossomo:",self.cromossomo)
    # =======================================    
    def printComponentsCarga(self):
        for i in range(len(self.cromossomo)):
            if self.cromossomo[i] == "1":
                print(self.nomes[i]," Valor.: ",self.valores[i])
        
        
        
        

