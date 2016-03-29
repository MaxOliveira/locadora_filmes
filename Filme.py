# -*- coding: utf-8 -*-
CRIANCAS = 2
REGULAR = 0
NOVA_RELEASE = 1

class Filme:
    CRIANCAS = 2
    REGULAR = 0
    NOVA_RELEASE = 1
    _titulo = None
    _precoCod = None

    def __init__(self,titulo,precoCodigo):
        self._titulo = titulo
        self._precoCodigo = precoCodigo
    def getPrecoPorCodigo(self):
        return self._precoCodigo
    def setPrecoPorCodigo(self, arg):
        self._precoCodigo = arg
    def getTituloFilme(self):
        return self._titulo

    def getCharge(self, diasAlocados):
        resultado = 0.0
        if self._precoCodigo == REGULAR:
            resultado = resultado + 2
            if diasAlocados > 2:
                resultado = resultado + (diasAlocados - 2) * 1.5
        elif self._precoCodigo == NOVA_RELEASE:
            resultado = resultado + 3
        elif self._precoCodigo == CRIANCAS:
            resultado = resultado + 1.5
            if diasAlocados > 3:
                resultado = resultado + (diasAlocados-3) * 1.5
        return resultado

    def getBonusAlocacao(self, diasAlocados):
        if self._precoCodigo == Filme.NOVA_RELEASE and diasAlocados > 1:
            return 2
        else:
            return 1

if __name__ == '__main__':
    meuFilme = Filme('titanic',3)
