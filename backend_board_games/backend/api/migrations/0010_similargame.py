# Generated by Django 2.2.1 on 2019-12-11 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_gameshort_rank'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimilarGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.PositiveIntegerField(default=0)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='similar_games', to='api.Game')),
            ],
            options={
                'verbose_name': 'Similar Game',
                'verbose_name_plural': 'Similar Games',
            },
        ),
    ]