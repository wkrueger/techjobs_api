import strawberry

from .query.query import Query

schema = strawberry.Schema(query=Query)
