
from django.contrib import admin
from django.urls import path, include
from interview import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.subadmin, name='subadmin'),
    path('profile/<int:id>',views.profile,name='profile'),
    path('delete/<int:id>',views.deletequeans,name='deletequeans'),
    path('reviews/<int:id>',views.reviews,name='reviews'),
    path('view/<int:id>', views.viewquestions, name='viewquestions')
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
