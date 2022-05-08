import requests
import logging
import os

base_url = 'https://brasilapi.com.br/api'

logger = logging.getLogger('TelegramBot - BrasilAPI')

def get_cep(cep):
    endpoint = base_url + '/cep/v2/' + cep

    response = requests.get(endpoint)

    logger.info('brasilcep response:\n ' + str(response))

    if(response.status_code == requests.codes.ok):
        response = response.json()

        return response['street'] + ', ' + response['neighborhood'] + ', ' \
                + response['city'] + ' - ' + response['state'] + ', ' \
                + response['cep']
    else:
        # return ''
        return "{} não encontrado".format(cep)