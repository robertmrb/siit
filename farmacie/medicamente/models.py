from django.db import models


# Create your models here.

class Medicament(models.Model):
    unitate_m = (
        ('comprimate', 'comprimate'),
        ('flacoane', 'flacoane'),
    )
    id = models.AutoField(primary_key=True)
    numemedicament = models.CharField(max_length=40)
    stoc = models.IntegerField()
    unitate = models.CharField(max_length=10, choices=unitate_m, null=True)
    data_expirarii = models.DateField()

    def __str__(self):
        return self.numemedicament
