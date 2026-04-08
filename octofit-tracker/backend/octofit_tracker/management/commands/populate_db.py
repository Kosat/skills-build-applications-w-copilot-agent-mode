from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear all data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='dc', description='DC superheroes')

        # Users
        users = [
            User.objects.create(email='tony@stark.com', name='Tony Stark', team='marvel', is_superhero=True),
            User.objects.create(email='steve@rogers.com', name='Steve Rogers', team='marvel', is_superhero=True),
            User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team='dc', is_superhero=True),
            User.objects.create(email='clark@kent.com', name='Clark Kent', team='dc', is_superhero=True),
        ]

        # Activities
        Activity.objects.create(user=users[0], type='run', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='swim', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[2], type='cycle', duration=60, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='fly', duration=120, date=timezone.now().date())

        # Workouts
        Workout.objects.create(name='Pushups', description='Upper body', suggested_for='marvel')
        Workout.objects.create(name='Flight', description='Aerial', suggested_for='dc')

        # Leaderboard
        Leaderboard.objects.create(team=marvel, points=200)
        Leaderboard.objects.create(team=dc, points=180)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
