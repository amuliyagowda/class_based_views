"""
URL configuration for classbasedviews project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('string_fbv/',string_fbv,name='string_fbv'),
    path('string_cbv/',string_cbv.as_view(),name='string_cbv'),
    path('html_fbv/',html_fbv,name='html_fbv'),
    path('html_cbv/',html_cbv.as_view(),name='html_cbv'),
    path('insert_fbv/',insert_fbv,name='insert_fbv'),
    path('insert_cbv/',insert_cbv.as_view(),name='insert_cbv'),
    path('template/',template.as_view(),name='template')
]
