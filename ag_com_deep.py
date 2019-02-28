# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 22:35:40 2019
pip install deap
@author: Usuario
"""

import pymysql
from Produto import Produto
from Individuo import Individuo

import matplotlib.pyplot as plt


from deap import base
from deap import creator
from deap import algorithms
from deap import tools
import numpy
import random

class AgDeep():
    def __init__(self):
        self.limite = 10
        self.espacos = []
        self.valores = []
        self.nomes =   []
        self.lista_produtos = []
        self.toolbox = base.Toolbox()   
        self.populationSize=1000
        self.probabilidadeCrossover = 1.0
        self.probabilidadeMutacao = 0.01
        self.numeroGeracoes = 1000

    def process(self):
        #random.seed(2)
        self.loadData()
        self.initNeural(self.lista_produtos)
        
        populacao = self.toolbox.population(n = self.populationSize)
        
        
        
        
        estatisticas = tools.Statistics(key=lambda individuo: individuo.fitness.values)
        estatisticas.register("max",numpy.max)
        estatisticas.register("min",numpy.min)
        estatisticas.register("mean",numpy.mean)
        estatisticas.register("desvio padrao",numpy.std)
        
        #3population, toolbox, cxpb, mutpb, ngen, stats=None,halloffame=None, verbose=__debug__
        populacao, info = algorithms.eaSimple(population=populacao,
                                              toolbox=self.toolbox,
                                              cxpb=self.probabilidadeCrossover,
                                              mutpb=self.probabilidadeMutacao,
                                              ngen=self.numeroGeracoes,
                                              stats=estatisticas) 
        
        melhores = tools.selBest(populacao,1)
        
        for individuo in melhores:
            print("INDIVIDUO.: ",individuo)
            print("FITENESS..: ",individuo.fitness)
            
            soma = 0
            for i in range(len(self.lista_produtos)):
                if individuo[i] == 1:
                    soma += self.lista_produtos[i].valor
                    print("Nome>> %s R$ %.2f "%(self.lista_produtos[i].nome,
                                              float(self.lista_produtos[i].valor)))
                    
            print("Melhor Solução %.2f"% soma)
            
        valores_grafico = info.select("max")
       
        plt.plot(valores_grafico)
        plt.title("Acompanhamento dos valores")
        plt.show()
            
        
        
        
            
    def loadData(self):
        conexao = pymysql.connect(host="localhost",user="root", passwd="1982",db="ag")
        cursor = conexao.cursor()
        cursor.execute("SELECT nome,espaco,valor,quantidade FROM PRODUTOS")
        
        # LISTA DE ITENS DO BANDO
        for produto in cursor:
            quantidade = produto[3]
            for i in range(quantidade):
                p = Produto(produto[0],produto[1],produto[2])
                self.lista_produtos.append(p)
        
        cursor.close()
        conexao.close()
        
        
        
        for produto in self.lista_produtos:
            self.espacos.append(produto.espaco)
            self.valores.append(produto.valor)
            self.nomes.append(produto.nome)
        
        
    def initNeural(self,lista_produtos):
        
        creator.create("FitnessMax",base.Fitness, weights=(1.0,))
        creator.create("Individual",list,fitness=creator.FitnessMax)
        self.toolbox.register("attr_bool",random.randint,0,1)
        self.toolbox.register("individual",tools.initRepeat,creator.Individual,self.toolbox.attr_bool,n=len(lista_produtos))
        
        self.toolbox.register("population",tools.initRepeat,list,self.toolbox.individual)
        self.toolbox.register("evaluate",self.avaliacao)
        self.toolbox.register("mate",tools.cxOnePoint)
        self.toolbox.register("mutate",tools.mutFlipBit, indpb=0.1)
        self.toolbox.register("select",tools.selRoulette)
        
    def avaliacao(self,individual):
        nota = 0
        soma_espacos = 0
        for i in range(len(individual)):
            if individual[i] == 1:
                nota += self.lista_produtos[i].valor
                soma_espacos += self.lista_produtos[i].espaco
        if soma_espacos > self.limite:
            nota = 1
            
        return nota / 100000,
                
    
ag = AgDeep()
ag.process()