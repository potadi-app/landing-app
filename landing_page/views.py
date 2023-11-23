from django.shortcuts import render


def home(request):
    return render(request, 'index.html')

def cara_kerja(request):
    return render(request, 'cara_kerja.html')

def testi(request):
    return render(request, 'testi.html')

def contact(request):
    return render(request, 'contact.html')

def tentang_kami(request):
    return render(request, 'about.html')

def early(request):
    return render(request, 'early.html')

def healthy(request):
    return render(request, 'healthy.html')

def late(request):
    return render(request, 'late.html')