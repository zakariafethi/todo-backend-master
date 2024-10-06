from rest_framework import serializers

from todo.models import Todo, TodoList


class TodoSerializer(serializers.ModelSerializer):

    dueDate = serializers.DateField(source='due_date')

    class Meta:
        model = Todo
        exclude = ['due_date']


class TodoListSerializer(serializers.ModelSerializer):

    class Meta:
        model = TodoList
        fields = '__all__'


class TodoListDetailSerializer(serializers.ModelSerializer):

    todos = TodoSerializer(source='todo_set', many=True)

    class Meta:
        model = TodoList
        fields = '__all__'
