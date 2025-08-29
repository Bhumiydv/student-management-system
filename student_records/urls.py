"""
URL configuration for student_records project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from students.views import index
from students.views import about
from students.views import contact
from students.views import login
from students.views import admin_home
from students.views import add_student
from students.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('about',about,name='about'),
    path('contact',contact,name='contact'),
    path('login',login,name='login'),
    path('admin_dashboard',admin_home,name='admin_dashboard'),
    path('add_student',add_student,name="add_student"),
    path('view_students',view_students,name="view_students"),
    path('edit_students/<int:id>',edit_students,name='edit_students'),
    path('del_students/<int:id>',del_students,name='del_students'),
    path('search',search_data,name='search'),
    path('search_stu',search_stu,name="search_stu"),
    path('logout',Logout,name='logout'),
    path('account',account,name='account'),
    path('change_pass',change_pass,name='change_pass')
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)