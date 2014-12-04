from django.db import models

class Athlete(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=200)
    athletes = models.ManyToManyField(Athlete)

    def __str__(self):
        return self.name

class Season(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Organization(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    def __str__(self):
        return self.name

class Game(models.Model):
    home_team = models.ForeignKey(Team, related_name='+')
    away_team = models.ForeignKey(Team, related_name='+')
    home_score = models.PositiveIntegerField()
    away_score = models.PositiveIntegerField()
    date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.home_team) + " vs " + str(self.away_team)

class League(models.Model):
    name = models.CharField(max_length=200)
    season = models.ForeignKey(Season)
    teams = models.ManyToManyField(Team)
    organization = models.ForeignKey(Organization)

    def __str__(self):
        return self.name