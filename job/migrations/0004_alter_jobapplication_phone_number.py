# Generated by Django 3.2.23 on 2024-02-14 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_alter_jobapplication_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='phone_number',
            field=models.PositiveBigIntegerField(max_length=20),
        ),
    ]
