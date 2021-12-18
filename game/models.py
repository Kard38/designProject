from django.db import models
from django.urls import reverse


# Create your models here.
class Games(models.Model):
    object = None
    # GameId int primary key
    GameId = models.AutoField(primary_key=True)
    GameName = models.CharField(max_length=100)

    def __str__(self):
        return self.GameName

    def get_absolute_url(self):
        return reverse('game:detail', kwargs={'id': self.GameId})


class GamesDetails(models.Model):
    # GameId int  primary keyg
    GameId = Games.GameId
    games = models.OneToOneField(Games, on_delete=models.CASCADE, default=None)
    ReleaseDate = models.DateField()
    RequiredAge = models.IntegerField()
    DemoCount = models.IntegerField()
    DLCCount = models.IntegerField()
    Metacritic = models.IntegerField()
    RecommendationCount = models.IntegerField()
    AboutText = models.CharField(max_length=400)
    DetailedDescrip = models.CharField(max_length=800)
    SupportedLanguages = models.CharField(max_length=250)

    def __str__(self):
        return self.games.GameName


class Category(models.Model):
    # GameId
    GameId = Games.GameId
    games = models.OneToOneField(Games, on_delete=models.CASCADE, default=None)
    CategorySinglePlayer = models.BooleanField()
    CategoryMultiplayer = models.BooleanField()
    CategoryCoop = models.BooleanField()
    CategoryMMO = models.BooleanField()
    CategoryInAppPurchase = models.BooleanField()
    CategoryIncludeLevelEditor = models.BooleanField()
    CategoryVRSupport = models.BooleanField()
    GenreIsIndie = models.BooleanField()
    GenreIsAction = models.BooleanField()
    GenreIsAdventure = models.BooleanField()
    GenreIsCasual = models.BooleanField()
    GenreIsStrategy = models.BooleanField()
    GenreIsRPG = models.BooleanField()
    GenreIsSimulation = models.BooleanField()
    GenreIsEarlyAcces = models.BooleanField()
    GenreIsFreeToPlay = models.BooleanField()
    GenreIsSports = models.BooleanField()
    GenreIsRacing = models.BooleanField()
    GenreIsMassivelyMultiplayer = models.BooleanField()

    def __str__(self):
        return self.games.GameName



class Platform(models.Model):
    # GameId
    GameId = Games.GameId
    games = models.OneToOneField(Games, on_delete=models.CASCADE, default=None)
    Windows = models.BooleanField()
    Linux = models.BooleanField()
    Mac = models.BooleanField()
    PS4 = models.BooleanField()
    PS5 = models.BooleanField()
    XBOXONE = models.BooleanField()

    def __str__(self):
        return self.games.GameName
