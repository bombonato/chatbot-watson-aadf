import logging
import brasilapi
import weatherapi

logger = logging.getLogger('TelegramBot - Actions')

def action_handler(action, parameters, return_var):
    return_values = {}
    if action == 'cep':
        return_values = search_cep(parameters, return_var)
    elif action == 'clima':
        return_values = get_weather(parameters, return_var)

    return {
            'skills': {
                'main skill': {
                    'user_defined': return_values
                }
            }
        }

def search_cep(parameters, return_var):
    query = parameters['termo']
    cep_text = brasilapi.get_cep(query) # TODO: (melhoria) mudar para tratar retorno como dicionário

    # trato os nomes aqui para facilitar, tratar no assistant eh mais complexo
    # pois nao tenho o mesmo poder de programacao
    cep_formatado = '\n\n'
    cep_formatado += cep_text + '\n\n'

    return {
        return_var: cep_formatado
    }

def get_weather(parameters, return_var):
    query = parameters['termo']

    logger.info('get_weather - cidade: {}'.format(query))

    clima_text = weatherapi.obter_clima(query) 
    
    clima_formatado = '\n\n'
    clima_formatado += clima_text + '\n\n'

    return {
        return_var: clima_formatado
    }