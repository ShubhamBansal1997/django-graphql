# -*- coding: utf-8 -*-
# @Author: Shubham Bansal
# @Date:   2018-08-26 01:03:45
# @Last Modified by:   Shubham Bansal
# @Last Modified time: 2018-08-26 01:12:02
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
