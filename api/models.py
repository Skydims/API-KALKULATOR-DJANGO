from django.db import models

class HasilKalkulator(models.Model):
    angka1 = models.FloatField()
    angka2 = models.FloatField()
    operator = models.CharField(max_length=10)
    hasil = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Hasil: {self.angka1} {self.operator} {self.angka2} = {self.hasil}"
