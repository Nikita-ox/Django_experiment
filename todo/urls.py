from django.urls import path
from rest_framework import routers

from todo import views
from todo.views import get
from .api import TodoViewSet, SkillViewSet

router = routers.DefaultRouter()  # Дефолтный роутер
router.register('api/todo', TodoViewSet, 'todo')  # Регестрирует апи урл, с кверисетом
router.register('api/skill', SkillViewSet, 'skill')

urlpatterns = router.urls
