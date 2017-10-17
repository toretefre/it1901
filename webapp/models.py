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
    scene = models.CharField(max_length=200)
    teknikere= models.TextField()
    konsert = models.CharField(max_length=200)
    dato = models.DateTimeField(blank=True, null=True)
    band = models.ForeignKey('Band', models.SET_NULL, blank=True, null=True,)
    festival = models.CharField(max_length=200)

    def __str__(self):
        return self.konsert

class Backline(models.Model):
    band = models.ForeignKey('band', models.SET_NULL, blank=True, null=True,)
    backline = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.backline

class Tekniske_behov(models.Model):
    band = models.ForeignKey('band', models.SET_NULL, blank=True, null=True,)
    backline = models.ForeignKey('backline', models.SET_NULL, blank=True, null=True,)
    behov = models.CharField(max_length=50, db_index=True)
    opplastet = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.behov)
