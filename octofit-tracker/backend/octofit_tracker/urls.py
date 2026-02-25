"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
import os

from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

# build the base URL depending on whether we are in a codespace
codespace_name = os.environ.get('CODESPACE_NAME')
if codespace_name:
    # use HTTPS for codespace - the cert is valid for the app.github.dev domain
    base_url = f"https://{codespace_name}-8000.app.github.dev"
else:
    # local development can use http to avoid HTTPS/cert issues
    base_url = "http://localhost:8000"

router = DefaultRouter()
# register viewsets imported from views
router.register(r'users', views.UserViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'activities', views.ActivityViewSet)
router.register(r'workouts', views.WorkoutViewSet)
router.register(r'leaderboard', views.LeaderboardEntryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.api_root, name='api_root'),
    path('api/', include(router.urls)),
]
