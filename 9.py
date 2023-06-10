Gaji = int(input("Masukkan gaji Anda dalam bulan!"))
LamaCicilan = int(input("Masukkan lama cicilan yang anda inginkan! (dalam tahun (ex: 10)) : "))
NominalDP = int(input("Masukkan Nominal DP yang Anda inginkan! "))

Konversi = LamaCicilan * 12
TotalUang = (Gaji * Konversi) - NominalDP
SisaBulan = Konversi - 60

# Menghitung suku bunga fix dan floating
if 1 <= Konversi <= 60:
    bunga_fix = 0.04
    bunga_floating = 0
elif 61 <= Konversi <= 120:
    bunga_fix = 0.06
    bunga_floating = 0.10
elif 121 <= Konversi <= 180:
    bunga_fix = 0.08
    bunga_floating = 0.10
elif 181 <= Konversi <= 240:
    bunga_fix = 0.12
    bunga_floating = 0.10
else:
    bunga_fix = 0.13
    bunga_floating = 0.10

# Maksimal Angsuran
MaksimalTotalAngsuran = TotalUang * 0.3 
MaksimalTotalAngsuranperBulan = MaksimalTotalAngsuran / Konversi

# Breakdown Total Angsuran Bunga
TotalBungaFix = TotalUang * bunga_fix
TotalBungaFloating = TotalUang * bunga_floating
TotalBunga = (bunga_fix * 60) + (bunga_floating * SisaBulan)

# Breakdown Angsuran Bunga per Bulan 
bungafix = TotalBungaFix / Konversi
bungafloating = TotalBungaFloating / Konversi 
TotalBungaperBulan = TotalBunga / Konversi

# Breakdown Angsuran Pokok
AngsuranPokokperBulan = MaksimalTotalAngsuranperBulan - TotalBungaperBulan
TotalAngsuranPokok = AngsuranPokokperBulan * Konversi

#Saran Harga
SaranHargaRumah = MaksimalTotalAngsuran

# OUTPUT
print("===================================================================")
print("===================================================================")
print("Total Angsuran per bulan yang harus dibayarkan sebesar Rp", MaksimalTotalAngsuranperBulan)
print("===================================================================")
print("Total Angsuran Pokok yang harus dibayarkan sebesar Rp", TotalAngsuranPokok )
print("===================================================================")
print("Total Angsuran Bunga Fix yang harus dibayarkan sebesar Rp", TotalBungaFix)
print("===================================================================")
print("Total Angsuran Bunga Floating yang harus dibayarkan sebesar Rp", TotalBungaFloating)
print("===================================================================")
print("Total Angsuran Bunga yang harus dibayarkan sebesar Rp", TotalBunga)
print("===================================================================")
print("Maka saran harga rumah yang dapat diambil untuk KPR sebesar Rp", SaranHargaRumah)
print("===================================================================")
print("===================================================================")

# Menampilkan tabel angsuran setiap bulan
print("-----------------------------------------------------------------------")
print("Bulan\t\tAngsuran Pokok\t\tAngsuran Bunga Fix\t\tAngsuran Bunga Floating\t\tTotal Bunga per Bulan\t\t\t\tTotal Angsuran per Bulan")
print("-----------------------------------------------------------------------")
for bulan in range(1, Konversi + 1):
    if bulan <= 60:
        print(f"{bulan}\t\t{AngsuranPokokperBulan:.2f}\t\t{bungafix:.2f}\t\t{bungafloating:.2f}\t\t{TotalBungaperBulan:.2f}\t\t\t\t{MaksimalTotalAngsuranperBulan:.2f}")
print("-----------------------------------------------------------------------")

# Menampilkan tabel angsuran setiap bulan dengan bunga floating
if Konversi > 60:
    print("-----------------------------------------------------------------------")
    print("Bulan\t\tAngsuran Pokok\t\tAngsuran Bunga Fix\t\tAngsuran Bunga Floating\t\tTotal Bunga per Bulan\t\t\t\tTotal Angsuran per Bulan")
    print("-----------------------------------------------------------------------")
    for bulan in range(61, Konversi + 1):
        print(f"{bulan}\t\t{AngsuranPokokperBulan:.2f}\t\t{bungafix:.2f}\t\t{bungafloating:.2f}\t\t{TotalBungaperBulan:.2f}\t\t\t\t{MaksimalTotalAngsuranperBulan:.2f}")
    print("-----------------------------------------------------------------------")