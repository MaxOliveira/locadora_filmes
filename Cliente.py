    # -*- coding: utf-8 -*-
#import java.util.Enumeration;
#import java.util.Vector;
from Filme import Filme
from Alocacao import Alocacao
import itertools

class Cliente():
    _nome = None
    _alocacoes = []

    def __init__(self, nome):
        self._nome = nome
        self._alocacoes = []
    def addicionarAlocacao(self, alocacao): # art de tipo alocacao
        self._alocacoes.append(alocacao)
    def getNome(self):
        return self._nome
    def ExpresaoParaCalcularDadosDeAlocacao(self):
        totalQuantidade = 0.0
        pontosFrequenciaAlocacao = 0
        listaDeAlocacoes = iter(self._alocacoes)
        resultado = 'Registro de Locação para : '+ self.getNome()+'\n'

        #while(alocacoes):
        for cadaAlocacao in listaDeAlocacoes:
            charge = 0

            pontosFrequenciaAlocacao = Alocacao.getPontosFrequenciaAlocacao(cadaAlocacao)

            bonusAlocacao = Alocacao.getBonusAlocacao(cadaAlocacao)

            resultado = resultado + ' '+cadaAlocacao.getFilme().getTituloFilme()+' '+ str(cadaAlocacao.getCharge())+'\n'

        resultado = resultado + "Quantia devida é "+ str(self.getTotalAlocacao())+"\n"
        resultado = resultado + 'Voce ganhou '+ str(self.getTotalPontosFrequenciaAlocacao())+' pontos de locacao.'
        return resultado

    def getTotalAlocacao(self):
        resultado = 0
        listaDeAlocacoes = iter(self._alocacoes)
        for cadaAlocacao in listaDeAlocacoes:
            resultado = resultado + cadaAlocacao.getCharge()
        return resultado

    def getTotalPontosFrequenciaAlocacao(self):
        resultado = 0.0
        listaDeAlocacoes = iter(self._alocacoes)
        for cadaAlocacao in listaDeAlocacoes:
            resultado = resultado + cadaAlocacao.getPontosFrequenciaAlocacao()
        return resultado

if __name__ == '__main__':
    meuCliente = Cliente('Ruben')
    print meuCliente.getNome()
    fil01 = Filme('Titanic',2)
    alo01 = Alocacao(fil01,5) #filme, dias locados
    alo02 = Alocacao(fil01,5) #filme, dias locados
    alo03 = Alocacao(fil01,6) #filme, dias locados

    meuCliente.addicionarAlocacao(alo01)
    meuCliente.addicionarAlocacao(alo02)
    meuCliente.addicionarAlocacao(alo03)

    print meuCliente.ExpresaoParaCalcularDadosDeAlocacao()
