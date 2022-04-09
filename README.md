# chatbot-watson-aadf

Chatbot IBM Watson com integração Telegram

### Turma Pós-IA 2021-1

- Alexandre Augusto Barbosa - 2186330043
- Artur Clemente, 2186330018
- Daniela Ribeiro Bragança Silva, 2186330030
- Fabio Bombonato, 2186330024

A seguir as variáveis que devem ser configuradas no Heroku:

Variáveis de Ambinete:

* WATSON_ASSISTANT_TOKEN: token IAM do Watson Assistant
* WATSON_ASSISTANT_URL: URL do Watson Assistant
* ASSISTANT_ID: ID do Assistant criado no Watson Assistant
* S2T_TOKEN: token IAM da API Watson SpeechToText
* S2T_URL: URL da API Watson SpeechToText
* T2S_TOKEN: token IAM da API Watson TextToSpeech
* T2S_URL: URL da API Watson TExtToSpeech
* TELEGRAM_BOT_TOKEN: token do bot criado no Telegram
* TELEGRAM_WEBHOOK: url da aplicação do heroku (https://\<appname\>.herokuapp.com)