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
MaksimalTotalAngsuranBulan = MaksimalTotalAngsuran / Konversi

# Breakdown Total Angsuran Bunga
TotalBungaFix = TotalUang * bunga_fix
TotalBungaFloating = TotalUang * bunga_floating
TotalBunga = (bunga_fix * 60) + (bunga_floating * SisaBulan)

# Breakdown Angsuran Bunga per Bulan 
bungafix = TotalBungaFix / Konversi
bungafloating = TotalBungaFloating / Konversi 
TotalBungaperBulan = bungafix + bungafloating
TotalSeluruhBunga = TotalBungaperBulan * Konversi

# Breakdown Angsuran Pokok
AngsuranPokokperBulan = MaksimalTotalAngsuranBulan - TotalBungaperBulan
TotalAngsuranPokok = AngsuranPokokperBulan * Konversi
AngsuranPokokperBulandgnBungafix = AngsuranPokokperBulan + bungafix
AngsuranPokokperBulandgnBungaFloating = AngsuranPokokperBulan + bungafloating

#Saran Harga
SaranHargaRumah = MaksimalTotalAngsuran

# OUTPUT
print("===================================================================")
print("===================================================================")
print("Total Angsuran per bulan yang harus dibayarkan sebesar Rp", MaksimalTotalAngsuran)
print("===================================================================")
print("Total Angsuran Pokok yang harus dibayarkan sebesar Rp", TotalAngsuranPokok )
print("===================================================================")
print("Total Angsuran Bunga Fix yang harus dibayarkan sebesar Rp", TotalBungaFix)
print("===================================================================")
print("Total Angsuran Bunga Floating yang harus dibayarkan sebesar Rp", TotalBungaFloating)
print("===================================================================")
print("Total Angsuran Bunga yang harus dibayarkan sebesar Rp", TotalSeluruhBunga)
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
        print(f"{bulan}\t\t{AngsuranPokokperBulan:.2f}\t\t{bungafix:.2f}\t\t0.00\t\t\t{bungafix:.2f}\t\t\t\t{AngsuranPokokperBulandgnBungafix:.2f}")
    else:
        print(f"{bulan}\t\t{AngsuranPokokperBulan:.2f}\t\t0.00\t\t\t{bungafloating:.2f}\t\t{bungafloating:.2f}\t\t\t\t{AngsuranPokokperBulandgnBungaFloating:.2f}")

import matplotlib.pyplot as plt

# Data untuk diagram garis
bulan = list(range(1, Konversi + 1))  # Progres bulan
y = []
for i in range(1, Konversi + 1):
    if i <= 60:
        y.append(AngsuranPokokperBulandgnBungafix)
    else:
        y.append(AngsuranPokokperBulandgnBungaFloating)

# Membuat diagram garis
plt.plot(bulan, y, marker='o', linestyle='-', color='b')

# Menampilkan judul dan label sumbu
plt.title('Progres Bulan vs Total Angsuran per Bulan')
plt.xlabel('Bulan')
plt.ylabel('Total Angsuran per Bulan')

# Menampilkan diagram garis
plt.show()