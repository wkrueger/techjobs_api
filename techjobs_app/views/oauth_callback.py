from django.http import HttpRequest

from techjobs_app.services.github_oauth_service import GithubOauth
from injector import inject

"""
FLUXO DE CRIAÇÃO DE USUÁRIO

 - Front busca link oauth e state
 - State é persistida
 - Usuário clica em "usar conta github"
    - Botão possui link para oauth github
 - Oauth chama o callback com "code" e "state"
    - Callback salva code e state em tabela
 - Front solicita dados de usuário enviando o "state"
   - Usuário confirma dados
 - Ao clicar no botão de confirmação, é enviado o "state" e em retorno é
   criado um usuário.

FLUXO DE AUTENTICAÇÃO VIA GITHUB
 - Front busca link oauth e state. State é salva no front.
 - Usuário clica em "entrar" invocando oauth github


PS: É necessário um fluxo de remoção de conta
"""


class OauthCallback:
    @inject
    def __init__(self, githubOauth: GithubOauth) -> None:
        self.githubOauth = githubOauth

    def view(self, request: HttpRequest):
        code = request.GET["code"]
        state = request.GET["state"]
        token = self.githubOauth.get_access_token(code)["access_token"]
        self.githubOauth.persist_code(state=state, code=code, token=token)
