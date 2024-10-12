from django.contrib.auth.models import AbstractUser
from django.db import models

class Personnel(AbstractUser):
    teams = models.ManyToManyField('teams.Team', related_name='personnel_members')

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='personnel_groups',  # Custom related_name for groups
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='personnel_permissions',  # Custom related_name for permissions
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    class Meta:
        verbose_name = "Personnel"
        verbose_name_plural = "Personnel"

    def __str__(self):
        return self.username

