import json

def login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if check_credentials(username, password):
        print("Login berhasil!")
        input_harga_rumah()
    else:
        print("Username atau password salah.")
        main()

def check_credentials(username, password):
    try:
        with open('data.txt', 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
    
    if username in data and data[username] == password:
        return True
    else:
        return False

def register():
    username = input("Masukkan username baru: ")
    password = input("Masukkan password baru: ")
    
    try:
        with open('data.txt', 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
    
    data[username] = password
    
    with open('data.txt', 'w') as file:
        json.dump(data, file)
    
    print("Registrasi berhasil!")

def input_harga_rumah():
    # Kode untuk input harga rumah
    print("Masukkan harga rumah")

# Main program
def main():
    print("Selamat datang!")
    choice = input("Apakah Anda ingin login (L) atau register (R)? ").upper()

    if choice == 'L':
        login()
    elif choice == 'R':
        register()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

main()
print("----Selamat Datang di Program Simulasi KPR----")
print("Menu program:")
print("A = Penentuan KPR berdasarkan harga rumah yang Anda inginkan")
print("B = Rekomendasi harga rumah sesuai dengan gaji yang Anda miliki")

menu = input("Masukkan menu yang Anda pilih (ex: A) : ").upper()
if menu == "A":
    HargaRumah = int(input("Masukkan harga rumah (ex: 500000000): "))
    PersenDP = int(input("Masukkan %DP (ex: 20 ): "))
    Tenor = int(input("Masukkan lama cicilan dalam tahun (ex: 10): "))
    SisaKerja = int(input("Masukkan sisa masa kerja Anda:"))

    if SisaKerja < Tenor :
        print("===================================================================")
        print("Anda tidak disarankan untuk mengambil tenor dengan jangka waktu tersebut. Kami sarankan untuk mengambil tenor dengan jangka waktu di bawah atau setara dengan", SisaKerja, "tahun")

        DP = PersenDP / 100 * HargaRumah 
        Konversi = SisaKerja * 12
        SisaBulan = Konversi - 60
        KPR = HargaRumah - DP
        
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
        KPRbagiTahun = KPR / SisaKerja
        AngsuranPokok = KPR / Konversi

        Bunga_Fix = BungaFix (Konversi)
        AngsuranBungaFix = (KPRbagiTahun * Bunga_Fix) / 12

        Bunga_Floating = BungaFloating (Konversi)
        AngsuranBungaFloating = (KPRbagiTahun * Bunga_Floating) / 12

        TotalAngsuranPokok = AngsuranPokok * Konversi
        TotalAngsuranBungaFix = AngsuranBungaFix * 60 if Konversi > 60 else AngsuranBungaFix * Konversi
        TotalAngsuranBungaFloating = AngsuranBungaFloating * SisaBulan if Konversi > 60 else 0
        TotalAngsuranBunga = TotalAngsuranBungaFix + TotalAngsuranBungaFloating

        AngsuranperBulan5Tahun = AngsuranPokok + AngsuranBungaFix
        AngsuranperBulanSisaBulan = AngsuranPokok + AngsuranBungaFloating

        TotalKPR = TotalAngsuranPokok + TotalAngsuranBunga
        MinimalGaji = TotalKPR / (Konversi * 0.3)

        # OUTPUT
        print("===================================================================")
        print("Total Angsuran Bunga Fix yang dibayarkan: ", TotalAngsuranBungaFix)
        print("===================================================================")
        print("Total Angsuran Bunga Floating yang dibayarkan: ", TotalAngsuranBungaFloating)
        print("===================================================================")
        print("Total Angsuran Bunga yang dibayarkan: ", TotalAngsuranBunga)
        print("===================================================================")
        print("Sehingga total KPR yang diambil sebesar: ", TotalKPR)
        print("===================================================================")
        print("Minimal gaji yang direkomdasikan untuk mengambil KPR tersebut sebesar: ", MinimalGaji)
        print("===================================================================")
        print("===================================================================")

        # Menampilkan Tabel Angsuran Setiap Bulan
        print("-----------------------------------------------------------------------")
        print("Bulan\t\tAngsuran Pokok\t\tAngsuran Bunga Fix\t\tAngsuran Bunga Floating\t\t\t\tTotal Angsuran per Bulan")
        print("-----------------------------------------------------------------------")
        for bulan in range(1, Konversi + 1):
            if bulan <= 60:
                print(f"{bulan}\t\t{AngsuranPokok:.2f}\t\t{AngsuranBungaFix:.2f}\t\t\t\t\t0.00\t\t\t\t\t\t{AngsuranperBulan5Tahun:.2f}")
            else:
                print(f"{bulan}\t\t{AngsuranPokok:.2f}\t\t0.00\t\t\t\t\t{AngsuranBungaFloating:.2f}\t\t\t\t\t\t{AngsuranperBulanSisaBulan:.2f}")

        import matplotlib.pyplot as plt

        # Data untuk Diagram Garis
        bulan = list(range(1, Konversi + 1))  # Progres bulan
        y = []
        for i in range(1, Konversi + 1):
            if i <= 60:
                y.append(AngsuranperBulan5Tahun)
            else:
                y.append(AngsuranperBulanSisaBulan)

        # Membuat Diagram Garis
        plt.plot(bulan, y, marker='o', linestyle='-', color='b')

        # Menampilkan Judul dan Label Sumbu
        plt.title('Progres Bulan vs Total Angsuran per Bulan')
        plt.xlabel('Bulan')
        plt.ylabel('Total Angsuran per Bulan')

        # Menampilkan Diagram Garis
        plt.show()

    else :
        DP = PersenDP / 100 * HargaRumah 
        Konversi = Tenor * 12
        SisaBulan = Konversi - 60
        KPR = HargaRumah - DP
        
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

        AngsuranPokok = KPR / Konversi
        KPRbagiTahun = KPR / Tenor

        Bunga_Fix = BungaFix (Konversi)
        AngsuranBungaFix = (KPRbagiTahun * Bunga_Fix) / 12

        Bunga_Floating = BungaFloating (Konversi)
        AngsuranBungaFloating = (KPRbagiTahun) * Bunga_Floating / 12

        TotalAngsuranPokok = AngsuranPokok * Konversi
        TotalAngsuranBungaFix = AngsuranBungaFix * 60 if Konversi > 60 else AngsuranBungaFix * Konversi
        TotalAngsuranBungaFloating = AngsuranBungaFloating * SisaBulan if Konversi > 60 else 0
        TotalAngsuranBunga = TotalAngsuranBungaFix + TotalAngsuranBungaFloating

        AngsuranperBulan5Tahun = AngsuranPokok + AngsuranBungaFix
        AngsuranperBulanSisaBulan = AngsuranPokok + AngsuranBungaFloating

        TotalKPR = TotalAngsuranPokok + TotalAngsuranBunga
        MinimalGaji = TotalKPR / (Konversi * 0.3)

        # OUTPUT
        print("===================================================================")
        print("===================================================================")
        print("Total Angsuran Bunga Fix yang dibayarkan: ", TotalAngsuranBungaFix)
        print("===================================================================")
        print("Total Angsuran Bunga Floating yang dibayarkan: ", TotalAngsuranBungaFloating)
        print("===================================================================")
        print("Total Angsuran Bunga yang dibayarkan: ", TotalAngsuranBunga)
        print("===================================================================")
        print("Sehingga total KPR yang diambil sebesar: ", TotalKPR)
        print("===================================================================")
        print("Minimal gaji yang direkomdasikan untuk mengambil KPR tersebut sebesar: ", MinimalGaji)
        print("===================================================================")
        print("===================================================================")

        # Menampilkan Tabel Angsuran Setiap Bulan
        print("-----------------------------------------------------------------------")
        print("Bulan\t\tAngsuran Pokok\t\tAngsuran Bunga Fix\t\tAngsuran Bunga Floating\t\t\t\tTotal Angsuran per Bulan")
        print("-----------------------------------------------------------------------")
        for bulan in range(1, Konversi + 1):
            if bulan <= 60:
                print(f"{bulan}\t\t{AngsuranPokok:.2f}\t\t{AngsuranBungaFix:.2f}\t\t\t\t\t0.00\t\t\t\t\t\t{AngsuranperBulan5Tahun:.2f}")
            else:
                print(f"{bulan}\t\t{AngsuranPokok:.2f}\t\t0.00\t\t\t\t\t{AngsuranBungaFloating:.2f}\t\t\t\t\t\t{AngsuranperBulanSisaBulan:.2f}")

        import matplotlib.pyplot as plt

        # Data untuk Diagram Garis
        bulan = list(range(1, Konversi + 1))  # Progres bulan
        y = []
        for i in range(1, Konversi + 1):
            if i <= 60:
                y.append(AngsuranperBulan5Tahun)
            else:
                y.append(AngsuranperBulanSisaBulan)

        # Membuat Diagram Garis
        plt.plot(bulan, y, marker='o', linestyle='-', color='b')

        # Menampilkan Judul dan Label Sumbu
        plt.title('Progres Bulan vs Total Angsuran per Bulan')
        plt.xlabel('Bulan')
        plt.ylabel('Total Angsuran per Bulan')

        # Menampilkan Diagram Garis
        plt.show()


elif menu == "B":
    GajiBulanan = int(input("Masukkan gaji bulanan Anda: "))
    Tenor = int(input("Masukkan lama KPR yang ingin Anda ambil(dalam tahun): "))
    SisaKerja = int(input("Masukkan sisa masa kerja Anda:"))

    if SisaKerja < Tenor :
        print("===================================================================")
        print("Anda tidak disarankan untuk mengambil tenor dengan jangka waktu tersebut. Kami sarankan untuk mengambil tenor dengan jangka waktu dibawah atau setara dengan", SisaKerja, "tahun")
        
        Konversi = SisaKerja * 12
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
            AngsuranBungaFix = MaksAngsuran * Bunga_Fix/12

            Bunga_Floating = BungaFloating (Konversi)
            AngsuranBungaFloating = MaksAngsuran * Bunga_Floating/12

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

        # Menampilkan Tabel Angsuran Setiap Bulan
        print("-----------------------------------------------------------------------")
        print("Bulan\t\tAngsuran Pokok\t\tAngsuran Bunga Fix\t\tAngsuran Bunga Floating\t\t\t\tTotal Angsuran per Bulan")
        print("-----------------------------------------------------------------------")
        for bulan in range(1, Konversi + 1):
            if bulan <= 60:
                print(f"{bulan}\t\t{AngsuranPokok:.2f}\t\t{AngsuranBungaFix:.2f}\t\t\t\t\t0.00\t\t\t\t\t\t{AngsuranperBulan5Tahun:.2f}")
            else:
                print(f"{bulan}\t\t{AngsuranPokok:.2f}\t\t0.00\t\t\t\t\t{AngsuranBungaFloating:.2f}\t\t\t\t\t\t{AngsuranperBulanSisaBulan:.2f}")

        import matplotlib.pyplot as plt

        # Data untuk Diagram Garis
        bulan = list(range(1, Konversi + 1))  # Progres bulan
        y = []
        for i in range(1, Konversi + 1):
            if i <= 60:
                y.append(AngsuranperBulan5Tahun)
            else:
                y.append(AngsuranperBulanSisaBulan)

        # Membuat Diagram Garis
        plt.plot(bulan, y, marker='o', linestyle='-', color='b')

        # Menampilkan judul dan label sumbu
        plt.title('Progres Bulan vs Total Angsuran per Bulan')
        plt.xlabel('Bulan')
        plt.ylabel('Total Angsuran per Bulan')

        # Menampilkan Diagram Garis
        plt.show()

        from PIL import Image

        # Memuat dan Menampilkan Gambar
        if SaranHargaRumah <= 150000000:
            TipeA = Image.open("TipeA.jpg")
            TipeA.show()
        elif 150000001 <= SaranHargaRumah <= 300000000:
            TipeB = Image.open("TipeB.jpg")
            TipeB.show()
        elif 300000001 <= SaranHargaRumah <= 450000000:
            TipeC = Image.open("TipeC.jpg")
            TipeC.show()
        elif 450000001 <= SaranHargaRumah <= 600000000:
            TipeD = Image.open("TipeD.jpg")
            TipeD.show()
        elif 600000001 <= SaranHargaRumah <= 850000000:
            TipeE = Image.open("TipeE.jpg")
            TipeE.show()
        elif 850000001 <= SaranHargaRumah <= 1300000000:
            TipeF = Image.open("TipeF.jpg")
            TipeF.show()
        elif 1300000001 <= SaranHargaRumah <= 1550000000:
            TipeG = Image.open("TipeG.jpg")
            TipeG.show()
        elif 1550000001 <= SaranHargaRumah <= 1800000000:
            TipeH = Image.open("TipeH.jpg")
            TipeH.show()
        elif 1800000001 <= SaranHargaRumah <= 2050000000:
            TipeI = Image.open("TipeI.jpg")
            TipeI.show()
        elif 2050000001 <= SaranHargaRumah <= 2550000000:
            TipeJ = Image.open("TipeJ.jpg")
            TipeJ.show()
        elif 2550000001 <= SaranHargaRumah <= 3050000000:
            TipeK = Image.open("TipeK.jpg")
            TipeK.show()
        elif 3050000001 <= SaranHargaRumah <= 3550000000:
            TipeL = Image.open("TipeL.jpg")
            TipeL.show()
        elif 3550000001 <= SaranHargaRumah <= 4050000000:
            TipeM = Image.open("TipeM.jpg")
            TipeM.show()
        elif 4050000001 <= SaranHargaRumah <= 4550000000:
            TipeN = Image.open("TipeN.jpg")
            TipeN.show()
        elif 4550000001 <= SaranHargaRumah <= 5050000000:
            TipeO = Image.open("TipeO.jpg")
            TipeO.show()
        elif 5050000001 <= SaranHargaRumah <= 6050000000:
            TipeP = Image.open("TipeP.jpg")
            TipeP.show()
        elif 6050000001 <= SaranHargaRumah <= 7050000000:
            TipeQ = Image.open("TipeQ.jpg")
            TipeQ.show()
        elif 7050000001 <= SaranHargaRumah <= 8050000000:
            TipeR = Image.open("TipeR.jpg")
            TipeR.show()
        elif 8050000001 <= SaranHargaRumah <= 9050000000:
            TipeS = Image.open("TipeS.jpg")
            TipeS.show()
        elif 9050000001 <= SaranHargaRumah <= 10050000000:
            TipeT = Image.open("TipeT.jpg")
            TipeT.show()
        elif 10050000001 <= SaranHargaRumah <= 15050000000:
            TipeU = Image.open("TipeU.jpg")
            TipeU.show()
        elif 15050000001 <= SaranHargaRumah <= 20050000000:
            TipeV = Image.open("TipeV.jpg")
            TipeV.show()
        elif 20050000001 <= SaranHargaRumah <= 25050000000:
            TipeW = Image.open("TipeW.jpg")
            TipeW.show()
        elif 25050000001 <= SaranHargaRumah <= 30050000000:
            TipeX = Image.open("TipeX.jpg")
            TipeX.show()
        elif 30050000001 <= SaranHargaRumah <= 35050000000: 
            TipeY = Image.open("TipeY.jpg")
            TipeY.show()
        elif 35050000001 <= SaranHargaRumah <= 40050000000: 
            TipeZ = Image.open("TipeZ.jpg")
            TipeZ.show()
        else:
            TipeAA = Image.open("TipeAA.jpg")
    else:
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
            AngsuranBungaFix = MaksAngsuran * Bunga_Fix/12

            Bunga_Floating = BungaFloating (Konversi)
            AngsuranBungaFloating = MaksAngsuran * Bunga_Floating/12

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

        # Menampilkan Tabel Angsuran Setiap Bulan
        print("-----------------------------------------------------------------------")
        print("Bulan\t\tAngsuran Pokok\t\tAngsuran Bunga Fix\t\tAngsuran Bunga Floating\t\t\t\tTotal Angsuran per Bulan")
        print("-----------------------------------------------------------------------")
        for bulan in range(1, Konversi + 1):
            if bulan <= 60:
                print(f"{bulan}\t\t{AngsuranPokok:.2f}\t\t{AngsuranBungaFix:.2f}\t\t\t\t\t0.00\t\t\t\t\t\t{AngsuranperBulan5Tahun:.2f}")
            else:
                print(f"{bulan}\t\t{AngsuranPokok:.2f}\t\t0.00\t\t\t\t\t{AngsuranBungaFloating:.2f}\t\t\t\t\t\t{AngsuranperBulanSisaBulan:.2f}")

        import matplotlib.pyplot as plt

        # Data untuk Diagram Garis
        bulan = list(range(1, Konversi + 1))  # Progres bulan
        y = []
        for i in range(1, Konversi + 1):
            if i <= 60:
                y.append(AngsuranperBulan5Tahun)
            else:
                y.append(AngsuranperBulanSisaBulan)

        # Membuat diagram garis
        plt.plot(bulan, y, marker='o', linestyle='-', color='b')

        # Menampilkan Judul dan Label Sumbu
        plt.title('Progres Bulan vs Total Angsuran per Bulan')
        plt.xlabel('Bulan')
        plt.ylabel('Total Angsuran per Bulan')

        # Menampilkan Diagram Garis
        plt.show()
        
        from PIL import Image

        # Memuat dan Menampilkan Gambar
        if SaranHargaRumah <= 150000000:
            TipeA = Image.open('TipeA.jpg')

            # Tampilkan gambar dalam pop-up
            plt.imshow(TipeA)
            plt.axis('off')
            plt.show()

        elif 150000001 <= SaranHargaRumah <= 300000000:
            TipeB = Image.open("TipeB.jpg")
            TipeB.show()
        elif 300000001 <= SaranHargaRumah <= 450000000:
            TipeC = Image.open("TipeC.jpg")
            TipeC.show()
        elif 450000001 <= SaranHargaRumah <= 600000000:
            TipeD = Image.open("TipeD.jpg")
            TipeD.show()
        elif 600000001 <= SaranHargaRumah <= 850000000:
            TipeE = Image.open("TipeE.jpg")
            TipeE.show()
        elif 850000001 <= SaranHargaRumah <= 1300000000:
            TipeF = Image.open("TipeF.jpg")
            TipeF.show()
        elif 1300000001 <= SaranHargaRumah <= 1550000000:
            TipeG = Image.open("TipeG.jpg")
            TipeG.show()
        elif 1550000001 <= SaranHargaRumah <= 1800000000:
            TipeH = Image.open("TipeH.jpg")
            TipeH.show()
        elif 1800000001 <= SaranHargaRumah <= 2050000000:
            TipeI = Image.open("TipeI.jpg")
            TipeI.show()
        elif 2050000001 <= SaranHargaRumah <= 2550000000:
            TipeJ = Image.open("TipeJ.jpg")
            TipeJ.show()
        elif 2550000001 <= SaranHargaRumah <= 3050000000:
            TipeK = Image.open("TipeK.jpg")
            TipeK.show()
        elif 3050000001 <= SaranHargaRumah <= 3550000000:
            TipeL = Image.open("TipeL.jpg")
            TipeL.show()
        elif 3550000001 <= SaranHargaRumah <= 4050000000:
            TipeM = Image.open("TipeM.jpg")
            TipeM.show()
        elif 4050000001 <= SaranHargaRumah <= 4550000000:
            TipeN = Image.open("TipeN.jpg")
            TipeN.show()
        elif 4550000001 <= SaranHargaRumah <= 5050000000:
            TipeO = Image.open("TipeO.jpg")
            TipeO.show()
        elif 5050000001 <= SaranHargaRumah <= 6050000000:
            TipeP = Image.open("TipeP.jpg")
            TipeP.show()
        elif 6050000001 <= SaranHargaRumah <= 7050000000:
            TipeQ = Image.open("TipeQ.jpg")
            TipeQ.show()
        elif 7050000001 <= SaranHargaRumah <= 8050000000:
            TipeR = Image.open("TipeR.jpg")
            TipeR.show()
        elif 8050000001 <= SaranHargaRumah <= 9050000000:
            TipeS = Image.open("TipeS.jpg")
            TipeS.show()
        elif 9050000001 <= SaranHargaRumah <= 10050000000:
            TipeT = Image.open("TipeT.jpg")
            TipeT.show()
        elif 10050000001 <= SaranHargaRumah <= 15050000000:
            TipeU = Image.open("TipeU.jpg")
            TipeU.show()
        elif 15050000001 <= SaranHargaRumah <= 20050000000:
            TipeV = Image.open("TipeV.jpg")
            TipeV.show()
        elif 20050000001 <= SaranHargaRumah <= 25050000000:
            TipeW = Image.open("TipeW.jpg")
            TipeW.show()
        elif 25050000001 <= SaranHargaRumah <= 30050000000:
            TipeX = Image.open("TipeX.jpg")
            TipeX.show()
        elif 30050000001 <= SaranHargaRumah <= 35050000000: 
            TipeY = Image.open("TipeY.jpg")
            TipeY.show()
        elif 35050000001 <= SaranHargaRumah <= 40050000000: 
            TipeZ = Image.open("TipeZ.jpg")
            TipeZ.show()
        else:
            TipeAA = Image.open("TipeAA.jpg")
else: 
    print("Menu tidak valid. Silakan pilih menu yang sesuai.")
