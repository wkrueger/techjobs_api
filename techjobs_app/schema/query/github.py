import strawberry
from kink import inject

from techjobs_app.services.github_oauth_service import (
    GithubOauthService,
)


@inject
class Resolvers:
    def __init__(self, github: GithubOauthService):
        self.github = github

    def get_oauth_url(self):
        return self.github.get_oauth_url()

    def get_user_info_from_state(self, state: str):
        return self.github.get_user_info(state)


@strawberry.type
class GetOauthUrlResponse:
    url: str
    state: str


@strawberry.type
class AccessTokenResponse:
    access_token: str


@strawberry.type
class Github:
    @strawberry.field
    def get_oauth_url(self) -> GetOauthUrlResponse:
        return Resolvers().get_oauth_url()

    @strawberry.field
    def get_user_info_from_state(self, state: str) -> AccessTokenResponse:
        return Resolvers().get_user_info_from_state(state)
