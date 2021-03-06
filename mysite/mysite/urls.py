"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from blog.views import page_not_found
from rest_framework_jwt.views import obtain_jwt_token
import xadmin

urlpatterns = [
    path('admin/', admin.site.urls),
    # 集成xadmin
    path('xadmin/', xadmin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('myauth.urls', namespace = 'myauth')),
    path('', include('blog.urls', namespace = 'blog')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('comment/', include('comment.urls', namespace = 'comment')),
    path('tools/', include('tools.urls', namespace = 'tools')),
    path('api/', include('apis.urls', namespace = 'apis')),
    path('api-auth/', obtain_jwt_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # 加入这个才能显示media文件

# 全局404
handler404 = page_not_found
