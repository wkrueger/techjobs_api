import graphene

from techjobs_app.schema.github_oauth_query import GithubOauthQuery


class Query(GithubOauthQuery, graphene.ObjectType):
    pass
