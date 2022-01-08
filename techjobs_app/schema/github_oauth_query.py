import graphene
from injector import Injector

from techjobs_app.services.github_oauth_service import GithubOauth

i = Injector()


class GithubUserInfo(graphene.ObjectType):
    name = graphene.NonNull(graphene.String)


class GithubOauthUrl(graphene.ObjectType):
    url = graphene.NonNull(graphene.String)
    state = graphene.NonNull(graphene.String)


class GithubOauthQuery(graphene.ObjectType):
    github_oauth_url = graphene.Field(GithubOauthUrl)

    def resolve_github_oauth_url(self, info):
        ghservice = i.get(GithubOauth)
        data = ghservice.get_oauth_url()
        return GithubOauthUrl(url=data["url"], state=data["state"])

    github_user_info = graphene.Field(
        GithubUserInfo, state=graphene.NonNull(graphene.String)
    )

    def resolve_github_user_info(self, info, state: str):
        return GithubUserInfo(name="Hello")
