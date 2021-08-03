# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 10:53:46 2018

@author: Philipe Leal
"""

    
class ObjetoGrafico(object):
    def __init__(self, cor_preenchimento, cor_de_contorno):
        """
        cor_preenchimento: valor inteiro entre 0 e 255
        
        cor_de_contorno: valor inteiro entre 0 e 255
        
        """
        if cor_preenchimento < 0:
            self.cor_preenchimento = cor_preenchimento =0
        else:
            self.cor_preenchimento = cor_preenchimento
            
        if cor_de_contorno <0:
            self.cor_de_contorno = cor_de_contorno = 0
        else:
            self.cor_de_contorno = cor_de_contorno
        


class Ponto(ObjetoGrafico):
    def __init__(self, x, y, *cor):
        self.x = x
        self.y = y
        if len(cor)>1:
            
            self.cor_preenchimento = self.cor_de_contorno = cor[0]
        else:
            self.cor_preenchimento = self.cor_de_contorno = cor
            
        super(Ponto, self).__init__(*cor)
    
    def __str__(self):
        print(self.x, self.y)
        
        
class Retangulo(Ponto):
    def __init__(self, largura, altura, X_min=0, Ymin=0, cor_preenchimento=0, cor_de_contorno=0):
        
        self.largura = largura
        
        self.altura = altura
        
        super().__init__(X_min, Ymin, cor_preenchimento, cor_de_contorno) 
        
    def __str__(self):
        
        return str('({0}, {1}) \n({2}, {3})'.format(self.x, self.x+self.largura, self.y, self.y+self.altura))
    
    def __getattr__(self, name):
        
        return str(self.name)
    
    
class Circulo(Ponto):
    def __init__(self, X, Y, Raio):
        super().__init__(X, Y)
        
        if Raio >0:
            self.Raio = Raio
            
        else:
            self.Raio = input("Insira um raio maior que zero: ")
        
        
        
Ret = Retangulo(2,2, 2,3, 4,5)

Ret.cor_de_contorno
