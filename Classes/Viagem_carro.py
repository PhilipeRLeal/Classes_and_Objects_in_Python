# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 13:57:31 2017

@author: Philipe Leal
"""

class Carro():
    
    def __init__(self, Marca, 
                 Volume_combustivel_tanque, 
                 Volume_max_tanque, 
                 eficiencia):
        
        self.Marca = str(Marca)
        self.Volume_combustivel_tanque = Volume_combustivel_tanque
        self.Volume_max_tanque = Volume_max_tanque
        self.eficiencia = eficiencia
        
    def locomocao(self, distancia_de_percurso):
        self.distancia_de_percurso = distancia_de_percurso
        if float(self.Volume_combustivel_tanque -(distancia_de_percurso/self.eficiencia))>0:

            self.Volume_combustivel_tanque = float(self.Volume_combustivel_tanque - 
                                                  (distancia_de_percurso/self.eficiencia))
            
        elif (float(self.Volume_combustivel_tanque -(distancia_de_percurso/self.eficiencia))) == 0:
            return 
            "Se viajar esta distancia, o combustivel acabara completamente."
            if input("Gostaria de adicionar mais combustivel (sim, nao)?: ") == "sim":    
                Litros = input("Quantos litros deverao ser postos?: ")
                self.Volume_combustivel_tanque = float(self.Volume_combustivel_tanque + Litros)
                print("Combustivel final no tanque: %f5.2 " % self.Volume_combustivel_tanque)
                
class Posto():
    def __init__(self, Nome, preco_Litro_combustivel):
        self.Nome = Nome
        self.preco_Litro_combustivel = preco_Litro_combustivel
        
    def Encher_combustivel(self, litros_a_encher):
        if self.Volume_combustivel_tanque == self.Volume_max_tanque:
            self.Litros_a_encher = 0
            
        else:
             self.Litros_a_encher =  self.Litros_a_encher
             self.Custo_de_abastecimento = self.Litros_a_encher * self.preco_Litro_combustivel
             
class Motorista():
    def __init__ (self, Nome):
        self.Nome = Nome
    
    def Viagem_de_carro(self, distancia_de_percurso_desejada):
        self.Volume_de_combustivel_requerida_por_viagem = (distancia_de_percurso_desejada/Carro.eficiencia())
        if self.Volume_combustivel_tanque > self.Volume_de_combustivel_requerida_por_viagem: 
            return ("Viagem concluida com sucesso")
            print("Sobraram %f5.2 " % self.Volume_combustivel_tanque)
            
        else:
            print("Antes de concluir o percurso, eh necessario abastecer o carro.")
            Decisao = input("Gostaria de abastecer o carro (sim, nao)?: ")
            if Decisao == "sim":
                print("Viagem concluida com sucesso")
                    
            else: 
                print("O carro pararah")
        
        
        
    