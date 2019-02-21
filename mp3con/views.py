from django.shortcuts import render
from django.http import HttpResponse
from .models import Utuber
from django.views import generic


class HomeView(generic.TemplateView):
    def get(self, request):
        return render(request,'index.html')

    def post(self, request):
        urls = request.POST.get('url')
        Utuber.download_mp3(urls, urls)
        return HttpResponse("Perfect")


class UtuberView(generic.ListView):
    model = Utuber
    template_name = 'index.html'
    context_object_name = 'all_list'

    def link(self):
        return Utuber.objects.all()

