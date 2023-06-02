print("----Selamat Datang di Program Simulasi KPR----")
print("Pada program ini, Kami akan memberikan perkiraan Angsuran Pokok, Angsuran Bunga Fix, Angsuran Bunga Floating, Angsuran per Bulan, Total KPR, dan Minimal gaji yang harus Anda miliki untuk mengambil KPR tersebut")

HargaRumah = int(input("Masukkan harga rumah (ex: 500000000) "))
PersenDP = float(input("Masukkan %DP (ex: 20 )"))
LamaCicilan = int(input("Masukkan lama cicilan dalam tahun (ex: 10)"))

NominalDP = PersenDP*100/100*HargaRumah 
Konversi = LamaCicilan*12
TotalPinjaman = HargaRumah-NominalDP
