# -*- coding: UTF-8 -*-
from descontos import Desconto_por_cinco_itens, Desconto_por_mais_de_quinhentos_reais, Sem_desconto
class Calculador_de_descontos(object):

    def calcula(self, orcamento):

        desconto = Desconto_por_cinco_itens(
            Desconto_por_mais_de_quinhentos_reais(Sem_desconto())
        ).calcular(orcamento)
        
        return desconto

if __name__ == '__main__':

    from orcamento import Orcamento, Item

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM - 1', 100))
    orcamento.adiciona_item(Item('ITEM - 1', 50))
    orcamento.adiciona_item(Item('ITEM - 1', 400))

    print(orcamento.total_itens)
    print(orcamento.valor)

    calc_descontos = Calculador_de_descontos()
    
    print(f'Desconto calculado: {calc_descontos.calcula(orcamento)}')