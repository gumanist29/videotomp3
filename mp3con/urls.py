
from django.urls import path
from mp3con.views import  HomeView
from .import views


urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('stories/', views.stories, name="stories")

]
