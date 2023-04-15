# thumbnailer/views.py
import os
from celery import current_app
from django import forms  
from django.conf import settings  
from django.http import JsonResponse  
from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from .tasks import make_thumbnails
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm

class FileUploadForm(forms.Form):  
    image_file = forms.ImageField(required=True)
class HomeView(View):  
    def get(self, request):
        form = FileUploadForm()
        return render(request, 'thumbnailer/home.html', { 'form': form })
    def post(self, request):
        form = FileUploadForm(request.POST, request.FILES)
        context = {}
        if form.is_valid():
            file_path = os.path.join(settings.IMAGES_DIR, request.FILES['image_file'].name)
            with open(file_path, 'wb+') as fp:
                for chunk in request.FILES['image_file']:
                    fp.write(chunk)
            task = make_thumbnails.delay(file_path, thumbnails=[(128, 128)])
            context['task_id'] = task.id
            context['task_status'] = task.status
            return render(request, 'thumbnailer/home.html', context)
        context['form'] = form
        return render(request, 'thumbnailer/home.html', context)
class TaskView(View):  
    def get(self, request, task_id):
        task = current_app.AsyncResult(task_id)
        response_data = {'task_status': task.status, 'task_id': task.id}
        if task.status == 'SUCCESS':
            response_data['results'] = task.get()
        return JsonResponse(response_data)
def main(reqest):
    return render(reqest, 'thumbnailer/main.html')
def about_prj(reqest):
    return render(reqest, 'thumbnailer/about_prj.html')
def about_us(reqest):
    return render(reqest, 'thumbnailer/about_us.html')

def test(reqest):
    return render(reqest, 'thumbnailer/base.html')

def e_handler404(request, exception, template_name="thumbnailer/404.html"):
    response = render_to_response(template_name)
    response.status_code = 404
    return response

def e_handler500(request, *args, **argv):
    return render(request, 'thumbnailer/500.html', status=500)

#https://codedec.com/tutorials/user-login-and-logout-in-django/
def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account Created Successfully!!!')
            fm.save()
    else:
        fm = SignUpForm()
    return render(request,'thumbnailer/signup.html',{'form':fm})
#Login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Успешно вошел в систему!!!')
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request,'thumbnailer/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')
#Profile
def user_profile(request):
    if request.user.is_authenticated:
        return render(request,'thumbnailer/profile.html',{'name':request.user})
    else:
        return HttpResponseRedirect('/login/')
#Logout
def user_logout(request):
    logout(request)
    return render(request,'thumbnailer/logout.html')
