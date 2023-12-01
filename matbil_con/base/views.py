from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Navbar, Navbar2, Home, Duyuru, Bolum, Amac, Cikti, Program, Dersler, Mezunlar, Staj, Kalite, Arastirma, İletisim, Idare, Analiz, Bilgisayar, Cebir, Geometri, Lojik, Topoloji, Uygulamali
from .forms import ContactForm

def home(request):
    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    duyurus = Duyuru.objects.all().order_by('-date')

    paginator = Paginator(duyurus, 6) 

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'duyurus': duyurus, 'page_obj': page_obj}

    return render(request, 'base/home.html', context)

def duyuru_detay(request, id):
    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    duyuru_d = Duyuru.objects.get( tittle=id)

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'duyuru_d': duyuru_d}

    return render(request, 'base/duyuru_detay.html', context)

def bolum(request):
    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    bolums = Bolum.objects.first()

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'bolums': bolums}

    return render(request, 'base/bolum_hakkinda.html', context)

def amac(request):
    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    amacs = Amac.objects.first()

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'amacs': amacs}

    return render(request, 'base/ogretim_amac.html', context)

def cikti(request):
    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    ciktis = Cikti.objects.first()

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'ciktis': ciktis}

    return render(request, 'base/program_ciktisi.html', context)

def program(request):
    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    programs = Program.objects.first()

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'programs': programs}

    return render(request, 'base/akademik_program.html', context)

def dersler(request):
    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    dersler = Dersler.objects.first()

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'dersler': dersler}

    return render(request, 'base/ders_icerigi.html', context)

def mezunlar(request):
    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    mezunlar = Mezunlar.objects.first()

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'mezunlar': mezunlar}

    return render(request, 'base/mezunlar.html', context)

def staj(request):
    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    staj = Staj.objects.first()

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'staj': staj}

    return render(request, 'base/staj.html', context)

def kalite(request):
    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    kalite = Kalite.objects.first()

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'kalite': kalite}

    return render(request, 'base/kalite.html', context)

def yayin(request):
    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    yayin = Arastirma.objects.first()

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'yayin': yayin}

    return render(request, 'base/yayin.html', context)

def proje(request):
    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    proje = Arastirma.objects.first()

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'proje': proje}

    return render(request, 'base/proje.html', context)

def iletisim(request):
    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    iletisim = İletisim.objects.first()

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'iletisim': iletisim}

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
    

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'form':form}

    return render(request, 'base/iletisim_form.html', context)

def idare(request):
    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    idares = Idare.objects.all()

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'idares': idares}

    return render(request, 'base/idare.html', context)

def analiz(request):
    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    analizs = Analiz.objects.all()

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'analizs': analizs}

    return render(request, 'base/analiz.html', context)

def bilgisayar(request):
    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    bilgisayars = Bilgisayar.objects.all()

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'bilgisayars': bilgisayars}

    return render(request, 'base/bilgisayar.html', context)

def cebir(request):
    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    cebirs = Cebir.objects.all()

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'cebirs': cebirs}

    return render(request, 'base/cebir.html', context)

def geometri(request):
    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    geometris = Geometri.objects.all()

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'geometris': geometris}

    return render(request, 'base/geometri.html', context)

def lojik(request):
    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    lojiks = Lojik.objects.all()

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'lojiks': lojiks}

    return render(request, 'base/lojik.html', context)

def topoloji(request):
    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    topolojis = Topoloji.objects.all()

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'topolojis': topolojis}

    return render(request, 'base/topoloji.html', context)

def uygulamali(request):
    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    uygulamalis = Uygulamali.objects.all()

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'uygulamalis': uygulamalis}

    return render(request, 'base/uygulamali.html', context)
# Create your views here.
