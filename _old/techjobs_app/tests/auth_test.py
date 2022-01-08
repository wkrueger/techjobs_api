from django.test.testcases import TransactionTestCase
from techjobs_app.services.github_oauth_service import AccessTokenResponse
from unittest.mock import patch


def get_access_token_mock(code: str) -> AccessTokenResponse:
    return {"access_token": "123456"}


class GithubAuthTest(TransactionTestCase):
    @patch(
        "techjobs_app.services.github_oauth_service.get_access_token",
        return_value=get_access_token_mock,
    )
    def call_callback(self):
        resp = self.client.get("/oauth_callback")
        a = 2
