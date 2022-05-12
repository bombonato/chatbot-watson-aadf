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
- Pesquisa utilizando Voz básica

### Comandos Básicos

- usar "ajuda" no Telegram que obtem ajuda pelo watson
- ou usar "/help" para obter alguns comandos diretamente pelo Telegram
- Enviar perguntas como: "Quais recursos estão disponíveis?"

### Exemplos

- Oi, Olá, como vai
- O que pode fazer? Quais recursos estão disponíveis? 
- Gostaria de pesquisar o cep
- Quero saber o clima
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

### Watson Assistant

Importar a SKILL utilizada no Watson Assistant:

Skill
- Acessar o IBM Watson Assistant
- Barra Lateral Skill
- Clicar em "Create skill"
- Selecionar o cartão da Skill criado, clicar em próximo
- Selecionar "Import skill" e selecionar o arquivo de versão mais novo "skill-WatsonBotSkillAADF<versao>.json"
- O webhook é criado nessa importação, apontando para o código rodando no Heroku (ou outro provedor utilizado), pode ser verificado entrando na Skill e clicando no menu "Webhooks", no caso, corresponde ao local onde a aplicação gateway entre Telegram e Watson esta rodando (ex. heroku)

Assistant
- Barra lateral Assistants
- Criar uma nova Assistente
- Selecionar a Skill criada no passo anterior para fazer a interligação

### Notas

- Implementação no Watson ainda não reconhecendo valores numéricos nos testes, tais como pesquisa por CEP, a qual identifica em palavras por extenso, em ves de números, impedindo a pesquisa por CEP.
  - Ex.: "2022-01-01 99:99:99,999 - TelegramBot - INFO - Detectada frase: setenta e um nove três um clientes e quarenta"
- Recurso de pesquisa por Clima esta funcional, verificamos mais facilidades na pesquisa por cidades como Brasília, Curitiba, Florianopolis, Belo Horizonte, etc, certa dificuldade para cidade como São Paulo, Rio de Janeiro, etc, possivelmente relacionado a questões da fala como entonação, espaçamento, ruído, etc.