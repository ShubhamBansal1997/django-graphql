# -*- coding: utf-8 -*-
# @Author: Shubham Bansal
# @Date:   2018-08-26 03:32:07
# @Last Modified by:   Shubham Bansal
# @Last Modified time: 2018-08-26 03:47:33
import graphene
import django_filters
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Links, Vote

class LinkFilter(django_filters.FilterSet):
  class Meta(object):
    models = Links
    fields = ['url', 'description']


class LinkNode(DjangoObjectType):
  class Meta:
    model = Links
    interfaces = (graphene.relay.Node, )


class VoteNote(DjangoObjectType):
  class Meta:
    model = Vote
    interfaces = (graphene.relay.Node, )


class RelayQuery(graphene.ObjectType):
  relay_link = graphene.relay.Node.Field(LinkNode)
  relay_links = DjangoFilterConnectionField(LinkNode, filterset_class=LinkFilter)


class RelayCreateLink(graphene.relay.ClientIDMutation):
  link = graphene.Field(LinkNode)

  class Input:
    url = graphene.String()
    description = graphene.String()

  def mutate_and_get_payload(root, info, **input):
    user = info.context.user or None

    link = Links(
        url=input.get('url'),
        description=input.get('description'),
        posted_by=user
    )
    link.save()

    return RelayCreateLink(link=link)


class RelayMutation(graphene.AbstractType):
  relay_create_link = RelayCreateLink.Field()
