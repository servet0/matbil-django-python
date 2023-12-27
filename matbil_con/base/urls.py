from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('duyuru/<str:id>/', views.duyuru_detay, name = 'duyuru'),
    path('bolum-hakkinda/', views.bolum, name = 'bolum'),
    path('ogretim-amac/', views.amac, name = 'amac'),
    path('program-ciktisi/', views.cikti, name = 'cikti'),
    path('akademik-program/', views.program, name = 'program'),
    path('ders-icerigi/', views.dersler, name = 'dersler'),
    path('mezunlar/', views.mezunlar, name = 'mezunlar'),
    path('staj/', views.staj, name = 'staj'),
    path('kalite-komisyonu/', views.kalite, name = 'kalite'),
    path('arastirma-yayinlar/', views.yayin, name = 'yayin'),
    path('arastirma-projeler/', views.proje, name = 'proje'),
    path('iletisim/', views.iletisim, name = 'iletisim'),
    path('iletisim-formu/', views.contact, name = 'contact'),
    path('idare/', views.idare, name = 'idare'),
    path('analiz-ve-fonksiyonlar-teorisi/', views.analiz, name = 'analiz'),
    path('bilgisayar-bilimleri/', views.bilgisayar, name = 'bilgisayar'),
    path('cebir-ve-sayılar-teorisi/', views.cebir, name = 'cebir'),
    path('geometri/', views.geometri, name = 'geometri'),
    path('matematiğin-temelleri-ve-lojik/', views.lojik, name = 'lojik'),
    path('topoloji/', views.topoloji, name = 'topoloji'),
    path('uygulamali-matematik/', views.uygulamali, name = 'uygulamali'),
]