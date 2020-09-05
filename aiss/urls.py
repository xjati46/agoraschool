"""aiss URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.views.generic import RedirectView
from home_app.views import RegistrationView, UserUpdateView, Page403View

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='home/')),
    path('home/', include('home_app.urls')),
    path('core/', include('account_app.urls')),
    path('extra/', include('extra_app.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path(
        'accounts/registration/',
        RegistrationView.as_view(),
        name='registration'),
    path(
        'accounts/update/<int:pk>/',
        UserUpdateView.as_view(),
        name='user-update'),
    path('denied-access/', Page403View.as_view(), name='denied-access'),
]
