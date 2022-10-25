from .models import Todo
from rest_framework import viewsets, permissions
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()  # Наши объекты в базе данных
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TodoSerializer  # класс сериалайзера
