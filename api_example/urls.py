"""api_example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import languages

#from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    )

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include('languages.urls')),
    url('^api-auth/', include('rest_framework.urls')),#spd : display login/logout button
    url('^api/token/$', TokenObtainPairView.as_view()),
    url('^api/token/refresh$', TokenRefreshView.as_view()),
    url('^logout/$', languages.views.LogoutView.as_view({'get': 'list'})),
]
