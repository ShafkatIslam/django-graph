import graphene
import event_management.api.schema

class Query(event_management.api.schema.Query, graphene.ObjectType):
    pass

class Mutation(event_management.api.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)