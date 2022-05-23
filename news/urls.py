from django.urls import path
from . import views

urlpatterns =[
    path('',views.welcome,name='Welcome'),
    path('today/',views.news_of_day,name='newsToday')
    
    
    ]