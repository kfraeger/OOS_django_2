from django.db import models

# Create your models here.

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


# media/img/flags/name
def upload_to_dir(instance, filename):
    return 'img/flags/{0}/{1}'.format(instance.name, filename)


# media/img/player/name
def upload_to_dir_player(instance, filename):
    return 'img/player/{0}/{1}'.format(instance.team, filename)


class Stadium(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["city"]


class Round (models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=1)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Team(models.Model):

    name = models.CharField(max_length=50, unique=True, blank=False, verbose_name="Team")
    short = models.CharField(max_length=3, default='')
    trainer = models.CharField(max_length=100)
    group = models.ForeignKey(Group, verbose_name="Gruppe", related_name='group')
    flag = models.ImageField(upload_to=upload_to_dir, default='', verbose_name="Nationalflagge")
    games_played = models.PositiveIntegerField(default=0)
    win = models.PositiveIntegerField(default=0)
    draw = models.PositiveIntegerField(default=0)
    lost = models.PositiveIntegerField(default=0)
    goal = models.PositiveIntegerField(default=0)
    goal_conceded = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('em16:team-detail', kwargs={'pk': self.pk})

    def _calc_tordifferenz(self):
        """returns the calculated Tordifferenz"""
        return self.goal - self.goal_conceded

    def _calc_points(self):
        return self.win * 3 + self.draw

    tordifferenz = property(_calc_tordifferenz)
    points = property(_calc_points)

    class Meta:
        ordering = ["name"]


class Player (models.Model):

    POSITION_CHOICES = (
        ('Torwart', 'Torwart'),
        ('Stürmer', 'Stürmer'),
        ('Mittelfeld', 'Mittelfeld'),
        ('Verteidigung', 'Verteidigung')
    )

    name = models.CharField(max_length=100, verbose_name='Vorname')
    surname = models.CharField(max_length=100, verbose_name='Nachname')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='Nationalmannschaft', related_name='team')
    position = models.CharField(max_length=20, choices=POSITION_CHOICES, default='--', verbose_name='Position')
    number = models.IntegerField(default=0, verbose_name='Nummer')
    img = models.ImageField(upload_to=upload_to_dir_player, verbose_name='Spielerbild')

    def get_absolute_url(self):
        return reverse('em16:player-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return u"{0} {1}".format(self.surname, self.name)

    class Meta:
        ordering = ["surname"]


class Game(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    round = models.ForeignKey(Round, related_name='rounds')
    group = models.ForeignKey(Group, null=True, blank=True)
    teamHomeAlias = models.CharField(max_length=50, null=True, verbose_name='Heimteam Liste')
    teamGuestAlias = models.CharField(max_length=50, null=True, verbose_name='Gastteam Liste')
    host = models.ForeignKey(Stadium, verbose_name="Gastgeber", related_name='stadiums', default='')
    teamHome = models.ForeignKey(Team, related_name='home', null=True, blank=True)
    teamGuest = models.ForeignKey(Team, related_name='guest', null=True, blank=True)
    teamHomeGoals = models.PositiveIntegerField(null=True, blank=True)
    teamGuestGoals = models.PositiveIntegerField(null=True, blank=True)
    others = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):  # __unicode__ on Python 2
        return 'u{0}'.format(self.date)

    class Meta:
        ordering = ["date", "time"]

