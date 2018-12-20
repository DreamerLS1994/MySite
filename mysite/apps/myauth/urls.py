# -*- coding: utf-8 -*-
from .views import profile_view,update_profile_view
from django.urls import path

app_name = '[myauth]'

urlpatterns = [
    path('profile/', profile_view,name='profile_url'),
    path('profile/update', update_profile_view,name='update_profile_url'),
    
]

