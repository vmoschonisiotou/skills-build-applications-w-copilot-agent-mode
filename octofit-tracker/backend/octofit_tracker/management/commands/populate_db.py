from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team=marvel),
            User.objects.create(email='captain@marvel.com', name='Captain America', team=marvel),
            User.objects.create(email='spiderman@marvel.com', name='Spider-Man', team=marvel),
            User.objects.create(email='batman@dc.com', name='Batman', team=dc),
            User.objects.create(email='superman@dc.com', name='Superman', team=dc),
            User.objects.create(email='wonderwoman@dc.com', name='Wonder Woman', team=dc),
        ]

        # Create activities
        Activity.objects.create(user=users[0], type='run', duration=30, points=50, date=timezone.now())
        Activity.objects.create(user=users[1], type='walk', duration=60, points=40, date=timezone.now())
        Activity.objects.create(user=users[2], type='strength', duration=45, points=60, date=timezone.now())
        Activity.objects.create(user=users[3], type='run', duration=25, points=45, date=timezone.now())
        Activity.objects.create(user=users[4], type='walk', duration=50, points=35, date=timezone.now())
        Activity.objects.create(user=users[5], type='strength', duration=40, points=55, date=timezone.now())

        # Create workouts
        w1 = Workout.objects.create(name='Morning Cardio', description='A quick morning run.')
        w2 = Workout.objects.create(name='Strength Circuit', description='Pushups, squats, lunges.')
        w1.suggested_for.add(marvel)
        w2.suggested_for.add(dc)

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, total_points=150)
        Leaderboard.objects.create(team=dc, total_points=135)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
