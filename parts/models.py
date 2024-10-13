from django.db import models

class Part(models.Model):
    PART_TYPES = [
        ('wing', 'Wing'),
        ('fuselage', 'Fuselage'),
        ('tail', 'Tail'),
        ('avionics', 'Avionics'),
    ]

    part_type = models.CharField(max_length=10, choices=PART_TYPES)
    aircraft_type = models.ForeignKey('aircrafts.Aircraft', on_delete=models.CASCADE)
    team = models.ForeignKey('teams.Team', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.part_type} for {self.aircraft_type}"

