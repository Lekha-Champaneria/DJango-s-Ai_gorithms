from django.contrib import admin
from django.urls import path
from LandingPage import views

urlpatterns = [
    path('', views.index, name="home"),
    path('token_request',views.run_get_token),
    path('find_Track',views.run_get_song_details),
    path('end',views.end)
]