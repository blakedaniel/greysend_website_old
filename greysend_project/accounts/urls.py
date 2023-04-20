from accounts import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('members', views.list_users, name='list_users'),
    path('signup',views.signup, name='signup'),
]