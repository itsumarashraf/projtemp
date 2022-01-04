
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
    path('TagFilter/<slug:tslug>',views.filterbytag, name='filterbytag'),
    path('view_criminals', views.viewcriminals, name='viewcriminals'),
    path('view_trash/', views.veiwtrashcriminals, name='veiwtrashcriminals'),
    path('trash/<int:id>', views.trashcriminal, name='trashcriminal'),
    path('restore/<int:id>', views.restore, name='restore'),
    path('permemant_delete/<int:id>', views.permemantdelete, name='permemantdelete'),
    path('addcriminal', views.addcriminal, name='addcriminal'),
    path('pending_cases', views.pendingcases, name='pendingcases'),
    path('editcriminal/<int:id>', views.editcriminal, name='editcriminal'),
    path('view/<int:id>', views.viewcriminal, name='viewcriminal'),
    path('addcrime/<int:id>', views.addcrime, name='addcrime'),
    path('view/<int:id>/upload_docs/', views.uploaddocuments, name='uploaddocuments'),
    path('view/<int:id>/record/', views.recordvideo, name='recordvideo'),
    path('view/<int:id>/videos/', views.criminalvid, name='criminalvid')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
