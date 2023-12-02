from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Navbar, Navbar2, Home, Duyuru, Bolum, Amac, Cikti, Program, Dersler, Mezunlar, Staj, Kalite, Arastirma, İletisim, Idare, Analiz, Bilgisayar, Cebir, Geometri, Lojik, Topoloji, Uygulamali, Footer
from .forms import ContactForm

def home(request):
    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    duyurus = Duyuru.objects.all().order_by('-date')
    footers = Footer.objects.first()

    paginator = Paginator(duyurus, 6) 

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'duyurus': duyurus, 'page_obj': page_obj, 'footers': footers}

    return render(request, 'base/home.html', context)

def duyuru_detay(request, id):
    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    duyuru_d = Duyuru.objects.get( tittle=id)
    footers = Footer.objects.first()

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'duyuru_d': duyuru_d, 'footers': footers}

    return render(request, 'base/duyuru_detay.html', context)

def bolum(request):
    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    bolums = Bolum.objects.first()
    footers = Footer.objects.first()

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'bolums': bolums, 'footers': footers}

    return render(request, 'base/bolum_hakkinda.html', context)

def amac(request):
    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    amacs = Amac.objects.first()
    footers = Footer.objects.first()

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'amacs': amacs, 'footers': footers}

    return render(request, 'base/ogretim_amac.html', context)

def cikti(request):
    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    ciktis = Cikti.objects.first()
    footers = Footer.objects.first()

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'ciktis': ciktis, 'footers': footers}

    return render(request, 'base/program_ciktisi.html', context)

def program(request):
    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    programs = Program.objects.first()
    footers = Footer.objects.first()

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'programs': programs, 'footers': footers}

    return render(request, 'base/akademik_program.html', context)

def dersler(request):
    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    dersler = Dersler.objects.first()
    footers = Footer.objects.first()

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'dersler': dersler, 'footers': footers}

    return render(request, 'base/ders_icerigi.html', context)

def mezunlar(request):
    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    mezunlar = Mezunlar.objects.first()
    footers = Footer.objects.first()

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'mezunlar': mezunlar, 'footers': footers}

    return render(request, 'base/mezunlar.html', context)

def staj(request):
    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    staj = Staj.objects.first()
    footers = Footer.objects.first()

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'staj': staj, 'footers': footers}

    return render(request, 'base/staj.html', context)

def kalite(request):
    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    kalite = Kalite.objects.first()
    footers = Footer.objects.first()

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'kalite': kalite, 'footers': footers}

    return render(request, 'base/kalite.html', context)

def yayin(request):
    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    yayin = Arastirma.objects.first()
    footers = Footer.objects.first()

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'yayin': yayin, 'footers': footers}

    return render(request, 'base/yayin.html', context)

def proje(request):
    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    proje = Arastirma.objects.first()
    footers = Footer.objects.first()

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'proje': proje, 'footers': footers}

    return render(request, 'base/proje.html', context)

def iletisim(request):
    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    iletisim = İletisim.objects.first()
    footers = Footer.objects.first()

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'iletisim': iletisim, 'footers': footers}

    return render(request, 'base/iletisim.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')  # İletişim başarıyla gönderildiyse yönlendir
    else:
        form = ContactForm()

    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    footers = Footer.objects.first()
    

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'form':form, 'footers': footers}

    return render(request, 'base/iletisim_form.html', context)

def idare(request):
    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    idares = Idare.objects.all()
    footers = Footer.objects.first()

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'idares': idares, 'footers': footers}

    return render(request, 'base/idare.html', context)

def analiz(request):
    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    analizs = Analiz.objects.all()
    footers = Footer.objects.first()

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'analizs': analizs, 'footers': footers}

    return render(request, 'base/analiz.html', context)

def bilgisayar(request):
    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    bilgisayars = Bilgisayar.objects.all()
    footers = Footer.objects.first()

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'bilgisayars': bilgisayars, 'footers': footers}

    return render(request, 'base/bilgisayar.html', context)

def cebir(request):
    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    cebirs = Cebir.objects.all()
    footers = Footer.objects.first()

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'cebirs': cebirs, 'footers': footers}

    return render(request, 'base/cebir.html', context)

def geometri(request):
    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    geometris = Geometri.objects.all()
    footers = Footer.objects.first()

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'geometris': geometris, 'footers': footers}

    return render(request, 'base/geometri.html', context)

def lojik(request):
    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    lojiks = Lojik.objects.all()
    footers = Footer.objects.first()

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'lojiks': lojiks, 'footers': footers}

    return render(request, 'base/lojik.html', context)

def topoloji(request):
    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    topolojis = Topoloji.objects.all()
    footers = Footer.objects.first()

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'topolojis': topolojis, 'footers': footers}

    return render(request, 'base/topoloji.html', context)

def uygulamali(request):
    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    uygulamalis = Uygulamali.objects.all()
    footers = Footer.objects.first()

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'uygulamalis': uygulamalis, 'footers': footers}

    return render(request, 'base/uygulamali.html', context)

# Create your views here.
