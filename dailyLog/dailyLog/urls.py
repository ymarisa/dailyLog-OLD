"""dailyLog URL Configuration

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
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from log import views

urlpatterns = [
    path('', views.api_root),
    path('admin/', admin.site.urls),
    path('habits/',
         views.HabitList.as_view(),
         name='user-habits'),
    path('logs/',
         views.LogList.as_view(),
         name='log-entries'),
    path('log/<int:pk>/',
         views.LogDetail.as_view(),
         name='log-detail'),
    path('habit/<int:pk>',
         views.HabitDetail.as_view(),
         name='habit-detail'),
    path('users/<int:pk>/',
         views.UserDetail.as_view(),
         name='user-detail'),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)

