# Generated by Django 3.2.23 on 2024-01-03 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='job',
            field=models.CharField(blank=True, choices=[('Sales Assistant', 'Sales Assistant'), ('Delivery Driver', 'Delivery Driver'), ('Mechanic', 'Mechanic'), ('Window Tinter', 'Window Tinter')], max_length=50, null=True),
        ),
    ]