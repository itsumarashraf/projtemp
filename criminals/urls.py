
from django.contrib import admin
from django.urls import path, include
from criminals import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('login',views.userlogin, name='userlogin'),
    path('logout',views.userlogout, name='userlogout'),
    path('register',views.register, name='register'),
    path('addcriminal', views.addcriminal, name='addcriminal'),
    path('editcriminal/<int:id>', views.editcriminal, name='editcriminal'),
    path('view/<int:id>', views.viewcriminal, name='viewcriminal'),
    path('view/updateprofile/<int:id>', views.updateprofile, name='updateprofile'),
    path('addcrime/<int:id>', views.addcrime, name='addcrime'),
    path('view/<int:id>/docs/', views.docs, name='docs')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
