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

    def getCharge(self):
        charge =  self._filme.getCharge(self._diasAlocados)
        return charge

    def getPontosFrequenciaAlocacao(self):
        pontosFrequenciaAlocacao = 0.0
        pontosFrequenciaAlocacao += 1
        return pontosFrequenciaAlocacao

    def getBonusAlocacao(self):
        bonusAlocacao = self._filme.getBonusAlocacao(self._diasAlocados)
        return bonusAlocacao


if __name__ == '__main__':
    minhaAlocacao = Alocacao()
