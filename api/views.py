from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import HasilKalkulator

@csrf_exempt  # Jika Anda tidak menggunakan CSRF (bisa dihilangkan jika tidak perlu)
def kalkulator(request):
    if request.method == "GET":
        angka1 = request.GET.get('angka1')
        angka2 = request.GET.get('angka2')
        operator = request.GET.get('operator')

        # Validasi input angka dan operator
        try:
            angka1 = float(angka1)
            angka2 = float(angka2)
        except (ValueError, TypeError):
            return JsonResponse({"error": "Masukkan angka yang valid"}, status=400)

        if operator == "tambah":
            hasil = angka1 + angka2
        elif operator == "kurang":
            hasil = angka1 - angka2
        elif operator == "kali":
            hasil = angka1 * angka2
        elif operator == "bagi":
            if angka2 == 0:
                return JsonResponse({"error": "Tidak dapat membagi dengan nol"}, status=400)
            else:
                hasil = angka1 / angka2
        else:
            return JsonResponse({"error": "Operator tidak valid"}, status=400)

        # Menyimpan hasil perhitungan ke database
        hasil_kalkulasi = HasilKalkulator.objects.create(
            angka1=angka1, angka2=angka2, operator=operator, hasil=hasil
        )

        return JsonResponse({
            "hasil": hasil,
            "id": hasil_kalkulasi.id,  # ID hasil yang baru disimpan
            "created_at": hasil_kalkulasi.created_at  # Tanggal/waktu pembuatan hasil
        })

    return JsonResponse({"error": "Metode HTTP tidak valid, gunakan GET"}, status=405)  # Pastikan ini hanya ada di fungsi yang menangani POST atau non-GET request


# Fungsi untuk mengambil hasil perhitungan berdasarkan ID
def ambil_hasil(request, id):
    if request.method == "GET":  # Pastikan hanya menerima request GET untuk ambil hasil
        try:
            # Mencari hasil berdasarkan ID
            hasil = HasilKalkulator.objects.get(id=id)
            
            # Mengembalikan hasil dalam format JSON
            return JsonResponse({
                "angka1": hasil.angka1,
                "angka2": hasil.angka2,
                "operator": hasil.operator,
                "hasil": hasil.hasil,
                "created_at": hasil.created_at
            })
        except HasilKalkulator.DoesNotExist:
            # Jika hasil tidak ditemukan, mengembalikan pesan error
            return JsonResponse({"error": "Hasil tidak ditemukan"}, status=404)

    # Hanya menerima GET untuk endpoint ini
    return JsonResponse({"error": "Metode HTTP tidak valid, gunakan GET"}, status=405)
