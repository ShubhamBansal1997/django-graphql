# -*- coding: utf-8 -*-
# @Author: Shubham Bansal
# @Date:   2018-08-26 01:07:08
# @Last Modified by:   Shubham Bansal
# @Last Modified time: 2018-08-26 01:10:45
import graphene

import links.schema

class Query(links.schema.Query, graphene.ObjectType):
  pass


schema = graphene.Schema(query=Query)
