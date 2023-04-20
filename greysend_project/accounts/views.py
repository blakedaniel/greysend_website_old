from django.shortcuts import render
from .models import ChatUser

# Create your views here.
def index(request):
    return render(request, 'index.html')


def list_users(request):
    users = ChatUser.objects.all()
    return render(request, 'list_users.html',
      {'users': users})     