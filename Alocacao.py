# -*- coding: utf-8 -*-
from Filme import Filme

CRIANCAS = 2
REGULAR = 0
NOVA_RELEASE = 1

class Alocacao:
    def __init__(self,filme, diasAlocado): #filme de tipo Filme
        self._filme = filme #Tipo filme
        self._diasAlocados = diasAlocado
    def getDiasAlocados(self):
        return self._diasAlocados
    def getFilme(self):
        return self._filme

    def quantidadePara(alocacao, estaQuantidade):
        if alocacao.getFilme().getPrecoCodigo() == REGULAR:
            estaQuantidade = estaQuantidade + 2
            if alocacao.getDiasAlocados() > 2:
                estaQuantidade = estaQuantidade + (alocacao.getDiasAlocados() - 2) * 1.5
        elif alocacao.getFilme().getPrecoCodigo() == NOVA_RELEASE:
            estaQuantidade = estaQuantidade + 3
        elif alocacao.getFilme().getPrecoCodigo() == CRIANCAS:
            estaQuantidade = estaQuantidade + 1.5
            if alocacao.getDiasAlocados() > 3:
                estaQuantidade = estaQuantidade + (alocacao.getDiasAlocados()-3) * 1.5
        return estaQuantidade

if __name__ == '__main__':
    minhaAlocacao = Alocacao()
