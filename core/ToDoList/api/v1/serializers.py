from rest_framework import serializers
from ToDoList.models import Tasks

# class ToDoListSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     id = serializers.IntegerField()
#     task = serializers.CharField()
#     IsDone = serializers.BooleanField()


class ToDoListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tasks
        fields = ['user','email','id', 'task', 'IsDone', 'created_date', 'updated_date']