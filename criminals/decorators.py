from django.http import HttpResponse
from django.shortcuts import redirect,render
from interview import views
def adminOnly(view_function):
    def wrapperFun(request, *args, **kwargs):
        if request.user.is_superuser:
            return view_function(request, *args, **kwargs)
        elif request.user.is_staff:
            return redirect('subadmin')
        else:
            return redirect('userlogin')
    return wrapperFun