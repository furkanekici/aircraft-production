from django.db import models

class Aircraft(models.Model):
    AIRCRAFT_TYPES = [
        ('tb2', 'TB2'),
        ('tb3', 'TB3'),
        ('akinci', 'AKINCI'),
        ('kizilelma', 'KIZILELMA'),
    ]

    aircraft_type = models.CharField(max_length=20, choices=AIRCRAFT_TYPES)
    wing = models.OneToOneField('parts.Part', related_name='wing', on_delete=models.CASCADE, null=True)
    fuselage = models.OneToOneField('parts.Part', related_name='fuselage', on_delete=models.CASCADE, null=True)
    tail = models.OneToOneField('parts.Part', related_name='tail', on_delete=models.CASCADE, null=True)
    avionics = models.OneToOneField('parts.Part', related_name='avionics', on_delete=models.CASCADE, null=True)
    assembled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_ready(self):
        return all([self.wing, self.fuselage, self.tail, self.avionics])

    def __str__(self):
        return f"{self.aircraft_type} - Assembled: {self.assembled}"

