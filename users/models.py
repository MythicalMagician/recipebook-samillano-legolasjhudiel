# users/models.py
"""Profile class for user accounts."""

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Profile class extending default User model.
    Name with maximum of 50 characters.
    Short bio allowing more than 255 characters.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.TextField(blank=True, max_length=510)

    def __str__(self):
        return self.name
