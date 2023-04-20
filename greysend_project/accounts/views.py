from django.shortcuts import render
from .models import AccountUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login


# Create your views here.
def index(request):
    return render(request, 'index.html')


def list_users(request):
    users = User.objects.all()
    return render(request, 'list_users.html',
      {'users': users})    

def signup(request):
    # breakpoint()
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(request.POST['username'],
                                            password=request.POST['password1'])
            user.save()
            login(request, user)
        return render(request, 'signup.html', {"form":UserCreationForm})  
# Compare this snippet from greysend_project/accounts/models.py: