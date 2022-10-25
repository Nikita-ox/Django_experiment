from rest_framework import routers
from .api import TodoViewSet

router = routers.DefaultRouter()  # Дефолтный роутер
router.register('api/todo', TodoViewSet, 'todo')  # Регестрирует апи урл, с кверисетом

urlpatterns = router.urls
