import urllib.parse
from techjobs_app.models.temp_oauth_tokens import TempOauthTokens
from techjobs_root.settings import GH_CLIENT_ID, GH_CLIENT_SECRET
import uuid
import requests
from typing import TypedDict

"""
FLUXO DE CRIAÇÃO DE USUÁRIO

 - Front busca link oauth e state
 - State é persistida
 - Usuário clica em "usar conta github"
    - Botão possui link para oauth github
 - Oauth chama o callback com "code" e "state"
    - Callback salva code e state em tabela
 - Front solicita dados de usuário enviando o "state"
   - Realizar polling ate ter retorno
   - Usuário confirma dados
 - Ao clicar no botão de confirmação, é enviado o "state" e em retorno é
   criado um usuário.

FLUXO DE AUTENTICAÇÃO VIA GITHUB
 - Front busca link oauth e state. State é salva no front.
 - Usuário clica em "entrar" invocando oauth github


PS: É necessário um fluxo de remoção de conta
"""


class AccessTokenResponse(TypedDict):
    access_token: str


def get_oauth_url():
    base_url = "https://github.com/login/oauth/authorize"
    vars = {"client_id": GH_CLIENT_ID, "state": uuid.uuid4()}
    return {"url": base_url + urllib.parse.urlencode(vars), "state": vars["state"]}


def get_access_token(code: str) -> AccessTokenResponse:
    base_url = "https://github.com/login/oauth/access_token"
    vars = {
        "client_id": GH_CLIENT_ID,
        "client_secret": GH_CLIENT_SECRET,
        "code": code,
    }
    response = requests.post(
        base_url, params=vars, headers={"Accept": "application/json"}
    )
    return response.json()


def persist_code(state: str, code: str, token: str):
    persist = TempOauthTokens(state=state, code=code, token=token)
    persist.save()


def get_user_info(self, state: str):
    pass
