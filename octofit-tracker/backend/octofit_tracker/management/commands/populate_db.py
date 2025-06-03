# This script populates test data for users, teams, activities, leaderboard, and workouts collections in octofit_db.

from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Users
        user1 = User.objects.create(email='alice@example.com', name='Alice', password='alicepass')
        user2 = User.objects.create(email='bob@example.com', name='Bob', password='bobpass')
        user3 = User.objects.create(email='carol@example.com', name='Carol', password='carolpass')

        # Teams (using plain dicts for members)
        team1 = Team.objects.create(name='Team Alpha', members=[
            {"email": user1.email, "name": user1.name},
            {"email": user2.email, "name": user2.name}
        ])
        team2 = Team.objects.create(name='Team Beta', members=[
            {"email": user3.email, "name": user3.name}
        ])

        # Activities (reference by user email)
        Activity.objects.create(user_email=user1.email, activity_type='run', duration=30)
        Activity.objects.create(user_email=user2.email, activity_type='walk', duration=45)
        Activity.objects.create(user_email=user3.email, activity_type='strength', duration=20)

        # Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups')
        Workout.objects.create(name='Situps', description='Do 30 situps')

        # Leaderboard (reference by team name)
        Leaderboard.objects.create(team_name=team1.name, points=100)
        Leaderboard.objects.create(team_name=team2.name, points=80)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
