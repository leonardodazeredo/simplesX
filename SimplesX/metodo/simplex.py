'''
Created on 22 Jun 2015

@author: leo
'''
from numpy import matrix
from model.F import F

class Tabela(object):
 
    def __init__(self, funcaoObjetivo,restricoes=None,tipo='<='):
        self.linhaFuncaoObjetivo = [1] + [c*(-1) for c in funcaoObjetivo] + [0 for r in restricoes] + [0] 
        
        self.linhasRestricoes = []
        for i,(coeficientes,termo) in enumerate(restricoes):
            zeros = [0 for r in restricoes] 
            zeros[i] = 1       
            self.linhasRestricoes.append([0] + coeficientes + zeros + [termo])
            
        self.linhaFuncaoObjetivo = [F(n) for n in self.linhaFuncaoObjetivo]
        self.linhasRestricoes = [[F(n) for n in l] for l in self.linhasRestricoes]
       
    def printTabela(self):
        '''print(self.linhaFuncaoObjetivo)
        for restricao in self.linhasRestricoes:
            print(restricao)'''
        
        tabela = [self.linhaFuncaoObjetivo] + self.linhasRestricoes    
        print('\n', matrix([[float(f) for f in l] for l in tabela]))
         
    '''
    Encontra a coluna corresponte a variavel que entra da base e retorna seu indice 
    '''   
    def _encontraEntra(self):
        menorCoeficiente = min(self.linhaFuncaoObjetivo[1:-1])
        
        if menorCoeficiente >= 0: 
            return None
        else:        
            return self.linhaFuncaoObjetivo[0:-1].index(menorCoeficiente)
 
    '''
    Encontra a linha corresponte a variavel que sai da base e retorna seu indice 
    ''' 
    def _encontraSai(self, colunaDoPivo):   
        termos = [r[-1] for r in self.linhasRestricoes]
        coefisVariavelEntra = [r[colunaDoPivo] for r in self.linhasRestricoes]
        
        razoes = []
        for i,termo in enumerate(termos):
            if coefisVariavelEntra[i] == 0:
                razoes.append(99999999 * abs(max(termos)))
            else:
                razoes.append(termo/coefisVariavelEntra[i])
                
        menorRazaoPositiva = min([r for r in razoes if r > 0])        

        return razoes.index(menorRazaoPositiva)
 
    '''
    Faz o pivoteamento, tendo como elemento pivo o elemento pi,pj da matrix de restrições
    ''' 
    def _pivoteamento(self, pi, pj):
        #elemento pivo
        p = self.linhasRestricoes[pi][pj]     
        #divide a linha do pivo pelo elemento pivo       
        self.linhasRestricoes[pi] = [x/p for x in self.linhasRestricoes[pi]]     
        
        #para cada elemento da linha correspondente a F.O. multiplica cada elemento da linha pivo
        tempLinha = [self.linhaFuncaoObjetivo[pj]* x for x in self.linhasRestricoes[pi]]  
        #subtrai cada elemendo da linha da F.O. pelo falor calculado acima
        self.linhaFuncaoObjetivo = [self.linhaFuncaoObjetivo[i] - tempLinha[i] for i in range(len(tempLinha))]
        
        #para cara linha corresponte a restricao i repete o mesmo procedimento feito na linha fa F.O.
        for i,restricao in enumerate(self.linhasRestricoes):
            if i != pi: 
                tempLinha = [restricao[pj]* x for x in self.linhasRestricoes[pi]]         
                self.linhasRestricoes[i] = [restricao[i] - tempLinha[i] for i in range(len(tempLinha))]   
 
    '''
    Testa se a F.O. atual indica que a solução otima foi encontrada
    ''' 
    def _solucaoOtimaEncontrada(self):
        if min(self.linhaFuncaoObjetivo[1:-1]) >= 0: 
            return True
        else:
            return False
    
    '''
    Executa o metodo simplex
    ''' 
    def executar(self):
        self.printTabela()
        
        while not self._solucaoOtimaEncontrada():
            c = self._encontraEntra()
            r = self._encontraSai(c)
            
            self._pivoteamento(r,c)
            
            print('\nColuna do pivo: %s\nLinha do pivo: %s'%(c+1,r))
            
            self.printTabela()
            
    def solucao(self):
        self.executar()
             
if __name__ == '__main__':
    
    """
    max z = 2x + 3y + 2z
    
    s.a.    2x +  y +  z <= 4
             x + 2y +  z <= 7
                       z <= 5
            x,y,z >= 0
    """
    #t = Tabela([2,3,2],restricoes=[([2, 1,1], 4),([1, 2, 1], 7),([0, 0, 1], 5)])
    
    """
    max z = 3x + 5y
    
    s.a.    2x + 4y <= 10
            6x +  y <= 20
             x -  y <= 30
            x,y >= 0
    """
    t = Tabela([3,5],restricoes=[([2, 4], 10),([6, 1], 20),([1, -1], 30)])
    
    """
    max z = 3x + 5y
    
    s.a.    2x + 4y <= 10
            6x +  y <= 20
             x -  y <= 30
            x,y >= 0
    """
    #t = Tabela([3,5],restricoes=[([2, 4], 10),([6, 1], 20),([1, -1], 30)])
    
    t.executar()

    