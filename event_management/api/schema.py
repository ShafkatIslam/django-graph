import graphene
from django.contrib.auth.models import User
from graphene_django.types import DjangoObjectType
from .models import Event, Event_member, Location
from django.db.models import Max, Count

class LocationType(DjangoObjectType):
    class Meta:
        model = Location


class EventType(DjangoObjectType):
    location = graphene.Field(LocationType)

    class Meta:
        model = Event

class EventMemberType(DjangoObjectType):
    class Meta:
        model = Event_member

class Query(graphene.ObjectType):
    all_events = graphene.List(EventType)
    event = graphene.Field(EventType, id = graphene.Int())
    event_list = graphene.List(EventType, name = graphene.String())
    event_all_members = graphene.Field(EventType)

    def resolve_all_events(self, info, **kwargs):
        return Event.objects.all()

    def resolve_event(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Event.objects.get(pk=id)
        return None

    def resolve_event_list(self, info, **kwargs):
        name = kwargs.get('name')
        if name is not None:
            user = User.objects.get(username=name)
            id = user.pk
            if id is not None:
                memberId = []
                event_member = Event_member.objects.filter(user_id=id)
                for member in event_member:
                    memberId.append(member.event_id)
                event_name = Event.objects.filter(id__in=memberId)
                print(memberId)
                return event_name
            return None
        return None

    def resolve_event_all_members(self, info, **kwargs):
        users = User.objects.all().count()
        query_result = Event_member.objects.values('event_id').order_by().annotate(event_count=Count('event_id'))
        maxval = max(query_result, key=lambda x: x['event_count'])

        max_event_id = maxval['event_id']
        max_event_id_count = maxval['event_count']
        print(users)
        print(maxval)
        if users == max_event_id_count:
            event_name = Event.objects.get(pk=max_event_id)
            return event_name
        return None


class EventCreateMutation(graphene.Mutation):

    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        location_name = graphene.String(required=True)

    event = graphene.Field(EventType)

    def mutate(self,info,name,description,location_name):
        location = Location.objects.get(name=location_name)
        if not Event.objects.filter(name=name,description=description,location=location):
            event = Event.objects.create(name=name, description=description, location=location)
            return EventCreateMutation(event=event)
        else:
            return None

class EventLocationUpdateMutation(graphene.Mutation):

    class Arguments:
        location_name = graphene.String()
        id = graphene.ID(required=True)

    event = graphene.Field(EventType)

    def mutate(self,info,id,location_name):
        location = Location.objects.get(name=location_name)
        event = Event.objects.get(pk=id)
        if location_name is not None:
            event.location = location
        event.save()

        return EventCreateMutation(event=event)

class DeleteMemberMutation(graphene.Mutation):

    class Arguments:
        user_name = graphene.String()
        event_name = graphene.String()

    event = graphene.Field(EventMemberType)

    def mutate(self,info,user_name,event_name):
        user_info = User.objects.get(username=user_name)
        event_info = Event.objects.get(name=event_name)

        user_id = user_info.pk
        event_id = event_info.pk

        event = Event_member.objects.get(user_id=user_id,event_id=event_id)
        event.delete()

        return EventCreateMutation(event=None)

class Mutation:
    create_event = EventCreateMutation.Field()
    update_event_location = EventLocationUpdateMutation.Field()
    delete_user = DeleteMemberMutation.Field()


