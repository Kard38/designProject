from django.db import models
from django.urls import reverse
# from django.contrib.auth.models import User


# Create your models here.
from account.models import CustomUser


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
    CategorySinglePlayer = models.BooleanField(verbose_name='Tek Oyuncu')
    CategoryMultiplayer = models.BooleanField(verbose_name='Çoklu Oyuncu')
    CategoryCoop = models.BooleanField(verbose_name='CO-OP')
    CategoryMMO = models.BooleanField(verbose_name='MMO')
    CategoryInAppPurchase = models.BooleanField(verbose_name='Uygulama içi satın alma')
    CategoryVRSupport = models.BooleanField(verbose_name='VR Destekli')
    GenreIsIndie = models.BooleanField(verbose_name='İndie')
    GenreIsAction = models.BooleanField(verbose_name='Aksiyon')
    GenreIsAdventure = models.BooleanField(verbose_name='Macera')
    GenreIsCasual = models.BooleanField(verbose_name='Gündelik')
    GenreIsStrategy = models.BooleanField(verbose_name='Strateji')
    GenreIsRPG = models.BooleanField(verbose_name='RPG')
    GenreIsSimulation = models.BooleanField(verbose_name='Simülasyon')
    GenreIsEarlyAcces = models.BooleanField(verbose_name='Erken Erişim')
    GenreIsFreeToPlay = models.BooleanField(verbose_name='Oynaması Ücretsiz')
    GenreIsSports = models.BooleanField(verbose_name='Spor')
    GenreIsRacing = models.BooleanField(verbose_name='Yarış')
    GenreIsMassivelyMultiplayer = models.BooleanField(verbose_name='Devasa Çok Oyunculu')

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


class UsersFavorites(models.Model):
    favoritesId = models.AutoField(primary_key=True)
    users = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)
    games = models.ForeignKey(Games, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.users.username
