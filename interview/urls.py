
from django.contrib import admin
from django.urls import path, include
from interview import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.subadmin, name='subadmin'),
    path('view/<int:id>', views.viewquestions, name='viewquestions'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
