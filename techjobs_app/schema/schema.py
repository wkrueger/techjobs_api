import graphene
from techjobs_app.schema.mutation import Mutation
from techjobs_app.schema.query import Query

schema = graphene.Schema(query=Query, mutation=Mutation)
