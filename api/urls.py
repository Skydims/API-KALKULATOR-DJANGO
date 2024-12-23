from django.urls import path
from .views import kalkulator, ambil_hasil

urlpatterns = [
    path('kalkulator/', kalkulator, name='kalkulator'),
    path('kalkulator/<int:id>/', ambil_hasil, name='ambil_hasil'),
]
