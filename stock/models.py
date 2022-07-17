from django.db import models

# Create your models here.


class Stock(models.Model):
    title = models.CharField(max_length=155)
    date = models.DateField()
    description = models.TextField(max_length=1555)
    jumlah = models.IntegerField(null=True, blank=True)
    harga = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title
