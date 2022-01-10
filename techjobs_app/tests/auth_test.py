import json

from django.test.testcases import TransactionTestCase
from kink import di

from techjobs_app.services.github_oauth_service import (
    AccessTokenResponse,
    GithubOauthService,
)


class GithubMock(GithubOauthService):
    def get_access_token(self, code: str) -> AccessTokenResponse:
        return AccessTokenResponse(access_token="123456")


GQL_PATH = "/graphql/"


class GithubAuthTest(TransactionTestCase):
    def setUp(self) -> None:
        super().setUp()
        di[GithubOauthService] = GithubMock()

    def test_github_auth_url(self):
        response = self.client.post(
            GQL_PATH,
            json.dumps(
                {
                    "query": """query {
              getOauthUrl {
                url
                state
              }
            }
            """,
                }
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)

    def test_call_callback(self):
        resp = self.client.get("/oauth_callback", data={"code": "code", "state": "state"})
        self.assertEqual(resp.status_code, 200)
