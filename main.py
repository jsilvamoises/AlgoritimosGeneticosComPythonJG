# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 14:32:15 2019
conda install pymysql
@author: Usuario
"""
import pymysql
from Produto import Produto
from Individuo import Individuo
from algoritmo_genetico import AlgoritimoGenetico

import matplotlib.pyplot as plt

if __name__ == "__main__":
    #p1 = Produto(nome="Iphone 6",espaco=0.0000899,valor=2199.12)
    
    lista_produtos = []
    
    conexao = pymysql.connect(host="localhost",user="root", passwd="1982",db="ag")
    cursor = conexao.cursor()
    cursor.execute("SELECT nome,espaco,valor,quantidade FROM PRODUTOS")
    
    # LISTA DE ITENS DO BANDO
    for produto in cursor:
        quantidade = produto[3]
        for i in range(quantidade):
            p = Produto(produto[0],produto[1],produto[2])
            lista_produtos.append(p)
    
    cursor.close()
    conexao.close()
    
    
    """
    lista_produtos.append(Produto(nome="Geladeira Dako",espaco=0.751,valor=999.99))
    lista_produtos.append(Produto(nome="Iphone 6",espaco=0.0000899,valor=2911.12))
    lista_produtos.append(Produto(nome="TV 55",espaco=0.400,valor=4346.99))
    lista_produtos.append(Produto(nome="TV 58",espaco=0.290,valor=3999.90))
    lista_produtos.append(Produto(nome="Notebook Dell",espaco=0.00350,valor=2490.90))
    lista_produtos.append(Produto(nome="Ventilador Panasonic",espaco=0.496,valor=199.90))
    lista_produtos.append(Produto(nome="Microondas Eletrolux",espaco=0.0424,valor=309.66))
    lista_produtos.append(Produto(nome="Microondas LG",espaco=0.0544,valor=429.90))
    lista_produtos.append(Produto(nome="Microondas Panasonic",espaco=0.0319,valor=299.29))
    lista_produtos.append(Produto(nome="Geladeira Brastemp",espaco=0.635,valor=849.00))
    lista_produtos.append(Produto(nome="Geladeira Consul",espaco=0.870,valor=1199.89))
    lista_produtos.append(Produto(nome="Notebook Lenovo",espaco=0.498,valor=1999.99))
    lista_produtos.append(Produto(nome="Notebook Asus",espaco=0.527,valor=3999.99))
    """
    
    
    
    #for produto in lista_produtos:
    #    print(produto.toString())
    
    espacos = []
    valores = []
    nomes =   []
    
    for produto in lista_produtos:
        espacos.append(produto.espaco)
        valores.append(produto.valor)
        nomes.append(produto.nome)
        
    limite = 10   
    tamanho_populacao = 100
    taxa_mutacao = 0.01
    numero_geracaoes = 2000
    
    # CRIA ALGORITMO GENÉTICO
    ag = AlgoritimoGenetico(tamanho_populacao)
    
    resultado = ag.resolver(taxa_mutacao,numero_geracaoes,espacos,valores,nomes,limite)
    
    for i in range(len(lista_produtos)):
        if resultado[i] == "1":
            print("Nome..: ",lista_produtos[i].nome)
            print("Valor.:",lista_produtos[i].valor)
            print("="*30)
            
    #for valor in ag.lista_solucao:
    #    print(valor)
    
    plt.plot(ag.lista_solucao)
    plt.title("Acompanhamentos dos valores")
    plt.show()
    

   
    
   
    