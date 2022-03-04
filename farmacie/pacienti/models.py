from django.db import models


# Create your models here.

class Pacient(models.Model):
    gen_p = (
        ('M', 'M'),
        ('F', 'F'),
    )
    nrgestiune = models.AutoField(primary_key=True)
    nume = models.CharField(max_length=40)
    telefon = models.IntegerField()
    email = models.EmailField(max_length=40)
    varsta = models.IntegerField()
    gen = models.CharField(max_length=1, choices=gen_p, null=True)
    observatii = models.TextField(blank=True)
    data_adaugarii = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nume