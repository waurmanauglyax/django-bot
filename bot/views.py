from django.shortcuts import render
from django.http import HttpResponse

def bot_view(request, message):
    return HttpResponse(f"Ваше сообщение: {message}")
