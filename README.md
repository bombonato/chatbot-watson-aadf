# chatbot-watson-aadf

Chatbot IBM Watson com integração Telegram
- Suporte a VOZ

### Turma Pós-IA 2021-1

- Alexandre Augusto Barbosa - 2186330043
- Artur Clemente, 2186330018
- Daniela Ribeiro Bragança Silva, 2186330030
- Fabio Bombonato, 2186330024

# Recursos

- Pesquisa por CEP
- Pesquisa por Clima
- Pesquisa por Voz básica

### Comandos

- usar "ajuda" no Telegram que obtem ajuda pelo watson
- ou usar "/help" para obter alguns comandos diretamente pelo Telegram

### Exemplos

- Oi, Olá, como vai
- O que pode fazer? Quais recursos estão disponíveis? 
- Gostaria de pesquisar o cep
- Quero saber o clime
- Tchau, adeus, etc

### Ambiente

A seguir as variáveis que devem ser configuradas no Heroku:

* WATSON_ASSISTANT_TOKEN: token IAM do Watson Assistant
* WATSON_ASSISTANT_URL: URL do Watson Assistant
* ASSISTANT_ID: ID do Assistant criado no Watson Assistant
* T2S_TOKEN: Token do Watson Text to Speech
* T2S_URL: URL de acesso ao Watson Text to Speech
* S2T_TOKEN: Token do Watson Speech to Text
* S2T_URL: URL de acesso ao Watson Speech to Text
* TELEGRAM_BOT_TOKEN: token do bot criado no Telegram
* TELEGRAM_WEBHOOK: url da aplicação do heroku (https://\<appname\>.herokuapp.com)
* OWM_API_KEY: chave da API do OpenWeatherMap