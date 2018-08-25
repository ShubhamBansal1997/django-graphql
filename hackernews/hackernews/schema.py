# -*- coding: utf-8 -*-
# @Author: Shubham Bansal
# @Date:   2018-08-26 01:07:08
# @Last Modified by:   Shubham Bansal
# @Last Modified time: 2018-08-26 01:22:57
import graphene

import links.schema

class Query(links.schema.Query, graphene.ObjectType):
  pass


class Mutation(links.schema.Mutation, graphene.ObjectType):
  pass

schema = graphene.Schema(query=Query, mutation=Mutation)
