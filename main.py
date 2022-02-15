# Graphene uses code-fist approach to building GraphQL API

from graphene import ObjectType, String, Schema

class Query(ObjectType):
    hello = String(name=String(default_value="stranger"))
    goodbye = String()

    # root and info are from GraphQL Context
    # for each field in the schema, there needs to be a resolver
    def resolve_hello(root, info, name):
        return f"Hello ${name}"
    
    def resolve_goodbye(root, info):
        return "Good Bye"

# Schema defines the types and the realtionship between the fields
# Schema contains
#   query (Object Type)
#   mutuation - changes data and retrieves changes
#   subscription - sends changes to clients

schema = Schema(query=Query)

# execute a query against a schema
query_string = 'query gethello{ hello }'
result = schema.execute(query_string)
print(result)

query_string = '{ GoodBye }'
result = schema.execute(query_string)
print(result)

# execute query using parameters
query_with_parameters = '{ hello(name: "GraphQL") }'
result = schema.execute(query_with_parameters)
print(result)