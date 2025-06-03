from djongo import models

class User(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    def __str__(self):
        return self.email

class TeamMember(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    class Meta:
        abstract = True

class Team(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    members = models.ArrayField(model_container=TeamMember, blank=True, null=True)
    def __str__(self):
        return self.name

class Activity(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    user_email = models.EmailField()
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user_email} - {self.activity_type}"

class Leaderboard(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    team_name = models.CharField(max_length=100)
    points = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.team_name} - {self.points}"

class Workout(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name
