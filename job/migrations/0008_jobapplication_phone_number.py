# Generated by Django 3.2.23 on 2024-02-14 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_remove_jobapplication_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='phone_number',
            field=models.IntegerField(default='1234567890'),
        ),
    ]