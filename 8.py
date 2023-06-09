print("----Selamat Datang di Program Simulasi KPR----")
print("Menu program:")
print("A = Penentuan KPR berdasarkan harga yang Anda inginkan")
print("B = Rekomendasi harga rumah sesuai dengan gaji yang Anda miliki")

menu = input("Masukkan menu yang Anda pilih (ex: A) : ")
if menu == "A":
    HargaRumah = int(input("Masukkan harga rumah (ex: 500000000) : "))
    PersenDP = int(input("Masukkan %DP (ex: 20 ) : "))
    LamaCicilan = int(input("Masukkan lama cicilan dalam tahun (ex: 10) : "))

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

    # Menghitung angsuran pokok
    angsuran_pokok = TotalPinjaman / Konversi

    # Menghitung angsuran bunga tetap per bulan
    angsuran_bunga_fix_perbulan = TotalPinjaman * bunga_fix / 12

    # Menghitung angsuran per bulan menggunakan bunga fix
    angsuran_per_bulan_menggunakan_bunga_fix = angsuran_pokok + angsuran_bunga_fix_perbulan

    SisaBulan = Konversi - 60
    totalKPR5Tahun = angsuran_per_bulan_menggunakan_bunga_fix * 60
    angsuran_bunga_floating_perbulan = TotalPinjaman * bunga_fix / 12
    angsuran_per_bulan_menggunakan_bunga_floating = (TotalPinjaman - totalKPR5Tahun) / SisaBulan + angsuran_bunga_floating_perbulan

    total_KPR = (angsuran_per_bulan_menggunakan_bunga_fix + angsuran_per_bulan_menggunakan_bunga_floating) * Konversi
    minimal_gaji = total_KPR / (Konversi * 0.3)

    # OUTPUT
    print("===================================================================")
    print("Angsuran Pokok per bulan yang harus dibayarkan sebesar Rp", angsuran_pokok)
    print("===================================================================")
    print("Angsuran Bunga Fix per bulan yang harus dibayarkan sebesar Rp", angsuran_bunga_fix_perbulan)
    print("===================================================================")
    print("Total Angsuran menggunakan Bunga Fix per bulan yang harus dibayarkan sebesar Rp", angsuran_per_bulan_menggunakan_bunga_fix)
    print("===================================================================")
    print("Angsuran Bunga Floating per bulan yang harus dibayarkan sebesar Rp", angsuran_bunga_floating_perbulan)
    print("===================================================================")
    print("Total Angsuran menggunakan Bunga Floating per bulan yang harus dibayarkan sebesar Rp", angsuran_per_bulan_menggunakan_bunga_floating)
    print("===================================================================")
    print("Maka total KPR yang harus dibayarkan adalah Rp", total_KPR)
    print("===================================================================")
    print("Minimal gaji yang menyanggupi untuk mengambil KPR ini adalah Rp", minimal_gaji, "Per bulan")

    # Menampilkan tabel angsuran setiap bulan
    print("-----------------------------------------------------------------------")
    print("Bulan\t\tAngsuran Pokok\t\tAngsuran Bunga Fix\t\tAngsuran Per Bulan Menggunakan Bunga Fix")
    print("-----------------------------------------------------------------------")
    for bulan in range(1, Konversi + 1):
        if bulan <= 60:
            print(f"{bulan}\t\t{angsuran_pokok:.2f}\t\t\t{angsuran_bunga_fix_perbulan:.2f}\t\t\t\t{angsuran_per_bulan_menggunakan_bunga_fix:.2f}")
    print("-----------------------------------------------------------------------")

    # Menampilkan tabel angsuran setiap bulan dengan bunga floating
    if Konversi > 60:
        print("-----------------------------------------------------------------------")
        print("Bulan\t\tAngsuran Pokok\t\tAngsuran Bunga Floating\t\tAngsuran Per Bulan Menggunakan Bunga Floating")
        print("-----------------------------------------------------------------------")
        for bulan in range(61, Konversi + 1):
            print(f"{bulan}\t\t{angsuran_pokok:.2f}\t\t{angsuran_bunga_floating_perbulan:.2f}\t\t\t\t{angsuran_per_bulan_menggunakan_bunga_floating:.2f}")
        print("-----------------------------------------------------------------------")
elif menu == "B":
    Gaji = int(input("Masukkan gaji Anda dalam bulan!"))
    LamaCicilan = int(input("Masukkan lama cicilan yang anda inginkan! (dalam tahun (ex: 10)) : "))
    NominalDP = int(input("Masukkan Nominal DP yang Anda inginkan! "))

    Konversi = LamaCicilan * 12
    TotalUang = (Gaji * Konversi) - NominalDP

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

    # Menghitung angsuran pokok
    angsuran_pokok = TotalUang / Konversi

    # Menghitung angsuran bunga tetap per bulan
    angsuran_bunga_fix_perbulan = TotalUang * bunga_fix / 12

    # Menghitung angsuran per bulan menggunakan bunga fix
    angsuran_per_bulan_menggunakan_bunga_fix = angsuran_pokok + angsuran_bunga_fix_perbulan

    SisaBulan = Konversi - 60
    totalKPR5Tahun = angsuran_per_bulan_menggunakan_bunga_fix * 60
    angsuran_bunga_floating_perbulan = TotalUang * bunga_fix / 12
    angsuran_per_bulan_menggunakan_bunga_floating = (TotalUang - totalKPR5Tahun) / SisaBulan + angsuran_bunga_floating_perbulan

    SaranHargaRumah = (angsuran_per_bulan_menggunakan_bunga_fix + angsuran_per_bulan_menggunakan_bunga_floating) * Konversi

    # OUTPUT
    print("===================================================================")
    print("Angsuran Pokok per bulan yang harus dibayarkan sebesar Rp", angsuran_pokok)
    print("===================================================================")
    print("Angsuran Bunga Fix per bulan yang harus dibayarkan sebesar Rp", angsuran_bunga_fix_perbulan)
    print("===================================================================")
    print("Total Angsuran menggunakan Bunga Fix per bulan yang harus dibayarkan sebesar Rp", angsuran_per_bulan_menggunakan_bunga_fix)
    print("===================================================================")
    print("Angsuran Bunga Floating per bulan yang harus dibayarkan sebesar Rp", angsuran_bunga_floating_perbulan)
    print("===================================================================")
    print("Total Angsuran menggunakan Bunga Floating per bulan yang harus dibayarkan sebesar Rp", angsuran_per_bulan_menggunakan_bunga_floating)
    print("===================================================================")
    print("Maka saran harga rumah yang dapat diambil untuk KPR sebesar Rp", SaranHargaRumah)
    print("===================================================================")


    # Menampilkan tabel angsuran setiap bulan
    print("-----------------------------------------------------------------------")
    print("Bulan\t\tAngsuran Pokok\t\tAngsuran Bunga Fix\t\tAngsuran Per Bulan Menggunakan Bunga Fix")
    print("-----------------------------------------------------------------------")
    for bulan in range(1, Konversi + 1):
        if bulan <= 60:
            print(f"{bulan}\t\t{angsuran_pokok:.2f}\t\t\t{angsuran_bunga_fix_perbulan:.2f}\t\t\t\t{angsuran_per_bulan_menggunakan_bunga_fix:.2f}")
    print("-----------------------------------------------------------------------")

    # Menampilkan tabel angsuran setiap bulan dengan bunga floating
    if Konversi > 60:
        print("-----------------------------------------------------------------------")
        print("Bulan\t\tAngsuran Pokok\t\tAngsuran Bunga Floating\t\tAngsuran Per Bulan Menggunakan Bunga Floating")
        print("-----------------------------------------------------------------------")
        for bulan in range(61, Konversi + 1):
            print(f"{bulan}\t\t{angsuran_pokok:.2f}\t\t{angsuran_bunga_floating_perbulan:.2f}\t\t\t\t{angsuran_per_bulan_menggunakan_bunga_floating:.2f}")
        print("-----------------------------------------------------------------------")
else:
    print("Menu tidak valid. Silakan pilih menu yang sesuai.")