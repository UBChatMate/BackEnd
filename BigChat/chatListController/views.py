from django.shortcuts import render

# Create your views here.
import requests
import json


from django.core import serializers
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse
from django.views.generic import View

from auth.models import Users
from .models import getChatListModel
from .models import getMessageHistoryModel

def index(request):
     return HttpResponse("Auth POST")


class ChatList(View):
    
    def get(self, requests):
         return HttpResponse("ChatList GET")

    def post(self, requests):
         return HttpResponse("ChatList POST")


class MessageHistory(View):

    def get(self, requests):
         return HttpResponse("Messages GET")

    def post(self, requests):
         return HttpResponse("Messages POST")

