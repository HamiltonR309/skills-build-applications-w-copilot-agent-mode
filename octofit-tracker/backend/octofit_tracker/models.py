from djongo import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Additional fields can be added here
    pass

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ArrayReferenceField(to=User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    calories_burned = models.PositiveIntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.activity_type} on {self.date}"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name

class LeaderboardEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.PositiveIntegerField(default=0)
    rank = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.points} pts"
