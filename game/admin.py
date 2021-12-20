from django.contrib import admin
from game.models import *


class GameDetailInline(admin.StackedInline):
    model = GamesDetails


class GameCategoryInline(admin.StackedInline):
    model = Category


class GamePlatformInline(admin.StackedInline):
    model = Platform


class GameAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['GameName']})
    ]
    inlines = [GameDetailInline, GamePlatformInline, GameCategoryInline]


admin.site.register(Games, GameAdmin)
# Register your models here.
