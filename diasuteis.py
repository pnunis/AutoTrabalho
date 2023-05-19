import pandas as pd
from pandas.tseries.offsets import BMonthEnd

def calcular_dias_uteis_mes(ano, mes):
    data_inicial = pd.Timestamp(year=ano, month=mes, day=1)
    data_final = BMonthEnd().rollforward(pd.Timestamp(year=ano, month=mes, day=1))

    dias_uteis = pd.bdate_range(start=data_inicial, end=data_final, freq='B')

    return dias_uteis.size

# Exemplo de uso
ano = 2023
mes = 5

dias_uteis = calcular_dias_uteis_mes(ano, mes)
print(f'O número de dias úteis em {mes}/{ano} é: {dias_uteis}')
