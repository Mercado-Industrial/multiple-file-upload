import time

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View

from .forms import FotoForm
#from .models import Photo
from .models import Foto


class BasicUploadView(View):
    def get(self, request):
        photos_list = Foto.objects.all()
        #return render(self.request, 'fotos/basic_upload/index.html', {'photos': photos_list})
        return render(self.request, 'photos/basic_upload/index.html', {'photos': photos_list})

    def post(self, request):
        form = FotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            foto = form.save()
            data = {'is_valid': True, 'name': foto.file.name, 'url': foto.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


class ProgressBarUploadView(View):
    def get(self, request):
        photos_list = Foto.objects.all()
        #return render(self.request, 'fotos/progress_bar_upload/index.html', {'fotos': photos_list})
        return render(self.request, 'photos/progress_bar_upload/index.html', {'fotos': photos_list})

    def post(self, request):
        time.sleep(1)  # You don't need this line. This is just to delay the process so you can see the progress bar testing locally.
        form = FotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            foto = form.save()
            data = {'is_valid': True, 'name': foto.file.name, 'url': foto.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


class DragAndDropUploadView(View):
    def get(self, request):
        photos_list = Foto.objects.all()
        return render(self.request, 'photos/drag_and_drop_upload/index.html', {'fotos': photos_list})

    def post(self, request):
        form = FotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': foto.file.name, 'url': foto.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


def clear_database(request):
    for photo in Foto.objects.all():
        photo.file.delete()
        photo.delete()
    return redirect(request.POST.get('next'))
