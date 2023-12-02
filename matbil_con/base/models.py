from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime


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

class Bolum(models.Model):
    tittle = models.CharField(max_length=500, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

class Amac(models.Model):
    tittle = models.CharField(max_length=500, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

class Cikti(models.Model):
    tittle = models.CharField(max_length=500, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

class Program(models.Model):
    tittle = models.CharField(max_length=500, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='universite', null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

class Dersler(models.Model):
    tittle = models.CharField(max_length=500, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

class Mezunlar(models.Model):
    tittle = models.CharField(max_length=500, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

class Staj(models.Model):
    tittle = models.CharField(max_length=500, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

class Kalite(models.Model):
    tittle = models.CharField(max_length=500, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

class Arastirma(models.Model):
    tittle = models.CharField(max_length=500, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    tittle2 = models.CharField(max_length=500, null=True, blank=True)
    description2 = RichTextField(null=True, blank=True)
    date2 = models.DateTimeField(auto_now=True)

class İletisim(models.Model):
    tittle = models.CharField(max_length=500, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=21)
    subject = models.CharField(max_length=300)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
    
class Idare(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    text = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='idare', null=True, blank=True)

class Analiz(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    text = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='idare', null=True, blank=True)

class Bilgisayar(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    text = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='idare', null=True, blank=True)

class Cebir(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    text = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='idare', null=True, blank=True)

class Geometri(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    text = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='idare', null=True, blank=True)

class Lojik(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    text = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='idare', null=True, blank=True)

class Topoloji(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    text = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='idare', null=True, blank=True)

class Uygulamali(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    text = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='idare', null=True, blank=True)

class Footer(models.Model):
    date = models.IntegerField(default=datetime.now().year)
    text = RichTextField(null=True, blank=True)
    text2 = RichTextField(null=True, blank=True)


# Create your models here.
