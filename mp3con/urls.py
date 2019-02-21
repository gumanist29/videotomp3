
from django.urls import path
from mp3con.views import  HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='index')

]
