from rest_framework import serializers
from .models import Task
from datetime import datetime


class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(allow_null=True)
    completed = serializers.BooleanField(default=False)
    created = serializers.DateTimeField(default=datetime.now())


    def to_representation(self, instance: Task):
        return {
            'id': instance.id,
            'info': f"{instance.title} - {instance.description}"
        }