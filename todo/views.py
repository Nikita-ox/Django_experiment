from django.http import JsonResponse
from django.shortcuts import render
from django.template.context_processors import request
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView

from .models import Skill


def get(request):
    if request.method == "GET":
        skills = Skill.objects.all()

        response = []
        for skill in skills:
            response.append({
                'id': skill.id,
                'name': skill.name
            })
        return JsonResponse(response, safe=False, json_dumps_params={
            'ensure_askii': False
        })
