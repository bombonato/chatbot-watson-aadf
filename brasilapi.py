import requests
import os

base_url = 'https://brasilapi.com.br/api'

def get_cep(cep):
    endpoint = '/cep/v2/' + cep

    response = requests.get(endpoint).json()
    if(response.status_code == requests.codes.ok):
        return response['street'] + ', ' + response['neighborhood'] + ', ' \
                + response['city'] + ' - ' + response['state'] + ', ' \
                + response['cep']
    else:
        return "{} não encontrado".format(cep)