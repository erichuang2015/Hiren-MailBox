from django.urls import path, re_path
from mail import views

urlpatterns = [
    path('', views.inbox, name='inbox'),
]