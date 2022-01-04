from django.urls import path, include
from updateprofile import views


urlpatterns = [
    path('',views.updateprofile, name='updateprofile')
]