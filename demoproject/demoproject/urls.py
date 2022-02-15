
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about-page'),
    path('', views.home, name='home'),
    path('articles/',include('articles.urls')),
]
