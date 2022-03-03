from django.db import models


# Create your models here.

class Retete(models.Model):
    id = models.AutoField(primary_key=True)
    pacient = models.ForeignKey('pacienti.Pacient', on_delete=models.CASCADE)
    medicament = models.ForeignKey('medicamente.Medicament', on_delete=models.CASCADE)
    data_expirare = models.DateField()

    def __str__(self):
        return self.id
