import requests
import logging

base_url = 'http://www.bstinfo.com.br/objetivoapiqa/api/tela/previsaoDoTempo'

logger = logging.getLogger('TelegramBot')

def get_weather(cep):
    headers = {'content-type': 'application/json'}
    data = {'cep': cep}
    response = requests.post(base_url,json=data, headers=headers)
    
    if(response.status_code == requests.codes.ok):
        response = response.json()

        retorno = 'Clima: ' + str(response['descricao']) + '\n'
        retorno += 'Temperatura atual: ' + str(response['temperatura']) + '\n'
        retorno += 'Umidade: ' + str(response['umidade']) + '\n'
        retorno += '---' * 20
        retorno += '\nPróximos dias:'
        for previsao in response['previsoes']:
            retorno += '\n' + str(previsao['data'])
            retorno += '\nClima: ' + str(previsao['descricao'])
            retorno += '\nTemperatura mínima: ' + str(previsao['tempmin'])
            retorno += '\nTemperatura máxima: ' + str(previsao['tempmax'])
            retorno += '\n\n'

        #print(retorno)
        return retorno

    else:
        return ''


#get_weather('12242-905')