from django.shortcuts import render
from django.http import JsonResponse
from landing_page.helpers.utils import email_send

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

def send_email(request):
    if request.method == 'POST':
        sender = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        print(sender, subject, message)
        try:
            email_send(sender, subject, message)
            return JsonResponse({'status': 200, 'message': 'Email terkirim dengan sukses'})
        except Exception as e:
            return JsonResponse({'status': 'failed', 'message': str(e)})