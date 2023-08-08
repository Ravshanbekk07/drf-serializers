from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.forms.models import model_to_dict

from .models import Task
from .serializers import TaskSerializer


@api_view(['GET'])
def task_list(request: Request):
    task = Task.objects.first()
    serializer = TaskSerializer(task)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

