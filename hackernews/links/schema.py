# -*- coding: utf-8 -*-
# @Author: Shubham Bansal
# @Date:   2018-08-26 01:03:45
# @Last Modified by:   Shubham Bansal
# @Last Modified time: 2018-08-26 03:07:33
import graphene
from graphene_django import DjangoObjectType

from .models import Links, Vote
from users.schema import UserType


class LinkType(DjangoObjectType):
  class Meta:
    model = Links


class VoteType(DjangoObjectType):
  class Meta:
    model = Vote


class Query(graphene.ObjectType):
  links = graphene.List(LinkType)
  votes = graphene.List(VoteType)

  def resolve_links(self, info, **kwargs):
    return Links.objects.all()

  def resolve_votes(self, info, **kwargs):
    return Vote.objects.all()


# Mutation
class CreateLink(graphene.Mutation):
  id = graphene.Int()
  url = graphene.String()
  description = graphene.String()
  posted_by = graphene.Field(UserType)

  # arguments
  class Arguments:
    url = graphene.String()
    description = graphene.String()

  # the mutation function
  def mutate(self, info, url, description):
    user = info.context.user or None

    link = Links(
      url=url,
      description=description,
      posted_by=user,
    )
    link.save()

    return CreateLink(
      id=link.id,
      url=link.url,
      description=link.description,
      posted_by=link.posted_by,
    )

# Add the CreateVote mutation
class CreateVote(graphene.Mutation):
  user = graphene.Field(UserType)
  link = graphene.Field(LinkType)

  class Arguments:
    link_id = graphene.Int()

  def mutate(self, info, link_id):
    user = info.context.user or None
    if user.is_anonymous:
      raise Exception('You must be logged to vote!')

    link = Links.objects.filter(id=link_id).first()
    if not link:
      raise Exception('Invalid Link!')

    Vote.objects.create(
      user=user,
      link=link
    )
    return CreateVote(user=user, link=link)

# ADd the mutation to the mutation class
class Mutation(graphene.ObjectType):
  create_link = CreateLink.Field()
  create_vote = CreateVote.Field()
