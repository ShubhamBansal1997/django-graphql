# -*- coding: utf-8 -*-
# @Author: Shubham Bansal
# @Date:   2018-08-26 01:03:45
# @Last Modified by:   Shubham Bansal
# @Last Modified time: 2018-08-26 01:26:21
import graphene
from graphene_django import DjangoObjectType

from .models import Links


class LinkType(DjangoObjectType):
  class Meta:
    model = Links


class Query(graphene.ObjectType):
  links = graphene.List(LinkType)

  def resolve_links(self, info, **kwargs):
    return Links.objects.all()


# Mutation
class CreateLink(graphene.Mutation):
  id = graphene.Int()
  url = graphene.String()
  description = graphene.String()

  # arguments
  class Arguments:
    url = graphene.String()
    description = graphene.String()

  # the mutation function
  def mutate(self, info, url, description):
    link = Links(url=url, description=description)
    link.save()

    return CreateLink(
      id=link.id,
      url=link.url,
      description=link.description,
    )


class Mutation(graphene.ObjectType):
  create_link = CreateLink.Field()
