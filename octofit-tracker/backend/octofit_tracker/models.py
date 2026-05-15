
from djongo import models
from uuid import uuid4

class Team(models.Model):
    id = models.CharField(primary_key=True, default=lambda: str(uuid4()), editable=False, max_length=36)
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        db_table = 'teams'
    def __str__(self):
        return self.name

class User(models.Model):
    id = models.CharField(primary_key=True, default=lambda: str(uuid4()), editable=False, max_length=36)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='user_members')
    class Meta:
        db_table = 'users'
    def __str__(self):
        return self.name

class Activity(models.Model):
    id = models.CharField(primary_key=True, default=lambda: str(uuid4()), editable=False, max_length=36)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='user_activities')
    type = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    points = models.IntegerField()
    date = models.DateField()
    class Meta:
        db_table = 'activities'

class Workout(models.Model):
    id = models.CharField(primary_key=True, default=lambda: str(uuid4()), editable=False, max_length=36)
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.ManyToManyField('Team', related_name='workout_suggestions')
    class Meta:
        db_table = 'workouts'

class Leaderboard(models.Model):
    id = models.CharField(primary_key=True, default=lambda: str(uuid4()), editable=False, max_length=36)
    team = models.OneToOneField('Team', on_delete=models.CASCADE, related_name='team_leaderboard')
    total_points = models.IntegerField(default=0)
    class Meta:
        db_table = 'leaderboard'
        db_table = 'leaderboard'
