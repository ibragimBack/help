# Generated by Django 5.0.4 on 2024-05-01 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0003_director_movies_count_alter_review_movie_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='director',
            name='movies_count',
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]
