# Generated by Django 2.2.1 on 2019-12-11 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_similargameconnection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='similargameconnection',
            name='similar_games_rank',
            field=models.IntegerField(default=0),
        ),
    ]