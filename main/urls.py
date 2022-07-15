from django.urls import path

from main import views

app_name = "main"

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news, name='news'),
    path('about_university/', views.about_university, name='about_university'),
    path('chats_university/', views.chats_university, name='chats_university'),

]
