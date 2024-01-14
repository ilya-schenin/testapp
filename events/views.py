from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes
from .models import Event
from organization.models import Organization
import threading
import queue
import time

event_queue = queue.Queue()


def create_event_with_delay(event_data, organization_ids):
    time.sleep(60)
    organization = Organization.objects.filter(id__in=organization_ids)
    event = Event.objects.create(
        title=event_data['title'],
        description=event_data['description'],
        image=event_data['image']
    )
    for item in organization:
        event.organization.add(item)


@api_view(['POST'])
def add_event(request):
    data = request.data
    organization_ids = data['organization']
    event_creation_thread = threading.Thread(target=create_event_with_delay, args=(data, organization_ids))
    event_creation_thread.start()
    return Response('ok')
