
from django.contrib import admin
from django.urls import path,include
from . import views,user_login
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('base',views.base),
    path('',views.HOME,name='home'),
    # path('single/course',views.single_course,name='single_course'),
    path('accounts/register',user_login.reg,name='register'),
    path('afterlogin/',views.ho,name='afterlogin'),
    path('',include('django.contrib.auth.urls')),
]
