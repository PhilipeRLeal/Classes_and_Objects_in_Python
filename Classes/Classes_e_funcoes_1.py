# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 11:29:24 2018

@author: Philipe Leal
"""

class Point: # definicao de classe
        
    def __init__(self, x=0, y=0): # funcao de iinicializacao da classe criada
        self.x = x # self.x e self.y são atributos do objeto Point 
        self.y = y # self.x e self.y são atributos do objeto Point
    
    def __eq__(self, other): # verifica se um dado atributo do Point eh igual ao seguinte retornando True
        return self.x==other.x and self.y == other.y
        
    def distancia_da_origem(self): # propriedade da Classe Point
        import math
                                        # math.hypot fornece a distância euclidiana do ponto em relacao ao ponto (0,0)
        return math.hypot(self.x, self.y) # retorna a distância da origem
        
    def __repr__(self): # funcao que permite ao usuario checar qual eh o tipo de objeto
        """ Esta função é utilizada para retornar uma string com o Tipo da classe definida e sua instância.
            Permite que ao usuário transformar esta string retornada  (ou qualquer outra de mesmo formato) em instância:
            
        
        """
                
                
        return ("Point ({0.x!r}, {0.y!r})".format(self))
        
class Circle(Point):
    def __init__(self, radius, x=0, y=0):
        super().__init__(x,y)
        self.radius = radius
    
    def edge_distance_from_origin(self):
        
        return (self.distancia_da_origem() - self.radius)
    
    def area(self):
        import math
        
        return (math.pi * (self.radius**2))
    
    def circumference(self):
        import math
        return 2 * math.pi * self.radius
    
    def __eq__(self, other):
        return (self.radius== other.radius and super().__eq__(other))
    
    def __str__(self):
        return (repr(self))
    
    def __repr__(self): # funcao que permite ao usuario checar qual eh o tipo de objeto, além de retornar uma string com o tipo do objeto
        """ Esta função é utilizada para retornar uma string com o Tipo da classe definida e sua instância.
            Permite que ao usuário transformar esta string retornada  (ou qualquer outra de mesmo formato) em instância:
            
                Ex:
                    P = Shape.Point(3,9)
                    repr(p)     # retornará 'Point(3,9)
                    q = eval(p.__module__ + "." + repr(p))
                    repr(q)     # Retorna 'Point(3,9)
        """
        return ("Circle ({0.radius!r}, {0.x!r}, {0.y!r})".format(self))
        
    
def Distancia_entre_pontos(P1, P2):
    import math
    Distancia = math.sqrt(    ((P1.x - P2.x)**2) + ((P1.y - P2.y)**2)  )
    
    return Distancia



    
A = Point(2.0,2.0)

B = Point(3.0,2.0)

C = Circle(5.0, 2.0, 2.0)

print(A.distancia_da_origem())

print(Distancia_entre_pontos( A, B))

print(C.area())

print(C.distancia_da_origem()) # notar como a funcao da classe objeto também é válida para sua subclasse Circle

