from django.db import models


class Profil(models.Model):
    rasm = models.FileField(blank=True, null=True)
    location = models.CharField(max_length=500, blank=True, null=True)
    sana = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.location

# Create your models here.
