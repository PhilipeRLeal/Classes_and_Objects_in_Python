# -*- coding: utf-8 -*-
"""
Created on Tue May  8 14:16:04 2018

@author: Philipe Leal
"""

import numpy as np

A = np.random.rand(5, 5)

def add_100(array):
    array = array + 100
    
    return array

B = np.vectorize(add_100)

C = B(A)


### ---------------------------- ###

# Flux = K_gas * ([gas_med] - [gas_equi])

    # K_gas = K_600 * (Sc_gas_temperatura/600)**N

    # N: varia entre 1 e -0.67.
        # padrão: N = (-0.67)
        
    # K600 = 2.07 + 0.215*U**1.7
    
        # U: velo do vento (m/s) a 10m de altura do alvo
        
    # Sc_gas_temperatura: [0:inf]
        # valor de a 25°C: Sc_CO2_25C = 468

    
class Liberacao_gas_dagua_para_Atm ():
    def __init__(self, conc_gas, conc_eq_gas, N_gas=None, K600_gas=None, Funcao_K_gas=None, U=None, Sc_gas_temp=None, Temperatura=None, Z_mix=None, Dia_jul=None, Lat=None, Horario_medida_OD=None, Respiration_hora=None):
        """
            Algoritmo criado a partir de Hu et al. (2015).
            Vide referência completa:
                
            ''' HU, Z. et al. Temporal dynamics and drivers 
                of ecosystem metabolism in a large subtropical 
                Shallow Lake (Lake Taihu). 
                International Journal of Environmental 
                Research and Public Health, 
                v. 12, n. 4, p. 3691–3706, 2015. ''' 
        
        
        
            conc_gas: concentração do gas na água
            
            conc_eq_gas: concentração de equilíbrio do gas (água-ar)
            
            N_gas: coeficiente de difusibiilidade do gas
                1) N_gas é específico por temperatura e por gas
                2) N_gas varia entre: [-067:1]
                3) caso N_gas não seja definido, N_gas = -0.67
    
            K600_gas: coeficiente de difusibilidade do gas. 
            
            K600_gas pode ser definido pelo usuário de duas formas:
                1) um valor (float) definido pelo usuário
                2) uma funcao (callable) do vento definido pelo usuário. Neste caso, o valor de U deverá ser informado pelo usuário
            
            Funcao_K_gas: funcao de conversão do K600_gas em K_gas:
                Pode ser definido pelo usuário como uma função, ou deixar como padrão.
                Funcao_K_gas padrão é calculado a partir de ...
                
                
            U: velocidade do vento.
                Obs: U deverá ser informado caso K600_gas seja uma função!!
                
            Sc_gas_temp: coeficiente Sc. É específico de gás para gás, e por temperatura.
            Sc_gas_temp pode ser definido pelo usuário como:
                1) um valor definido pelo usuário
                2) deixado em None (valor nominal), Sc_gas_temp=468.0,
                3) Estipulado pela equação de Wanninkhof (1992)
                    # ref: Wanninkhof, R. Relationship between wind speed and gas exchange over the ocean. J. Geophys. Res. 1992, 97, 7373–7382
            
            Quando Sc_gas_temp é estipulado conforme equação de Wanninkhof, 
                utilizar: Sc_gas_temp= 'Wanninkhof'
                Definir também a temperatura.
            
            Temperatura: temperatura do alvo para cálculo da equação de Wanninkhof (1992)
                Somente aplicada quando Sc_gas_temp = 'Wanninkhof'
                
            Z_mix: zona de mistura. Valor obrigatório para cálculo da GPP e da NPP (denominado NEP por Hu et al. (2015))
                Z_mix padrão: Z_mix=None
                
            Dia_jul: dia juliano. Obrigatório para cálculo de NEP e GPP:
                
            Lat: latitude. Obrigatório para cálculo de NEP e GPP:
            
            Horario_medida_OD: horário em 24h da medida em OD.Obrigatório para cálculo de NEP e GPP:
        
            Respiration_hora: taxa de respiração da comunidade em [oxigênio respirado]/hora                
                Respiration_hora é Obrigatório para cálculo de NEP e GPP:
        """
        
        self.conc_gas = conc_gas
        self.conc_eq_gas = conc_eq_gas
        self.N_gas = N_gas
        self.U = U
        self.Sc_gas_temp = Sc_gas_temp

        self.Flux_gas = None
        if self.N_gas == None:
            self.N_gas = -0.67
            
        else: 
            self.N_gas = self.N_gas
        
        
        self.K600_gas = K600_gas
               
        if self.K600_gas is None:
            print("funcao_K600_gas não definida pelo usuário!")
            print("Utilizando funcao_K600_gas do CO2 conforme ...")
            
            if self.U != None:
               print("U definido corretamente. Seguindo com os cálculos!")
                
                
               self.K600_gas = 2.07 + (0.215*(self.U**1.7))
               
            else:
               print("Erro!\nK600_gas não definido e U não definido")
                
        elif type(float(self.K600_gas)) == type(2.0):
            print("K600_gas definida corretamente pelo usuário")
            self.K600_gas = self.K600_gas
            
              
        elif callable(self.K600_gas) is True:
            print("Checando se U foi definida")
            
            if self.U != None:
                print("U definido corretamente. Seguindo com os cálculos!")
                
                self.K600_gas = self.K600_gas
            
            else:
                print("Faltou definir U.\nSe K600_gas é uma funcao definida pelo usuário, \nU deve ser informado pelo usuário")
                
                
        else:
            
            print("funcao_K600_gas mal definida pelo usuário!")
            print("Adotando funcao_K600_gas do CO2 conforme ...")
            
            if self.U != None:
                print("U definido corretamente. Seguindo com os cálculos!")
                
            
                self.K600_gas = 2.07 + (0.215*(self.U**1.7))
                
            else:
                print("Erro!\nFuncao_K600_gas mal definida, e U não foi definido.")
        
        
        # definindo Funcao_K_gas:
        
        self.Funcao_K_gas = Funcao_K_gas
        
        # definindo Temperatura:
        
        self.Temperatura = Temperatura
        
        # para Calculo de GPP e NEP:
        
            # definindo self.Sc_gas_temp com base na equação de Wanninkhof (1992):
        
            # definindo Z_mix para eventual cálculo de NPP (NEP) e GPP:
        
        self.Z_mix = Z_mix
        
        if self.Sc_gas_temp.lower()[0] == 'w':
            print("\nUtilizando a funcao de Wanninkhof (1992)\n")
            
            if self.Temperatura == None:
                print("\n\n")
                print("Problemas")
                print("Faltou definir a temperatura para calcular Sc_gas_temp a partir de Wanninkhof (1992)")
            
            else:
                T= float(self.Temperatura)
                self.Sc_gas_temp = 1800.6 - (120.1 * (T)) + (3.7818 *(T**2)) - (0.0476 * (T**3))
        
        elif isinstance(float(self.Sc_gas_temp),float):
            self.Sc_gas_temp = self.Sc_gas_temp
        
        else:
            self.Sc_gas_temp = 468.0
        
        # definindo dia juliano:
        
        self.Dia_jul = Dia_jul
        
        self.Lat = Lat
        
        self.Horario_medida_OD = Horario_medida_OD
        
        self.Respiration_hora = Respiration_hora
        
    def funcao_K_gas (self):
        if callable(self.Funcao_K_gas) == False:
            N_gas = self.N_gas
            Sc_gas_temp = self.Sc_gas_temp
            
            K600_gas = self.K600_gas
            self.K_gas = K600_gas * ((Sc_gas_temp/600.0)**(N_gas))
            
        
        elif callable(self.funcao_K_gas) == True:
            
            self.K_gas = self.funcao_K600_gas(self.U)

        else:
            
            print("Problemas no calculo de K_gas")
            
        return self.K_gas
            
    def Flux(self):
        try:
            self.Flux_gas = self.K_gas * (self.conc_gas - self.conc_eq_gas)
        except:
            print("Self Flux nao calculado")
        if np.shape(self.Flux_gas) != (1):
            Dict = {"K_gas":self.funcao_K_gas(), 
                    "[gas]":self.conc_gas, 
                    "[gas_eq]":self.conc_eq_gas}
            import matplotlib.pyplot as plt
            plt.figure(figsize=(8,8))
            plt.imshow(self.Flux_gas)
            plt.colorbar()
            plt.show()
            
        else:
            Dict = {"K_gas":self.funcao_K_gas(), 
                    "[gas]":self.conc_gas, 
                    "[gas_eq]":self.conc_eq_gas,
                    "Fluxo gas": self.Flux_gas}
            
            
        for key,value in Dict.items():
            print (key,": ", value)
            print()
        
     
        
       
        return self.Flux_gas
    
    def Fracao_horas_fotossinteticas(self):
        
        pi=3.1415926535
        latr=(lat/180.)*pi
        date=(self.Dia_jul/365.)*2*pi
        soldec=((0.39637-22.9133*cos(date)+4.02543*sin(date)-
                 0.3872*cos(2*(date))+0.052*sin(2*(date)))*pi)/180.0
        rt=-tan(latr)*tan(soldec)
        DLength = (24*acos(rt))/pi
        DLength(rt>1) =0
        DLength(rt<=-1)=24
        
        self.DLength = DLength
        
        self.Fracao_H_fotossinteticas = DLength/24.0

        
        return self.Fracao_H_fotossinteticas
    
    def NEP_hr (self):
        """ funcao de permite calcular a produtividade primária horária do ambiente
        Unidade: g O2·m−3·h−1
        """
        F = self.Flux()
        
        self.NEP_hour = (self.conc_gas - self.conc_eq_gas) - (F * self.Z_mix)
        
        
        return self.NEP_hour
    
    def NEP_dia(self):
        
        Fracao_horas_fotossinteticas(self)

        H_noite = 24 - self.DLength
        
        Nascer_sol = H_noite / 2
        
        Max_sol = Nascer_sol + (self.DLength/2)
        
        
        if self.Horario_medida_OD > 12:
            self.Horario_medida_OD -= 12
            
        else:
            self.Horario_medida_OD = self.Horario_medida_OD
        
        Taxa_horaria_potencial = self.Horario_medida_OD / Max_sol
        
        self.NEP_dia_max = (self.NEP_hour/Taxa_horaria_potencial)
        
        self.NEP_dia_medio = self.NEP_dia_max/2
        
        
        return self.NE_dia_medio
    
    def GPP (self):
        
        self.Respiration_dia = Respiration_hora * 24
        
        self.GPP = self.NEP_dia_medio - self.Respiration_dia
        
        return self.GPP
       
        
        
        
        
        
        
# caso 1:
        
Concen_CO2 = np.random.rand(2,2)

Concen_eq = 0.8

N = -0.18

U = 10

K_600 = 2.07*(0.215*(U**1.7))

Sc=468.0


 
Flux1 = Liberacao_gas_dagua_para_Atm(Concen_CO2, Concen_eq,N, K_600, None, U,Sc, None)           
          
print(Flux1.funcao_K_gas())

Fluxo_array1 = Flux1.Flux()


# caso 2:

Concen_CO2 = np.random.rand(2,2)

Concen_eq = 0.8

N = -0.18

U = 10

K_600 = 2.07*(0.215*(U**1.7))

Temperatura_C = 35

Flux2 = Liberacao_gas_dagua_para_Atm(Concen_CO2, Concen_eq, N, K_600, None, U,'w', Temperatura_C)           
          
print(Flux2.funcao_K_gas())

Fluxo_array2 = Flux2.Flux()




import matplotlib.pyplot as plt
plt.figure()
plt.imshow(Fluxo_array)
plt.colorbar()
plt.show()    