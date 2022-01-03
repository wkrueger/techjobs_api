# techjobs_api

(wip)

  - Repositório de postagens de vagas de TI
  - Fluxo de aprovação
  - Disparo de mensagens para e-mail e Discord

## Requisitos

  - Python 3.9
  - PostgreSQL (13)
  - Gerenciador de pacotes: pipenv

## Comandos iniciais

**Instalação:** pipenv install

**Variáveis de ambiente:** `cp .env.development .env`

**Execução:** `pipenv shell` e `python manage.py runserver`


O arquivo `docker-compose.yml` possui uma instância postgresql de exemplo (este compose não inclui o servidor python). (`docker-compose up -d`).

## Ambiente de desenvolvimento

  - Recomendado o uso do formatador de código **black** e a ativação da configuração "format on save" se usando o VS Code (já incluído arquivo de configuração).