from django.contrib import admin
from .models import Navbar, Navbar2, Home, Duyuru, Bolum, Amac, Cikti, Program, Dersler, Mezunlar, Staj, Kalite, Arastirma, İletisim, ContactMessage, Idare, Analiz, Bilgisayar, Cebir, Geometri, Lojik, Topoloji, Uygulamali, Footer



class NavbarAdmin(admin.ModelAdmin):
    list_display = ['logo', 'home', 'bolum', 'akademik', 'program', 'arastirma', 'nokta']
    search_fields = ['logo', 'home', 'bolum', 'akademik', 'program', 'arastirma', 'nokta']
    fields = ['logo', 'home', 'bolum', 'akademik', 'program', 'arastirma', 'nokta']


class HomeAdmin(admin.ModelAdmin):
    list_display = ['bolum_ismi', 'duyuru']
    search_fields = ['bolum_ismi', 'duyuru']
    fields = ['bolum_ismi', 'duyuru']

# Diğer modeller için de benzer şekilde devam edebilirsiniz.

admin.site.register(Navbar, NavbarAdmin)
admin.site.register(Navbar2)
admin.site.register(Home, HomeAdmin)
admin.site.register(Duyuru)
admin.site.register(Bolum)
admin.site.register(Amac)
admin.site.register(Cikti)
admin.site.register(Program)
admin.site.register(Dersler)
admin.site.register(Mezunlar)
admin.site.register(Staj)
admin.site.register(Kalite)
admin.site.register(Arastirma)
admin.site.register(İletisim)
admin.site.register(ContactMessage)
admin.site.register(Idare)
admin.site.register(Analiz)
admin.site.register(Bilgisayar)
admin.site.register(Cebir)
admin.site.register(Geometri)
admin.site.register(Lojik)
admin.site.register(Topoloji)
admin.site.register(Uygulamali)
admin.site.register(Footer)
