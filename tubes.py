print("----Selamat Datang di Program Simulasi KPR----")
print("Pada program ini, Kami akan memberikan perkiraan Angsuran Pokok, Angsuran Bunga Fix, Angsuran Bunga Floating, Angsuran per Bulan, Total KPR, dan Minimal gaji yang harus Anda miliki untuk mengambil KPR tersebut")

HargaRumah = int(input("Masukkan harga rumah (ex: 500000000) : "))
PersenDP = int(input("Masukkan %DP (ex: 20 ) : "))
LamaCicilan = int(input("Masukkan lama cicilan dalam tahun (ex: 10) : "))

NominalDP = PersenDP * HargaRumah / 100
Konversi = LamaCicilan * 12
TotalPinjaman = HargaRumah - NominalDP

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

# Menghitung angsuran pokok
angsuran_pokok = TotalPinjaman / Konversi

# Menghitung angsuran bunga fix per bulan
angsuran_bunga_fix_perbulan =  (TotalPinjaman *bunga_fix * LamaCicilan)/Konversi

# Menghitung angsuran per bulan menggunakan bunga fix
angsuran_per_bulan_menggunakan_bunga_fix = angsuran_pokok + angsuran_bunga_fix_perbulan

# Menghitung total bunga fix dan total angsuran saat menggunakan bunga fix dalam waktu 5 tahun ke bawah
total_bunga_fix = angsuran_bunga_fix_perbulan * 60
total_angsuran_bunga_fix = angsuran_per_bulan_menggunakan_bunga_fix * 60

# Menghitung angsuran bunga floating per bulan
angsuran_bunga_floating_perbulan = (TotalPinjaman * bunga_floating) / 12

# Menghitung angsuran pokok per bulan dengan bunga floating
angsuran_pokok_perbulan_dgn_bunga_floating = angsuran_pokok + angsuran_bunga_floating_perbulan

# Menghitung total bunga floating
total_bunga_floating = angsuran_bunga_floating_perbulan * (Konversi - 60)

# Menghitung angsuran per bulan menggunakan bunga floating
if Konversi > 60:
    total_angsuran_per_bulan_menggunakan_bunga_floating = (TotalPinjaman - total_angsuran_bunga_fix) / (Konversi - 60) + angsuran_bunga_floating_perbulan
else:
    total_angsuran_per_bulan_menggunakan_bunga_floating = angsuran_bunga_floating_perbulan 

# Menghitung total keseluruhan angsuran menggunakan bunga fix dan bunga floating
total_KPR = (angsuran_per_bulan_menggunakan_bunga_fix + total_angsuran_per_bulan_menggunakan_bunga_floating) * Konversi
minimal_gaji = total_KPR / (Konversi * 0.3)

# OUTPUT
print("===================================================================")
print("Angsuran Pokok per bulan yang harus dibayarkan sebesar Rp", angsuran_pokok)
print("===================================================================")
print("Angsuran Bunga Fix per bulan yang harus dibayarkan sebesar Rp", angsuran_bunga_fix_perbulan)
print("===================================================================")
print("Total keseluruhan Angsuran menggunakan Bunga Fix yang harus dibayarkan sebesar Rp", total_angsuran_bunga_fix)
print("===================================================================")
print("Total Angsuran Bunga Floating keseluruhan yang harus dibayarkan sebesar Rp", total_bunga_floating)
print("===================================================================")
print("Total Keseluruhan Angsuran menggunakan Bunga Floating yang harus dibayarkan sebesar Rp", total_angsuran_per_bulan_menggunakan_bunga_floating)
print("===================================================================")
print("Maka total KPR yang harus dibayarkan adalah Rp", total_KPR)
print("===================================================================")
print("Minimal gaji yang menyanggupi untuk mengambil KPR ini adalah Rp", minimal_gaji, "Per bulan")

# Menampilkan tabel angsuran setiap bulan
print("-----------------------------------------------------------------------")
print("Bulan\t\tAngsuran Pokok\t\tAngsuran Bunga Fix\t\tAngsuran Bunga Floating\t\tTotal Bunga per Bulan\t\t\t\tTotal Angsuran per Bulan")
print("-----------------------------------------------------------------------")
for bulan in range(1, Konversi + 1):
    if bulan <= 60:
        print(f"{bulan}\t\t{angsuran_pokok:.2f}\t\t\t{angsuran_bunga_fix_perbulan:.2f}\t\t0.00\t\t\t{angsuran_bunga_fix_perbulan:.2f} \t\t\t{angsuran_per_bulan_menggunakan_bunga_fix:.2f}")
    else:
        print(f"{bulan}\t\t{angsuran_pokok:.2f}\t\t0.00\t\t\t{angsuran_bunga_floating_perbulan:.2f}\t\t{angsuran_bunga_floating_perbulan:.2f}\t\t\t\t{angsuran_pokok_perbulan_dgn_bunga_floating:.2f}")

