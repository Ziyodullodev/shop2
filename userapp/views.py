from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from userapp.models import Client, Adress


class LoginView(View):
    def get(self, request):
        return render(request, 'page-user-login.html')

    def post(self, request):
        users = authenticate(username=request.POST['email'], password=request.POST['password1'])
        if users is None:
            return redirect('page-user-login')
        else:
            login(request, users)
            return redirect('page-index')


class RegView(View):
    def get(self, request):
        return render(request, 'page-user-register.html')

    def post(self, request):
        if request.POST.get("password1") != request.POST.get("password2"):
            return redirect("page-user-register")
        a = User.objects.create_user(
            username=request.POST['email'],
            password=request.POST['password1']
        )
        c = Client.objects.create(
            ism=request.POST["l"] + " " + request.POST["f"],
            email=request.POST['email'],
            jins=request.POST["gender"],
            user=a
        )
        Adress.objects.create(
            davlat=request.POST["davlat"],
            shahar=request.POST["shahar"],
            kocha=request.POST["street"],
            uy=request.POST["house"],
            zipcode=request.POST["zipc"],
            mijoz=c
        )
        from django.core.mail import EmailMessage
        from django.conf import settings
        from django.template.loader import render_to_string
        t = render_to_string("register-email.html", {"user": c})
        email = EmailMessage(
            "Alistyle do'koniga xush kelibsiz",
            t,
            settings.EMAIL_HOST_USER,
            [c.email],
        )
        email.fail_silently = False
        email.send()
        return redirect('page-user-login')

def Logout(request):
    logout(request)
    return redirect('page-index-2')

class ClientView(View):
    def get(self, request, pk):
        client = Client.objects.get(id=pk)
        adress = Adress.objects.filter(mijoz=client)
        return render(request, "page-profile-main.html", {"adress": adress, "client": client})

