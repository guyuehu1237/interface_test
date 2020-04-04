"""secondinterface URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from inttest import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/',views.add),
    path('query/',views.query),
    path('delete/',views.delete),
    path('change/',views.change),
    path('',views.interface),
    path('loadall/',views.loadall),
    path('action/',views.action),
    path('cars/',views.cars),
    path('compare/',views.compare),
    path('getParam/',views.getParam),
    path('person/',views.person)
]
