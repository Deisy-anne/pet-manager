"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from apps.user.api.viewsets.user import UserDetail, UserList
from apps.user.api.viewsets.user_authentication import UserAuthenticationList
from apps.pet.api.viewsets import PetDetail, PetList




urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign-up/', UserList.as_view()),
    path('sign-in/', UserAuthenticationList.as_view()),
    path('profile-details/<pk>/', UserDetail.as_view()),
    path('pets/', PetList.as_view()),
    path('pets/<pk>/', PetDetail.as_view()),
]
