from django.db import models

class Fardao(models.Model):

    id = models.CharField(max_length=10, primary_key=True)
    empresa = models.IntegerField()
    safra = models.IntegerField()
    peso = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.IntegerField()


    class Meta:
        verbose_name = 'fardão'
        verbose_name_plural = 'fardões'

    def __str__(self):
        return self.id

class Pluma(models.Model):

    id = models.IntegerField(primary_key=True)
    empresa = models.IntegerField()
    safra = models.IntegerField()
    fardao = models.ForeignKey('Fardao')
    peso = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return self.id