from django.test import TestCase
from django.contrib.auth.models import User
from .models import Team, Activity, Leaderboard, Workout

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Test Team")
        self.assertEqual(team.name, "Test Team")

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(username="testuser")
        activity = Activity.objects.create(user=user, activity_type="run", duration=30)
        self.assertEqual(activity.activity_type, "run")
        self.assertEqual(activity.duration, 30)

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard_entry(self):
        user = User.objects.create(username="testuser")
        entry = Leaderboard.objects.create(user=user, score=100)
        self.assertEqual(entry.score, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name="Pushups", description="Do 20 pushups")
        self.assertEqual(workout.name, "Pushups")
