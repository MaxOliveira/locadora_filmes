# -*- coding: utf-8 -*-
from Filme import Filme

CRIANCAS = 2
REGULAR = 0
NOVA_RELEASE = 1

class Alocacao:
    def __init__(self, filme, diasAlocados): #filme de tipo Filme
        self._filme = filme #Tipo filme
        self._diasAlocados = diasAlocados
    def getDiasAlocados(self):
        return self._diasAlocados
    def getFilme(self):
        return self._filme

    def quantidadeAlocacoesPorCodigo(self):
        resultado = 0.0
        if self.getFilme().getPrecoPorCodigo() == REGULAR:
            resultado = resultado + 2
            if self.getDiasAlocados() > 2:
                resultado = resultado + (self.getDiasAlocados() - 2) * 1.5
        elif self.getFilme().getPrecoPorCodigo() == NOVA_RELEASE:
            resultado = resultado + 3
        elif self.getFilme().getPrecoPorCodigo() == CRIANCAS:
            resultado = resultado + 1.5
            if self.getDiasAlocados() > 3:
                resultado = resultado + (self.getDiasAlocados()-3) * 1.5
        return resultado

    def addPontosFrequenciaAlocacao(self, pontosFrequenciaAlocacao):
        pontosFrequenciaAlocacao += 1
        return pontosFrequenciaAlocacao

    def bonusAlocacao(self, pontosFrequenciaAlocacao):
        if self.getFilme().getPrecoPorCodigo() == Filme.NOVA_RELEASE and self.getDiasAlocados() > 1:
            return pontosFrequenciaAlocacao +1
        else:
            return pontosFrequenciaAlocacao

if __name__ == '__main__':
    minhaAlocacao = Alocacao()
