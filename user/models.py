from django.db import models

# Create your models here.
import game.models


class Users(models.Model):
    UserId = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=32)
    UserPassword = models.CharField(max_length=32)
    UserBirthday = models.DateField(max_length=32)
    UserEmail = models.EmailField()

    def __str__(self):
        return self.UserName


class UsersFavorites(models.Model):
    favoritesId = models.AutoField(primary_key=True)
    users = models.OneToOneField(Users, on_delete=models.CASCADE, default=None)
    games = models.OneToOneField(game.models.Games, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.users.UserName
