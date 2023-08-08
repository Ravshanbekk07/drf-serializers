from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.forms.models import model_to_dict

from .models import Task


@api_view(['GET'])
def task_list(request: Request):
    tasks = Task.objects.all()
    data = []
    for task in tasks:
        data.append(model_to_dict(task))
    return Response(data=data, status=status.HTTP_200_OK)

