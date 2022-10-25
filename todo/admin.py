from django.contrib import admin

from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'date', 'done')  # Чтов идим в спимке
    list_display_links = ('id', 'title')  #
    search_fields = ('id', 'title', 'description')  # По каким полям можем искать
    list_editable = ('done')  # Что можем изменить прямо в списке
    list_filter = ('done')  # По каким параметрам можем фильтровать
