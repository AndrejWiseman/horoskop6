from django.db import models

# Create your models here.
class Horoskop(models.Model):

    znak = models.CharField(max_length=50)
    dnevni = models.TextField()
    nedeljni = models.TextField()
    mesecni = models.TextField()
    godisnji = models.TextField()

    def __str__(self):
        return self.znak
