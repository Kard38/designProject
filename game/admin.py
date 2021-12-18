from django.contrib import admin
from game.models import *

admin.site.register(Games,GamesDetails)

admin.site.__reduce__(Category)
# Register your models here.
