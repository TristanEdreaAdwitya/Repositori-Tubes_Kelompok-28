GajiBulanan = float(input("Masukkan gaji bulanan Anda: "))
Tenor = int(input("Masukkan lama KPR yang ingin Anda ambil(dalam tahun): "))

Konversi = Tenor * 12
SisaBulan = Konversi - 60

def BungaFix (Konversi):
    if 1 <= Konversi <= 60:
        return 0.04
    elif 61 <= Konversi <= 120:
        return 0.06
    elif 121 <= Konversi <= 180:
        return 0.08
    elif 181 <= Konversi <= 240:
        return 0.10
    else:
        return 0.13

def BungaFloating (Konversi):
    return 0.10

def KPR (GajiBulanan, Konversi):
    MaksAngsuran = GajiBulanan * 0.3
    AngsuranPokok = MaksAngsuran * 0.7 

    Bunga_Fix = BungaFix (Konversi)
    AngsuranBungaFix = MaksAngsuran * Bunga_Fix

    Bunga_Floating = BungaFloating (Konversi)
    AngsuranBungaFloating = MaksAngsuran * Bunga_Floating

    TotalAngsuranPokok = AngsuranPokok * Konversi
    TotalAngsuranBungaFix = AngsuranBungaFix * 60 if Konversi > 60 else AngsuranBungaFix * Konversi
    TotalAngsuranBungaFloating = AngsuranBungaFloating * SisaBulan if Konversi > 60 else 0
    TotalAngsuranBunga = TotalAngsuranBungaFix + TotalAngsuranBungaFloating

    AngsuranperBulan5Tahun = AngsuranPokok + AngsuranBungaFix
    AngsuranperBulanSisaBulan = AngsuranPokok + AngsuranBungaFloating

    SaranHargaRumah = TotalAngsuranPokok

    return AngsuranPokok, AngsuranBungaFix, AngsuranBungaFloating, AngsuranperBulan5Tahun, AngsuranperBulanSisaBulan, SaranHargaRumah,\
            TotalAngsuranPokok, TotalAngsuranBungaFix, TotalAngsuranBungaFloating, TotalAngsuranBunga, Konversi, SisaBulan

AngsuranPokok, AngsuranBungaFix, AngsuranBungaFloating, AngsuranperBulan5Tahun, AngsuranperBulanSisaBulan, SaranHargaRumah, \
TotalAngsuranPokok, TotalAngsuranBungaFix, TotalAngsuranBungaFloating, TotalAngsuranBunga, Konversi, SisaBulan = \
    KPR (GajiBulanan, Konversi)

# OUTPUT
print("===================================================================")
print("===================================================================")
print("Saran harga rumah yang dapat diambil sebesar: ", SaranHargaRumah)
print("Total Angsuran Pokok yang dibayarkan sebesar saran harga rumah")
print("===================================================================")
print("Total Angsuran Bunga Fix yang dibayarkan: ", TotalAngsuranBungaFix)
print("===================================================================")
print("Total Angsuran Bunga Floating yang dibayarkan: ", TotalAngsuranBungaFloating)
print("===================================================================")
print("Total Angsuran Bunga yang dibayarkan: ", TotalAngsuranBunga)
print("===================================================================")
print("===================================================================")

# Menampilkan tabel angsuran setiap bulan
print("-----------------------------------------------------------------------")
print("Bulan\t\tAngsuran Pokok\t\tAngsuran Bunga Fix\t\tAngsuran Bunga Floating\t\t\t\tTotal Angsuran per Bulan")
print("-----------------------------------------------------------------------")
for bulan in range(1, Konversi + 1):
    if bulan <= 60:
        print(f"{bulan}\t\t{AngsuranPokok:.2f}\t\t{AngsuranBungaFix:.2f}\t\t\t\t\t0.00\t\t\t\t\t\t{AngsuranperBulan5Tahun:.2f}")
    else:
        print(f"{bulan}\t\t{AngsuranPokok:.2f}\t\t0.00\t\t\t\t\t{AngsuranBungaFloating:.2f}\t\t\t\t\t\t{AngsuranperBulanSisaBulan:.2f}")

import matplotlib.pyplot as plt

# Data untuk diagram garis
bulan = list(range(1, Konversi + 1))  # Progres bulan
y = []
for i in range(1, Konversi + 1):
    if i <= 60:
        y.append(AngsuranperBulan5Tahun)
    else:
        y.append(AngsuranperBulanSisaBulan)

# Membuat diagram garis
plt.plot(bulan, y, marker='o', linestyle='-', color='b')

# Menampilkan judul dan label sumbu
plt.title('Progres Bulan vs Total Angsuran per Bulan')
plt.xlabel('Bulan')
plt.ylabel('Total Angsuran per Bulan')

# Menampilkan diagram garis
plt.show()