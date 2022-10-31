from .models import Todo, Skill
from rest_framework import viewsets, permissions
from .serializers import TodoSerializer, SkillSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()  # Наши объекты в базе данных

    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TodoSerializer  # класс сериалайзера


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()  # Наши объекты в базе данных

    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SkillSerializer  # класс сериалайзера
