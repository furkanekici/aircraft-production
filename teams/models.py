from django.db import models

class Team(models.Model):
    TEAM_TYPES = [
        ('wing', 'Wing Team'),
        ('fuselage', 'Fuselage Team'),
        ('tail', 'Tail Team'),
        ('avionics', 'Avionics Team'),
        ('assembly', 'Assembly Team'),
    ]

    team_type = models.CharField(max_length=10, choices=TEAM_TYPES)
    personnel = models.ManyToManyField('users.Personnel')

    def __str__(self):
        return self.team_type

