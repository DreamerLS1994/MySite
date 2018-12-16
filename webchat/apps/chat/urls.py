
from django.contrib import admin
from django.urls import path
from .views import login_view
app_name="chat"

urlpatterns = [
    path('', login_view, name='login_url'),   

]
