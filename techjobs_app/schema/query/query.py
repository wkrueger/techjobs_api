import strawberry

from techjobs_app.schema.query.github import Github


@strawberry.type
class Query(Github):
    pass
