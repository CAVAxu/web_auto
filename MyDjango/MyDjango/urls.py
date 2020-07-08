"""MyDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from MyFirstDjango import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^hello/$', views.hello),
    url('login/', views.login,name='login1'),
    path('bingo/archive/<year>/<month>.html', views.archive),
    url(r'^bingo2/archive/(?P<year>[0-9]{4})/(?P<month>[0-9]{2}).html$', views.archive),
    url('register/', views.register,name='register'),
    url('personInfo/', views.personInfo),
    url('navlist/', views.navigationList)
]
