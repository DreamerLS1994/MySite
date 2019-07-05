from django.conf.urls import include
from django.urls import path
from .views import RubbishView, RubbishDetailView, RubbishCategoryView, RubbishCategoryDetailView
app_name = '[apis]'

urlpatterns = [
    path('laji/', RubbishView.as_view()),
    path('laji/<str:pk>/', RubbishDetailView.as_view()),
    path('lajifenlei/', RubbishCategoryView.as_view()),
    path('lajifenlei/<str:pk>/', RubbishCategoryDetailView.as_view()),

]

