from django.db import models


# Create your models here.
class users(models.Model):
    UserId = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=32)
    UserPassword = models.CharField(max_length=32)
    UserBirthday = models.DateField(max_length=32)
    UserEmail = models.EmailField()

    def __str__(self):
        return self.UserName
