# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 16:54:42 2019

@author: Usuario
"""
from random import random
from Produto import Produto
from Individuo import Individuo


class AlgoritimoGenetico():
    def __init__(self,tamanho_populacao):
        self.tamanho_populacao = tamanho_populacao
        self.populacao = []
        self.geracao = 0
        self.melhor_solucaco = 0
        self.lista_solucao = []
        
    def inicializaPopulacao(self,espacos,valores,nomes,limite_espacos):
        for i in range(self.tamanho_populacao):
            self.populacao.append(Individuo(espacos,valores,nomes,limite_espacos))
            
        self.melhor_solucaco = self.populacao[0]
        
    def ordenaPopulacao(self):
        self.populacao = sorted(self.populacao,key=lambda populacao:populacao.nota_avaliacao,
                                reverse=True)
        
    def melhorIndividuo(self, individuo):
        if individuo.nota_avaliacao > self.melhor_solucaco.nota_avaliacao:
            self.melhor_solucaco = individuo
        
    
    def somaAvaliacoes(self):
        soma = 0
        for ind in self.populacao:
            soma+= ind.nota_avaliacao
        return soma
    
    def selecionaPai(self,soma_avaliacao):
        pai = -1
        valor_sorteado = random() * soma_avaliacao
        soma = 0
        i = 0
        while i < len(self.populacao) and soma < valor_sorteado:
            soma+=self.populacao[i].nota_avaliacao
            i +=  1
            pai +=1
        return pai
    
    def visualizaGeracao(self):
        melhor = self.populacao[0]
        print("Geração.: %s | Valor.: %s | Espaco.: %s Cromossomo.: %s"%(self.populacao[0].geracao,
                                                             melhor.nota_avaliacao,
                                                             melhor.espaco_usado,
                                                             melhor.cromossomo
                                                             ))
    def resolver(self,taxaMutacao,numeroGeracoes,espacos,valores,nomes,limiteEspacos):
        self.inicializaPopulacao(espacos,valores,nomes,limiteEspacos)
       
        for individuo in self.populacao:
            individuo.avaliacao()
            
        self.ordenaPopulacao()
        
        self.melhor_solucaco = self.populacao[0]
        self.lista_solucao.append(self.melhor_solucaco.nota_avaliacao)     
        self.visualizaGeracao()
        
        for geracao in range(numeroGeracoes):
            soma_avaliacao = self.somaAvaliacoes()
            nova_populacao = []
            
            for individuos_gerados in range(0,self.tamanho_populacao,2):
                pai1 = self.selecionaPai(soma_avaliacao)
                pai2 = self.selecionaPai(soma_avaliacao)
                
                filhos = self.populacao[pai1].crossover(self.populacao[pai2])
                
                nova_populacao.append(filhos[0].mutacao(taxaMutacao))
                nova_populacao.append(filhos[1].mutacao(taxaMutacao))
                
            self.populacao = list(nova_populacao)
            
            for individuo in self.populacao:
                individuo.avaliacao()
                
            self.ordenaPopulacao()
            self.visualizaGeracao()
            
            melhor = self.populacao[0]
            self.lista_solucao.append(melhor.nota_avaliacao) 
            self.melhorIndividuo(melhor)
        
        print("\n MELHOR SOLUCAO \n")
        print("\nG.: ",self.melhor_solucaco.geracao)
        print("\nV.: ",self.melhor_solucaco.nota_avaliacao)
        print("\nE.: ",self.melhor_solucaco.espaco_usado)
        print("\nC.: ",self.melhor_solucaco.cromossomo)
        
        return self.melhor_solucaco.cromossomo
            
            
        