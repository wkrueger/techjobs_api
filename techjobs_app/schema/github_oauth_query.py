import graphene


class GithubUserInfo(graphene.ObjectType):
    name = graphene.String()


class GithubOauthUrl(graphene.ObjectType):
    url = graphene.String()
    state = graphene.String()


class GithubOauthQuery(graphene.ObjectType):
    github_user_info = graphene.Field(GithubUserInfo, state=graphene.String())

    def resolve_github_user_info(self, root, info, state: str):
        return GithubUserInfo(name="Hello")

    github_oauth_url = graphene.Field(GithubOauthUrl)

    def resolve_github_oauth_url(self, root, info):
        return GithubOauthUrl(url="some_url", state="some_state")
