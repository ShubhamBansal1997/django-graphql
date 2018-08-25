# -*- coding: utf-8 -*-
# @Author: Shubham Bansal
# @Date:   2018-08-26 01:07:08
# @Last Modified by:   Shubham Bansal
# @Last Modified time: 2018-08-26 02:12:40
import graphene
import graphql_jwt

import links.schema
import users.schema


class Query(links.schema.Query, users.schema.Query, graphene.ObjectType):
    pass


class Mutation(users.schema.Mutation, links.schema.Mutation, graphene.ObjectType,):
  token_auth = graphql_jwt.ObtainJSONWebToken.Field()
  verify_token = graphql_jwt.Verify.Field()
  refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
