# Generated by Django 4.2.16 on 2024-10-12 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='personnel',
            field=models.ManyToManyField(to='users.personnel'),
        ),
    ]
