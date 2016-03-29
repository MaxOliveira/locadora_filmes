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
    def Expresao(self):
        totalQuantidade = 0.0
        pontosFrequenciaAlocacao = 0
        listaDeAlocacoes = iter(self._alocacoes)
        resultado = 'Registro de Locação para : '+ self.getNome()+'\n'

        #while(alocacoes):
        for alocacao in listaDeAlocacoes:
            estaQuantidade = 0
            #alocacao = next(alocacoes) #alocacao tipo alocacao
            #alocacao dever ser de tipo alocacao
            #Determinar valores para alocacao linha
            estaQuantidade = Alocacao.quantidadePara(alocacao,estaQuantidade)

            #adicionar pontos de locador frequente
            pontosFrequenciaAlocacao = self.addPontosFrequenciaAlocacao(pontosFrequenciaAlocacao)

            #adicionar bonus para uma locação de dois dias para lançamentos
            pontosFrequenciaAlocacao = self.bonusAlocacao(alocacao, pontosFrequenciaAlocacao)

            #mostrar informacoes para esta locacao
            resultado = resultado + ' '+alocacao.getFilme().getTitulo()+' '+ str(estaQuantidade)+'\n'

        #adicionar rodape do relatorio
        resultado = resultado + "Quantia devida é "+ str(totalQuantidade)+"\n"
        resultado = resultado + 'Voce ganhou '+ str(pontosFrequenciaAlocacao)+' pontos de locacao.'
        return resultado

    def addPontosFrequenciaAlocacao(self, pontosFrequenciaAlocacao):
        return pontosFrequenciaAlocacao + 1

    def bonusAlocacao(self, alocacao, pontosFrequenciaAlocacao):
        if alocacao.getFilme().getPrecoCodigo() == Filme.NOVA_RELEASE and alocacao.getDiasAlocados() > 1:
            return pontosFrequenciaAlocacao +1
        else:
            return pontosFrequenciaAlocacao

if __name__ == '__main__':
    meuCliente = Cliente('Ruben')
    print meuCliente.getNome()
    fil01 = Filme('Titanic',2)
    alo01 = Alocacao(fil01,5) #filme, dias locados
    alo02 = Alocacao(fil01,2) #filme, dias locados
    alo03 = Alocacao(fil01,1) #filme, dias locados

    meuCliente.addicionarAlocacao(alo01)
    meuCliente.addicionarAlocacao(alo02)
    meuCliente.addicionarAlocacao(alo03)

    print meuCliente.Expresao()
