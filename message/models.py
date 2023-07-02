from django.db import models
from django.urls import reverse


class Contact(models.Model):
    """A simple model for storing Contact information"""

    name = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=11)
    id_number = models.CharField(max_length=11)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Additional information for the Class"""

        ordering = ["date_added"]

    def __str__(self):
        return f"{self.name} :: {self.id_number.upper()}"

    def get_absolute_url(self):
        return reverse("home")
