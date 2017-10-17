from django.db import models

# Create your models here.



class Band(models.Model):
    navn = models.CharField(max_length=200)
    kostnad = models.IntegerField()
    manager = models.ForeignKey('auth.User')
    utstyr = models.TextField()
    sjanger = models.CharField(max_length=100)
    info = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.navn

class Bestilling(models.Model):
    dato = models.DateTimeField(blank=True,null=True)
    band = models.ForeignKey('Band')
    scene = models.CharField(max_length=200)
    godkjenning = ((True,'Godkjent'),(False,'Ikke godkjent'),(None,'Ikke vurdert enda'))
    godkjent = models.NullBooleanField(choices=godkjenning, default=None)

    def __str__(self):
        return self.band.navn

class Konserter(models.Model):
    scene = models.ForeignKey('Scener')
    teknikere= models.TextField()
    konsert = models.CharField(max_length=200)
    dato = models.DateTimeField(blank=True, null=True)
    band = models.ManyToManyField(Band, blank=True)
    festival = models.CharField(max_length=200)
    publikumsantall = models.IntegerField(blank=True)

    def __str__(self):
        return self.konsert

class Scener(models.Model):
    navn = models.CharField(max_length=200)
    storrelse = models.IntegerField()
    kostnad = models.IntegerField()

    def __str__(self):
        return self.navn
    class Meta:
        verbose_name_plural="Scener"
