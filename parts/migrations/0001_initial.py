# Generated by Django 4.2.16 on 2024-10-12 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aircrafts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_type', models.CharField(choices=[('wing', 'Wing'), ('fuselage', 'Fuselage'), ('tail', 'Tail'), ('avionics', 'Avionics')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('aircraft_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aircrafts.aircraft')),
            ],
        ),
    ]