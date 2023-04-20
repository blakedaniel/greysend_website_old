from django.shortcuts import render
from .models import ChatUser
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


def list_users(request):
    users = ChatUser.objects.all()
    return render(request, 'list_users.html',
      {'users': users})    

def signup(request):
    # breakpoint()
    return render(request, 'signup.html', {"form":UserCreationForm})  
# Compare this snippet from greysend_project/accounts/models.py: