# Generated by Django 3.2.23 on 2024-02-14 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_alter_jobapplication_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='phone_number',
            field=models.PositiveBigIntegerField(),
        ),
    ]
