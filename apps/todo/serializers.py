from rest_framework import serializers

from apps.todo.models import Todo

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields  = '__all__'