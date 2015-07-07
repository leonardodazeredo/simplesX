'''
Created on 6 Jul 2015

@author: leo
'''
from fractions import Fraction

class F(Fraction):
    '''
    Classe que representa um numero fracionario, extendendo fractions.Fraction, e implentando a lógica o "M grande"
    '''   
    def __init__(self,n,M=False):
        self.fraction = Fraction(n)
        self.M=M
    
    def __repr__(self):
        """repr(self)"""
        return self.fraction.__repr__()

    def __str__(self):
        """str(self)"""
        return  self.fraction.__str__()
        
    def __eq__(self, f):
        """a == b"""
        return  self.fraction.__eq__(f)

    def __add__(self, f):
        """a + b"""
        return  self.fraction.__add__(f)

    def ___sub__(self, f):
        """a - b"""
        return  self.fraction.__sub__(f)

    def __mul__(self, f):
        """a * b"""
        return  self.fraction.__mul__(f)

    def __div__(self, f):
        """a / b"""
        return  self.fraction.__div__(f)
    
    def __lt__(self, f):
        """a < b"""
        return self.fraction.__lt__(f)

    def __gt__(self, f):
        """a > b"""
        return self.fraction.__gt__(f)

    def __le__(self, f):
        """a <= b"""
        return self.fraction.__le__(f)

    def __ge__(self, f):
        """a >= b"""
        return self.fraction.__ge__(f)

