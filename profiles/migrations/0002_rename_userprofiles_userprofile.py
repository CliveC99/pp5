# Generated by Django 3.2.23 on 2023-11-23 00:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfiles',
            new_name='UserProfile',
        ),
    ]