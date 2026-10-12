
import datetime
import requests

def cotar():
    cotacoes = []
    hoje = datetime.date.today()

    for i in range(365):
        dia = hoje - datetime.timedelta(days=i)

        data = dia.strftime('%m-%d-%Y')

        url = f'https://economia.awesomeapi.com.br/json/daily/USD-BRL/1?start_date={dia.strftime("%Y%m%d")}&end_date={dia.strftime("%Y%m%d")}'

        resposta = requests.get(url)
        dados = resposta.json()

        if dados:
            cotacoes.append(float(dados[0]['bid']))
        else:
            cotacoes.append(None)

    return cotacoes
