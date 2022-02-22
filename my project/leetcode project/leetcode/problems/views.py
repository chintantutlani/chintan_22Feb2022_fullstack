from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

def createddd(request):

    return JsonResponse(data={'msg':'hi'})