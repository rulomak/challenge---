from rest_framework import serializers
from .models import ToDoList

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ('id', 'title', 'description', 'create_at')
        read_only_fields = ('create_at', )