print("----Selamat Datang di Program Simulasi KPR----")
print("Pada program ini, Kami akan memberikan perkiraan Angsuran Pokok, Angsuran Bunga Fix, Angsuran Bunga Floating, Angsuran per Bulan, Total KPR, dan Minimal gaji yang harus Anda miliki untuk mengambil KPR tersebut")

HargaRumah = int(input("Masukkan harga rumah (ex: 500000000) "))
PersenDP = float(input("Masukkan %DP (ex: 20 )"))
LamaCicilan = int(input("Masukkan lama cicilan dalam tahun (ex: 10)"))

NominalDP = PersenDP * HargaRumah / 100
Konversi = LamaCicilan * 12
TotalPinjaman = HargaRumah - NominalDP

# Menghitung suku bunga tetap dan angsuran bunga tetap berdasarkan lama cicilan
if 1 <= Konversi <= 60:
    bunga_fix = 0.04
elif 61 <= Konversi <= 120:
    bunga_fix = 0.06
elif 121 <= Konversi <= 180:
    bunga_fix = 0.08
elif 181 <= Konversi <= 240:
    bunga_fix = 0.12
else:
    bunga_fix = 0.13

# Menghitung angsuran bunga tetap
angsuran_bunga_fix = TotalPinjaman * bunga_fix

