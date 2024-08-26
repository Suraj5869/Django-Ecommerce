from django.urls import path
from E_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('new/', views.new, name='new'),
    path('rain/', views.rain, name='rain'),
    path('snow/', views.snow, name='snow'),
    path('allweather/', views.allweather, name='allweather'),
    path('shopall/', views.shopall, name='shopall'),
    path('hub/', views.hub, name='hub'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
]