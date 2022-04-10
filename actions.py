import brasilapi
import weather


def action_handler(action, parameters, return_var):
    return_values = {}
    if action == 'cep':
        return_values = search_cep(parameters, return_var)

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
    if cep_text != '':
        weather_text = weather.get_weather(query)
        cep_text += weather_text
    else:
        cep_text = "{} não encontrado".format(parameters['termo'])

    # trato os nomes aqui para facilitar, tratar no assistant eh mais complexo
    # pois nao tenho o mesmo poder de programacao
    cep_formatado = '\n\n'
    cep_formatado += cep_text + '\n\n'

    return {
        return_var: cep_formatado
    }

