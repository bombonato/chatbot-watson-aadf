import os
import logging

import pyowm

logger = logging.getLogger('TelegramBot - WeatherAPI')

def obter_clima(cidade):

    API_KEY = os.environ['OWM_API_KEY']

    logger.info('obter_clima - cidade: {}'.format(cidade))
    logger.info('obter_clima - key: {}'.format(API_KEY))

    place_br = "{},BR".format(cidade)

    config_dict = pyowm.utils.config.get_default_config()
    config_dict['language'] = 'pt_br'

    owm = pyowm.OWM(API_KEY, config_dict)
    omgr = owm.weather_manager()
    
    observation = omgr.weather_at_place(place_br)

    w = observation.weather

    temp = w.temperature('celsius')

    # clima_formatado = "Previsão para {0} - {1} - {2}ºC".format(cidade, w.detailed_status, temp['temp'])

    clima_formatado = "Previsão para {0}: {1}\n" \
        "- Temperatura: {2}ºC - Sensação: {3}ºC\n" \
        "- Humidade: {4}%\n" \
        "- Pressão: {5} hPa\n" \
        "- Vento: {6} m/s".format(cidade, w.detailed_status, temp['temp'], temp['feels_like'],w.humidity,w.pressure['press'],w.wind()['speed'])

    # return "Previsão para " + place_br + ": "+ w.detailed_status + "\n" \
    #     "- Temperatura: " + temp + " Celcius\n" \
    #     "- Humidade: " + w.humidity + "%\n" \
    #     "- Pressão: " + w.pressure['press'] + " hPa\n" \
    #     "- Vento: " + w.wind()['speed'] + " m/s"
    return clima_formatado