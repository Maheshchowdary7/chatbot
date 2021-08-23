from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('chatbot', views.chatbot, name = 'chatbot'),
    path('', views.HomePageView.as_view(), name='home'),
    path('process', views.process, name='process'),
    url('signup', views.signup, name='signup')
]