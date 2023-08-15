from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def detail(request):
    return render(request, "detail.html")

def account(request):
    return render(request, "accounts/customerCreate.html")