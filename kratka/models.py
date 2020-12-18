from django.db import models

# Create your models here.
class Produkt(models.Model):
    def __str__(self):
        return self.nazwa
    
    nazwa = models.CharField(max_length=100)
    opis = models.TextField()

    class Meta:
        verbose_name = "Produkt"
        verbose_name_plural = "Produkty"

