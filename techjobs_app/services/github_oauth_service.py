import urllib.parse
import uuid

import requests
from kink import di

from techjobs_app.models.temp_oauth_tokens import TempOauthTokens
from techjobs_root.settings import GH_CLIENT_ID, GH_CLIENT_SECRET
from dataclasses import dataclass

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


@dataclass
class GetOauthUrlResponse:
    url: str
    state: str


@dataclass
class AccessTokenResponse:
    access_token: str


class GithubOauthService:
    def get_oauth_url(self):
        base_url = "https://github.com/login/oauth/authorize"
        query = {"client_id": GH_CLIENT_ID, "state": uuid.uuid4()}
        return GetOauthUrlResponse(
            url=base_url + urllib.parse.urlencode(query), state=query["state"]
        )

    def get_access_token(selfg, code: str) -> AccessTokenResponse:
        base_url = "https://github.com/login/oauth/access_token"
        query = {
            "client_id": GH_CLIENT_ID,
            "client_secret": GH_CLIENT_SECRET,
            "code": code,
        }
        response = requests.post(base_url, params=query, headers={"Accept": "application/json"})
        json = response.json()
        return AccessTokenResponse(access_token=json["access_token"])

    def persist_code(self, state: str, code: str, token: str):
        persist = TempOauthTokens(state=state, code=code, token=token)
        persist.save()

    def get_user_info(self, state: str):
        pass


di[GithubOauthService] = GithubOauthService()
