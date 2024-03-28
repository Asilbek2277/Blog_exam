from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect
from django.views import View

from core import settings
from .models import *


class SMSClient:
    pass


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        User.objects.create(
            firs_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            username=request.POST.get('username'),
            password=request.POST.get('password'),
        )
        return redirect('login')



class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        profile=authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if profile is not None:
            profile=request.user
            login(request, profile)
            return redirect('maqolalar')
        return redirect('register')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')


class MaqolalarView(View):
    def get(self, request):
        context={
            'maqolalar': Maqola.objects.all(),
            'muallif': Muallif.objects.all()
        }
        return render( request, 'maqolalar.html', context)
    def post(self, request):
        Maqola.objects.create(
            sarlavha=request.POST['sarlavha'],
            sana=request.POST['sana'],
            mavzu=request.POST['mavzu'],
            matn=request.POST['matn'],
            muallif=Muallif.objects.get(id=request.POST['muallif']),
        )
        return redirect('maqolalar')
def bitta_maqola(request, pk):
    context={
        'maqola': Maqola.objects.get(id=pk)
    }
    return render(request, 'bitta_maqola.html', context)



