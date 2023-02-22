from django.shortcuts import render
from .forms import LoginForms, CadastroForms


def login(request):
    form = LoginForms()
    return render(request, "usuario/login.html", {"form":form})


def cadastro(request):
    form = CadastroForms()
    return render(request, "usuario/cadastro.html", {"form":form})