from django.db import models

# Create your models here.
from django.db import models

class Projet(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/')
    lien = models.URLField(blank=True)

    def __str__(self):
        return self.titre
