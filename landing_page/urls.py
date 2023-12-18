from django.urls import path, include
from landing_page import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cara-kerja/', views.cara_kerja, name='cara_kerja'),
    path('testimonial/', views.testi, name='testi'),
    path('kontak/', views.contact, name='contact'),
    path('tentang-kami/', views.tentang_kami, name='about'),
    path('diseases/early/', views.early, name='early'),
    path('diseases/healthy/', views.healthy, name='healthy'),
    path('diseases/late/', views.late, name='late'),

]