from django.db import models
from ckeditor.fields import RichTextField

class Navbar(models.Model):
    logo = models.CharField(max_length=500, null=True, blank=True)
    home = models.CharField(max_length=500, null=True, blank=True)
    
    bolum = models.CharField(max_length=500, null=True, blank=True)
    bolum_alt_1 = models.CharField(max_length=500, null=True, blank=True)
    bolum_alt_2 = models.CharField(max_length=500, null=True, blank=True)
    bolum_alt_3 = models.CharField(max_length=500, null=True, blank=True)
    bolum_alt_4 = models.CharField(max_length=500, null=True, blank=True)
    
    akademik = models.CharField(max_length=500, null=True, blank=True)
    akademik_alt_1 = models.CharField(max_length=500, null=True, blank=True)
    akademik_alt_2 = models.CharField(max_length=500, null=True, blank=True)
    akademik_alt_3 = models.CharField(max_length=500, null=True, blank=True)
    akademik_alt_4 = models.CharField(max_length=500, null=True, blank=True)
    akademik_alt_5 = models.CharField(max_length=500, null=True, blank=True)
    akademik_alt_6 = models.CharField(max_length=500, null=True, blank=True)
    akademik_alt_7 = models.CharField(max_length=500, null=True, blank=True)

    program = models.CharField(max_length=500, null=True, blank=True)
    ders = models.CharField(max_length=500, null=True, blank=True)
    mezun = models.CharField(max_length=500, null=True, blank=True)
    staj = models.CharField(max_length=500, null=True, blank=True)
    kalite = models.CharField(max_length=500, null=True, blank=True)

    arastirma = models.CharField(max_length=500, null=True, blank=True)
    arastirma_alt_1 = models.CharField(max_length=500, null=True, blank=True)
    arastirma_alt_2 = models.CharField(max_length=500, null=True, blank=True)

    nokta = models.CharField(max_length=500, null=True, blank=True)

class Navbar2(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

class Home(models.Model):
    bolum_ismi = models.CharField(max_length=500, null=True, blank=True)
    duyuru = models.CharField(max_length=500, null=True, blank=True)

class Duyuru(models.Model):
    tittle = models.CharField(max_length=500, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)



# Create your models here.
