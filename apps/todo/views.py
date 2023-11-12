from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.todo.models import Todo
from apps.todo.serializers import ProductSerializer

# Create your views here.
class TodoViewSet(GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = Todo.objects.all()
    serializer_class = ProductSerializer
    Permission_classes = [AllowAny, ]
