from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Team, Activity, Workout, LeaderboardEntry
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, WorkoutSerializer, LeaderboardEntrySerializer
import os

@api_view(['GET'])
def api_root(request, format=None):
    """Return a small index of available API endpoints using the correct base URL."""
    codespace_name = os.environ.get('CODESPACE_NAME')
    if codespace_name:
        base = f"https://{codespace_name}-8000.app.github.dev/api"
    else:
        base = "http://localhost:8000/api"

    return Response({
        'users': f"{base}/users/",
        'teams': f"{base}/teams/",
        'activities': f"{base}/activities/",
        'workouts': f"{base}/workouts/",
        'leaderboard': f"{base}/leaderboard/",
    })


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

class LeaderboardEntryViewSet(viewsets.ModelViewSet):
    queryset = LeaderboardEntry.objects.all().order_by('-points')
    serializer_class = LeaderboardEntrySerializer
