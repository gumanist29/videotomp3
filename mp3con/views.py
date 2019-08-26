from django.shortcuts import render
from django.http import HttpResponse
from .models import Utuber
from django.views import generic
from .redis import download_mp3


class HomeView(generic.TemplateView):
    def get(self, request):
        return render(request,'index.html')

    def post(self, request):
        url = request.POST.get('url')
        msg = download_mp3(url)
        if msg:
            return HttpResponse(msg)
        Utuber.objects.create(name=url)
        # new_utuber.save()
        return HttpResponse("Downloaded check in your Folder")




def stories(request):
    all_link_list = Utuber.objects.all()
    context = {'all_link_list': all_link_list}
    return render(request, 'base.html', context)

