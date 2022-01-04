from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('criminals.urls')),
    path('subadmin/', include('interview.urls')),
    path('view/updateprofile/<int:id>', include('updateprofile.urls'))
]
