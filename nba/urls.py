"""Customers URLs."""

# Django
from django.urls import path, include

# Django REST Framework
# https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/#using-routers
from rest_framework.routers import DefaultRouter

# Views
from nba import views

router = DefaultRouter()
router.register(r'nbaplayers', views.nbaPlayersViewSet, basename='nbaplayers')

urlpatterns = [
    path('', include(router.urls)),
]