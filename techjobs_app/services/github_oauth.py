import urllib.parse
from techjobs_app.models.temp_oauth_tokens import TempOauthTokens
from techjobs_root.settings import GH_CLIENT_ID, GH_CLIENT_SECRET
import uuid
import requests
from typing import TypedDict


class AccessTokenResponse(TypedDict):
    access_token: str


class GithubOauth:
    def get_oauth_url(self):
        base_url = "https://github.com/login/oauth/authorize"
        vars = {"client_id": GH_CLIENT_ID, "state": uuid.uuid4()}
        return {"url": base_url + urllib.parse.urlencode(vars), "state": vars["state"]}

    def get_access_token(self, code: str) -> AccessTokenResponse:
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

    def persist_code(self, state: str, code: str, token: str):
        persist = TempOauthTokens(state=state, code=code, token=token)
        persist.save()

    def get_user_info(self, state: str):
        pass
