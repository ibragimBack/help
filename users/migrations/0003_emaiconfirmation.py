# Generated by Django 5.0.4 on 2024-05-02 17:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_remove_user_groups_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmaiConfirmation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=6)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.customuser')),
            ],
        ),
    ]
