from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def register(request):
  if request.method == 'GET':
    return render(request, 'register.html')
  else:
    username = request.POST.get('username')
    first_name = request.POST.get('firstName')
    last_name = request.POST.get('lastName')
    email = request.POST.get('email')
    password = request.POST.get('password')
    
    user = User.objects.filter(username=username).first()
    
    if user:
      return HttpResponse("Já existe um usuário com esse nome")
    
    user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
    user.save()
    
    return redirect('plataforma') #HttpResponse("Usuário cadastrado com sucesso!")


def log_in(request):
  if request.method == 'GET':
    return render(request, 'login.html')
  else:
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    user = authenticate(username=username, password=password)
    
    if user:
      return redirect('plataforma')
    else:
      return HttpResponse("Usuário ou senha invalidados")

@login_required(login_url='auth:login')
def plataforma(request):
  return HttpResponse("Plataforma")