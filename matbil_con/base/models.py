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

    class Meta:
        verbose_name = ("Navbar")
        verbose_name_plural = ("Navbardaki Başlıkların İsimleri")


class Navbar2(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Navbar2")
        verbose_name_plural = ("İletişim ve sonradan eklenecek başlıkların isimleri ")

    def __str__(self):
        return self.name

class Home(models.Model):
    bolum_ismi = models.CharField(max_length=500, null=True, blank=True)
    duyuru = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = ("Home")
        verbose_name_plural = ("Anasayfa Başlıkları")

class Duyuru(models.Model):
    tittle = models.CharField(max_length=500, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Duyuru")
        verbose_name_plural = ("Duyurular")

    def __str__(self):
        return self.tittle

class Bolum(models.Model):
    tittle = models.CharField(max_length=500, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Bölüm")
        verbose_name_plural = ("Bölüm Hakkında")

    def __str__(self):
        return self.tittle

class Amac(models.Model):
    tittle = models.CharField(max_length=500, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tittle

    class Meta:
        verbose_name = ("Amaç")
        verbose_name_plural = ("Bölüm amaçları")

class Cikti(models.Model):
    tittle = models.CharField(max_length=500, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.tittle

    class Meta:
        verbose_name = ("Çıktı")
        verbose_name_plural = ("Bölüm Çıktısı")

class Program(models.Model):
    tittle = models.CharField(max_length=500, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='universite', null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tittle

    class Meta:
        verbose_name = ("Program")
        verbose_name_plural = ("Akademik Program")

class Dersler(models.Model):
    tittle = models.CharField(max_length=500, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tittle

    class Meta:
        verbose_name = ("Ders")
        verbose_name_plural = ("Ders İçerikleri")

class Mezunlar(models.Model):
    tittle = models.CharField(max_length=500, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tittle

    class Meta:
        verbose_name = ("Mezun")
        verbose_name_plural = ("Mezun Sistemi")

class Staj(models.Model):
    tittle = models.CharField(max_length=500, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tittle

    class Meta:
        verbose_name = ("Staj")
        verbose_name_plural = ("Staj")

class Kalite(models.Model):
    tittle = models.CharField(max_length=500, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tittle

    class Meta:
        verbose_name = ("Kalite")
        verbose_name_plural = ("Kalite Komisyonu")

class Arastirma(models.Model):
    tittle = models.CharField(max_length=500, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    tittle2 = models.CharField(max_length=500, null=True, blank=True)
    description2 = RichTextField(null=True, blank=True)
    date2 = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tittle

    class Meta:
        verbose_name = ("Araştırma")
        verbose_name_plural = ("Araştırma")

class İletisim(models.Model):
    tittle = models.CharField(max_length=500, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tittle

    class Meta:
        verbose_name = ("İletişim sayfası")
        verbose_name_plural = ("İletişim sayfası")

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=21)
    subject = models.CharField(max_length=300)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("İletişim form sayfası")
        verbose_name_plural = ("İletişim form sayfası")
    
class Idare(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    text = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='idare', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("İdare")
        verbose_name_plural = ("İdare")

class Analiz(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    text = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='idare', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("Analiz ve Fonksiyonlar Teorisi A.B.D")
        verbose_name_plural = ("Analiz ve Fonksiyonlar Teorisi A.B.D")

class Bilgisayar(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    text = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='idare', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("Bilgisayar Bilimleri A.B.D.")
        verbose_name_plural = ("Bilgisayar Bilimleri A.B.D.")

class Cebir(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    text = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='idare', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("Cebir ve Sayılar Teorisi A.B.D.")
        verbose_name_plural = ("Cebir ve Sayılar Teorisi A.B.D.")

class Geometri(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    text = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='idare', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("Geometri A.B.D.")
        verbose_name_plural = ("Geometri A.B.D.")

class Lojik(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    text = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='idare', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("Matematiğin Temelleri ve Lojik A.B.D.")
        verbose_name_plural = ("Matematiğin Temelleri ve Lojik A.B.D.")

class Topoloji(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    text = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='idare', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("Topoloji  A.B.D.")
        verbose_name_plural = ("Topoloji  A.B.D.")

class Uygulamali(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    text = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='idare', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("Uygulamalı Matematik  A.B.D.")
        verbose_name_plural = ("Uygulamalı Matematik  A.B.D.")

class Footer(models.Model):
    date = models.IntegerField(default=datetime.now().year)
    text = RichTextField(null=True, blank=True)
    text2 = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = ("Footer")
        verbose_name_plural = ("Footer")


# Create your models here.
