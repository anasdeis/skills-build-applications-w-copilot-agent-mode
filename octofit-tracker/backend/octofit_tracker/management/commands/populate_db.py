
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password'),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='password'),
            User.objects.create_user(username='batman', email='batman@dc.com', password='password'),
            User.objects.create_user(username='superman', email='superman@dc.com', password='password'),
        ]

        # Create Activities
        Activity.objects.create(user='ironman', activity_type='Running', duration=30, team='Marvel')
        Activity.objects.create(user='spiderman', activity_type='Cycling', duration=45, team='Marvel')
        Activity.objects.create(user='batman', activity_type='Swimming', duration=60, team='DC')
        Activity.objects.create(user='superman', activity_type='Yoga', duration=20, team='DC')

        # Create Leaderboard
        Leaderboard.objects.create(team='Marvel', points=75)
        Leaderboard.objects.create(team='DC', points=80)

        # Create Workouts
        Workout.objects.create(name='Hero HIIT', description='High intensity workout for heroes', suggested_for='Marvel')
        Workout.objects.create(name='Power Yoga', description='Yoga for super strength', suggested_for='DC')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
