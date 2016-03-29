# -*- coding: utf-8 -*-
from Filme import Filme

CRIANCAS = 2
REGULAR = 0
NOVA_RELEASE = 1

class Alocacao:
    def __init__(self, filme, diasAlocado): #filme de tipo Filme
        self._filme = filme #Tipo filme
        self._diasAlocados = diasAlocado
    def getDiasAlocados(self):
        return self._diasAlocados
    def getFilme(self):
        return self._filme

    def quantidadeAlocacoesPorCodigo(self):
        resultado = 0.0
        if self.getFilme().getPrecoCodigo() == REGULAR:
            resultado = resultado + 2
            if self.getDiasAlocados() > 2:
                resultado = resultado + (self.getDiasAlocados() - 2) * 1.5
        elif self.getFilme().getPrecoCodigo() == NOVA_RELEASE:
            resultado = resultado + 3
        elif self.getFilme().getPrecoCodigo() == CRIANCAS:
            resultado = resultado + 1.5
            if self.getDiasAlocados() > 3:
                resultado = resultado + (self.getDiasAlocados()-3) * 1.5
        return resultado

if __name__ == '__main__':
    minhaAlocacao = Alocacao()
