# Generated by Django 4.0 on 2021-12-18 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_platform_games'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='games',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='game.games'),
        ),
    ]
