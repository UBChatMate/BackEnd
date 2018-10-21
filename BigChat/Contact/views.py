from django.shortcuts import render

# Create your views here.
import requests
from .models import Contact
from auth.models import Users
from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from django.views.generic import View

def index(request):
     return HttpResponse("Contact POST")

class Contacts(View):
    def get(self, request):
        token = request.GET.get("token")
        print('get')
        return JsonResponse(getContact(token))
    
    # def addNew(self, request):
    #     token = request.GET.get("token")
    #     return JsonResponse(addNewUser(token))



def getUserId(token):
    try:
        user = Users.objects.get(token=token)
        if 'error' in user:
            return {'error': "Failed to achieve user. User not found."}
    except Exception:
        return {'error': "Failed to update token. User not found."}
    return user


def addNewUser(token):
    try:
        contact = Contact.object.raw('INSERT INTO contact_list (user_id, friend_id, date_added, date_modified) VALUES ((SELECT user_id FROM user_profile WHERE token = %s), NULL, NOW(), NOW())', [token])
        return {'success': "Succesfully added new user"}
    except Exception:
        return {'error': "Failed to add new user."}

def getContact(token):
    try:
        return Contact.object.raw('SELECT friend_id from public.\"contact_list\" where user_id =  (SELECT user_id FROM user_profile WHERE token = %s)', [token])
    except Exception:
        return {'error': "Failed to get contact."}

def addFriend(userId, friendId):
    try:
        Contact.object.raw('UPDATE contact_list SET friend_id = array_append(friend_id, %d), date_modified = NOW() WHERE user_id = %d', [friendId], [userId])
        return {'success': "Succesfully added contacts"}
    except Exception:
        return {'error': "Failed to add contact."}

