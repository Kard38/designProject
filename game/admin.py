from django.contrib import admin
from game.models import *


class GameAdmin(admin.ModelAdmin):
    list_display = ['GameID', 'GameName']

    class Meta:
        model = Games


class GameAdmin2(admin.ModelAdmin):
    list_display = ['games', 'Platform']

    class Meta:
        model = Platform


admin.site.register(Games)
admin.site.register(GamesDetails)
admin.site.register(Platform)
admin.site.register(Category)

# Register your models here.
