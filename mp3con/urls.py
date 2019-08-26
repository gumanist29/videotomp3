
from django.urls import path
from mp3con.views import  HomeView
from .import views

# app_name = 'mp3con'
urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('stories/', views.stories, name="stories")

]
