from django.urls import path, re_path
from mail import views

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('compose/', views.compose, name='compose'),
    path('sent/', views.sent, name='sent'),
    path('draft/', views.draft, name='draft'),
]
