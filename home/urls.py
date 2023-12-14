from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    re_path("^$", views.index, name="index"),
    #re_path("^main/$", views.main, name="main"),
    # path('login', views.loginPage, name='login'),
    re_path('accounts/register', views.registerPage, name='register'),
    re_path("^me/$", views.me, name="me"),
    re_path("^contact/$", views.contact, name="contact"),
    # path('logout', views.doLogout, name='logout')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
