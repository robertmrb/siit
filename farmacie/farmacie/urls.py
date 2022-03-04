"""farmacie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from farmacie.views import homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    #homepage
    path('', homepage, name='homepage'),

    #login/logout
    path('login/', include('django.contrib.auth.urls')),

    #pacienti
    path('pacienti/', include('pacienti.urls')),

    #medicamente
    path('medicamente/', include('medicamente.urls')),

    # retete
    path('retete/', include('retete.urls')),

    # register
    path('register/', include('users.urls')),
]
