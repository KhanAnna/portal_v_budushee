from django.shortcuts import render


def base(request):
    return render(request, "main/base.html", {})


def home(request):
    return render(request, "main/home.html", {})


def news(request):
    return render(request, "main/news.html", {})


def about_university(request):
    return render(request, "main/about_university.html", {})


def chats_university(request):
    return render(request, "main/chats_university.html", {})
