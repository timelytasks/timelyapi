"""app URL Configuration

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
from django.urls import path, include
from rest_framework import routers
from app.users.views import UserViewSet
from app.projects.views import ProjectViewSet, TaskViewSet

version = "v1"
router = routers.DefaultRouter()
router.register(r"projects", ProjectViewSet, basename="projects")
router.register(r"tasks", TaskViewSet, basename="tasks")
router.register(r"users", UserViewSet, basename="users")

urlpatterns = [
    path(f"api/{version}/auth/", include("rest_auth.urls")),
    path(f"api/{version}/auth/registration/", include("rest_auth.registration.urls")),
    path(f"api/{version}/", include(router.urls)),
    path("admin/", admin.site.urls),
]
