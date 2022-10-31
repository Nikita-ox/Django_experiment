from rest_framework import serializers

from .models import Todo, Skill


class TodoSerializer(serializers.ModelSerializer):
    '''Сереализовываем нашу модель в json представление'''

    class Meta:
        model = Todo
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    '''Сереализовываем нашу модель в json представление'''

    class Meta:
        model = Skill
        fields = '__all__'
