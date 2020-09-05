from django.urls import path
from home_app import views


app_name = 'home-app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]
