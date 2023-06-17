import json
import matplotlib.pyplot as plt
from termcolor import colored
from PIL import Image

print("")
def login():
    username = input(colored("Masukkan username: ","yellow"))
    password = input(colored("Masukkan password: ","yellow"))

    if check_credentials(username, password):
        print(colored("Login berhasil!","green"))
    else:
        print(colored("Username atau password salah.","red"))
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
    username = input(colored("Masukkan username baru: ","yellow"))
    password = input(colored("Masukkan password baru: ","yellow"))
    
    try:
        with open('data.txt', 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
    
    data[username] = password
    
    with open('data.txt', 'w') as file:
        json.dump(data, file)
    
    print(colored("Registrasi berhasil!","green"))

def input_harga_rumah():
    # Kode untuk input harga rumah
    print(colored("Masukkan harga rumah","yellow"))

# Main program
def main():
    print(colored("===========================================================================================================","green",))
    print(colored("                                       Selamat datang di Simulasi KPR !!                                   ","yellow",attrs=['bold']))
    print(colored("                 KPR (Kredit Pemilikan Rumah) adalah fasilitas pinjaman yang disediakan oleh               ","yellow"))
    print(colored("                        bank atau lembaga keuangan untuk membeli atau memiliki rumah.                        ","yellow"))
    print(colored("===========================================================================================================","green"))
    
    while True:
        choice = input(colored("Apakah Anda ingin login (L) atau register (R)? ","green")).upper()
        if choice == 'L':
            login()
            break
        elif choice == 'R':
            register()
            break
        else:
            print(colored("Pilihan tidak valid. Silakan coba lagi.","red"))
            
main()
print(colored("===========================================================================================================","green"))
print(colored("Menu program:","blue"))
print(colored("A = Penentuan KPR berdasarkan harga rumah yang Anda inginkan","blue"))
print(colored("B = Rekomendasi harga rumah sesuai dengan gaji yang Anda miliki","blue"))
print(colored("===========================================================================================================","green"))
while True:
    menu = input(colored("Masukkan menu yang Anda pilih (ex: A) : ","yellow")).upper()
    if menu == "A":
        print(colored("===========================================================================================================","green"))
        HargaRumah = int(input(colored("Masukkan harga rumah (ex: 500000000): ","yellow")))
        print(colored("===========================================================================================================","green"))
        PersenDP = int(input(colored("Masukkan %DP (ex: 20 ): ","yellow")))
        print(colored("===========================================================================================================","green"))
        Tenor = int(input(colored("Masukkan lama cicilan dalam tahun (ex: 10): ","yellow")))
        print(colored("===========================================================================================================","green"))
        SisaKerja = int(input(colored("Masukkan sisa masa kerja Anda (tahun): ","yellow")))
        print(colored("===========================================================================================================","green"))
        if SisaKerja < Tenor :
            print(colored("===========================================================================================================","green"))
            print(colored("Anda","red"),colored("TIDAK","red",attrs=['bold']),colored("disarankan untuk mengambil tenor dengan jangka waktu tersebut.","red")) 
            print(colored("Kami sarankan untuk mengambil tenor dengan jangka waktu di bawah atau setara dengan","red"), colored(SisaKerja,"red"), colored("tahun","red"))

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
            print(colored("===========================================================================================================","green"))
            print(colored("Total Angsuran Bunga Fix yang dibayarkan: ","yellow"),colored(TotalAngsuranBungaFix,"green"))
            print(colored("===========================================================================================================","green"))
            print(colored("Total Angsuran Bunga Floating yang dibayarkan: ","yellow"),colored( TotalAngsuranBungaFloating,"green"))
            print(colored("===========================================================================================================","green"))
            print(colored("Total Angsuran Bunga yang dibayarkan: ","yellow"),colored (TotalAngsuranBunga,"green"))
            print(colored("===========================================================================================================","green"))
            print(colored("Sehingga total KPR yang diambil sebesar: ","yellow"),colored( TotalKPR,"green"))
            print(colored("===========================================================================================================","green"))
            print(colored("Minimal gaji yang direkomdasikan untuk mengambil KPR tersebut sebesar: ","yellow"),colored(MinimalGaji,"green"))
            print(colored("===========================================================================================================","green"))

            # Menampilkan Tabel Angsuran Setiap Bulan
            print(colored("----------------------------------------------------------------------------------------------------------------------------------------------------------------","yellow"))
            print("Bulan\t\tAngsuran Pokok\t\tAngsuran Bunga Fix\t\tAngsuran Bunga Floating\t\t\t\tTotal Angsuran per Bulan")
            print(colored("----------------------------------------------------------------------------------------------------------------------------------------------------------------","yellow"))
            for bulan in range(1, Konversi + 1):
                if bulan <= 60:
                    print(f"{bulan}\t\t{AngsuranPokok:.2f}\t\t{AngsuranBungaFix:.2f}\t\t\t\t\t0.00\t\t\t\t\t\t{AngsuranperBulan5Tahun:.2f}")
                    break
                else:
                    print(f"{bulan}\t\t{AngsuranPokok:.2f}\t\t0.00\t\t\t\t\t{AngsuranBungaFloating:.2f}\t\t\t\t\t\t{AngsuranperBulanSisaBulan:.2f}")
                    break

            # Data untuk Diagram Garis
            bulan = list(range(1, Konversi + 1))  # Progres bulan
            y = []
            for i in range(1, Konversi + 1):
                if i <= 60:
                    y.append(AngsuranperBulan5Tahun)
                    break
                else:
                    y.append(AngsuranperBulanSisaBulan)
                    break

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
            print(colored("===========================================================================================================","green"))  
            print(colored("Total Angsuran Bunga Fix yang dibayarkan: ","yellow"),colored(TotalAngsuranBungaFix,"green"))
            print(colored("===========================================================================================================","green"))  
            print(colored("Total Angsuran Bunga Floating yang dibayarkan: ","yellow"),colored( TotalAngsuranBungaFloating,"green"))
            print(colored("===========================================================================================================","green"))  
            print(colored("Total Angsuran Bunga yang dibayarkan: ","yellow"),colored (TotalAngsuranBunga,"green"))
            print(colored("===========================================================================================================","green"))  
            print(colored("Sehingga total KPR yang diambil sebesar: ","yellow"),colored( TotalKPR,"green"))
            print(colored("===========================================================================================================","green"))  
            print(colored("Minimal gaji yang direkomdasikan untuk mengambil KPR tersebut sebesar: ","yellow"),colored(MinimalGaji,"green"))
            print(colored("===========================================================================================================","green"))  
            print(colored("===========================================================================================================","green"))  

            # Menampilkan Tabel Angsuran Setiap Bulan
            print(colored("----------------------------------------------------------------------------------------------------------------------------------------------------------------","yellow"))
            print("Bulan\t\tAngsuran Pokok\t\tAngsuran Bunga Fix\t\tAngsuran Bunga Floating\t\t\t\tTotal Angsuran per Bulan")
            print(colored("----------------------------------------------------------------------------------------------------------------------------------------------------------------","yellow"))
            for bulan in range(1, Konversi + 1):
                if bulan <= 60:
                    print(f"{bulan}\t\t{AngsuranPokok:.2f}\t\t{AngsuranBungaFix:.2f}\t\t\t\t\t0.00\t\t\t\t\t\t{AngsuranperBulan5Tahun:.2f}")
                    
                else:
                    print(f"{bulan}\t\t{AngsuranPokok:.2f}\t\t0.00\t\t\t\t\t{AngsuranBungaFloating:.2f}\t\t\t\t\t\t{AngsuranperBulanSisaBulan:.2f}")
                    
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
            break
            
    elif menu == "B":
        print(colored("===========================================================================================================","green"))
        GajiBulanan = int(input(colored("Masukkan gaji bulanan Anda: ","yellow")))
        print(colored("===========================================================================================================","green"))
        Tenor = int(input(colored("Masukkan lama KPR yang ingin Anda ambil(dalam tahun): ","yellow")))
        print(colored("===========================================================================================================","green"))
        SisaKerja = int(input(colored("Masukkan sisa masa kerja Anda (tahun):","yellow")))
        print(colored("===========================================================================================================","green"))

        if SisaKerja < Tenor :
            print(colored("===========================================================================================================","green"))
            print(colored("Anda","red"),colored("TIDAK","red",attrs=['bold']),colored("disarankan untuk mengambil tenor dengan jangka waktu tersebut.","red")) 
            print(colored("Kami sarankan untuk mengambil tenor dengan jangka waktu di bawah atau setara dengan","red"), colored(SisaKerja,"red"), colored("tahun","red"))
            
            Konversi = SisaKerja * 12
            SisaBulan = Konversi - 60

            def BungaFix (Konversi):
                if Konversi <= 60:
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
            print(colored("===========================================================================================================","green"))
            print(colored("Saran harga rumah yang dapat diambil sebesar: ","yellow"), colored(SaranHargaRumah,"green"))
            print(colored("===========================================================================================================","green"))
            print(colored("Total Angsuran Pokok yang dibayarkan sebesar saran harga rumah", "yellow"))
            print(colored("===========================================================================================================","green"))
            print(colored("Total Angsuran Bunga Fix yang dibayarkan: ","yellow"),colored(TotalAngsuranBungaFix,"green"))
            print(colored("===========================================================================================================","green"))
            print(colored("Total Angsuran Bunga Floating yang dibayarkan: ","yellow"),colored( TotalAngsuranBungaFloating,"green"))
            print(colored("===========================================================================================================","green"))
            print(colored("Total Angsuran Bunga yang dibayarkan: ","yellow"),colored (TotalAngsuranBunga,"green"))
            print(colored("===========================================================================================================","green"))
            print(colored("===========================================================================================================","green"))

            # Menampilkan Tabel Angsuran Setiap Bulan
            print(colored("----------------------------------------------------------------------------------------------------------------------------------------------------------------","yellow"))
            print("Bulan\t\tAngsuran Pokok\t\tAngsuran Bunga Fix\t\tAngsuran Bunga Floating\t\t\t\tTotal Angsuran per Bulan")
            print(colored("----------------------------------------------------------------------------------------------------------------------------------------------------------------","yellow"))
            for bulan in range(1, Konversi + 1):
                if bulan <= 60:
                    print(f"{bulan}\t\t{AngsuranPokok:.2f}\t\t{AngsuranBungaFix:.2f}\t\t\t\t\t0.00\t\t\t\t\t\t{AngsuranperBulan5Tahun:.2f}")
                    break
                else:
                    print(f"{bulan}\t\t{AngsuranPokok:.2f}\t\t0.00\t\t\t\t\t{AngsuranBungaFloating:.2f}\t\t\t\t\t\t{AngsuranperBulanSisaBulan:.2f}")
                    break

            # Data untuk Diagram Garis
            bulan = list(range(1, Konversi + 1))  # Progres bulan
            y = []
            for i in range(1, Konversi + 1):
                if i <= 60:
                    y.append(AngsuranperBulan5Tahun)
                    break
                else:
                    y.append(AngsuranperBulanSisaBulan)
                    break

            # Membuat Diagram Garis
            plt.plot(bulan, y, marker='o', linestyle='-', color='b')

            # Menampilkan judul dan label sumbu
            plt.title('Progres Bulan vs Total Angsuran per Bulan')
            plt.xlabel('Bulan')
            plt.ylabel('Total Angsuran per Bulan')

            # Menampilkan Diagram Garis
            plt.show()

            # Memuat dan Menampilkan Gambar
            if SaranHargaRumah <= 150000000:
                image = Image.open('TipeA.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 150000001 <= SaranHargaRumah <= 300000000:
                image = Image.open('TipeB.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 300000001 <= SaranHargaRumah <= 450000000:
                image = Image.open('TipeC.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 450000001 <= SaranHargaRumah <= 600000000:
                image = Image.open('TipeD.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 600000001 <= SaranHargaRumah <= 850000000:
                image = Image.open('TipeE.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 850000001 <= SaranHargaRumah <= 1300000000:
                image = Image.open('TipeF.jpg')
                # Tampilkan gambar dalam pop-up
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 1300000001 <= SaranHargaRumah <= 1550000000:
                image = Image.open('TipeG.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 1550000001 <= SaranHargaRumah <= 1800000000:
                image = Image.open('TipeH.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 1800000001 <= SaranHargaRumah <= 2050000000:
                image = Image.open('TipeI.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 2050000001 <= SaranHargaRumah <= 2550000000:
                image = Image.open('TipeJ.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 2550000001 <= SaranHargaRumah <= 3050000000:
                image = Image.open('TipeK.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 3050000001 <= SaranHargaRumah <= 3550000000:
                image = Image.open('TipeL.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 3550000001 <= SaranHargaRumah <= 4050000000:
                image = Image.open('TipeM.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 4050000001 <= SaranHargaRumah <= 4550000000:
                image = Image.open('TipeN.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 4550000001 <= SaranHargaRumah <= 5050000000:
                image = Image.open('TipeO.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 5050000001 <= SaranHargaRumah <= 6050000000:
                image = Image.open('TipeP.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 6050000001 <= SaranHargaRumah <= 7050000000:
                image = Image.open('TipeQ.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 7050000001 <= SaranHargaRumah <= 8050000000:
                image = Image.open('TipeR.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 8050000001 <= SaranHargaRumah <= 9050000000:
                image = Image.open('TipeS.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 9050000001 <= SaranHargaRumah <= 10050000000:
                image = Image.open('TipeT.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 10050000001 <= SaranHargaRumah <= 15050000000:
                image = Image.open('TipeU.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 15050000001 <= SaranHargaRumah <= 20050000000:
                image = Image.open('TipeV.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 20050000001 <= SaranHargaRumah <= 25050000000:
                image = Image.open('TipeW.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 25050000001 <= SaranHargaRumah <= 30050000000:
                image = Image.open('TipeX.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 30050000001 <= SaranHargaRumah <= 35050000000: 
                image = Image.open('TipeY.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 35050000001 <= SaranHargaRumah <= 40050000000: 
                image = Image.open('TipeZ.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            else:
                image = Image.open('TipeAA.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break

        else:
            Konversi = Tenor * 12
            SisaBulan = Konversi - 60

            def BungaFix (Konversi):
                if Konversi <= 60:
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
            print(colored("===========================================================================================================","green"))
            print("Saran harga rumah yang dapat diambil sebesar: ", SaranHargaRumah)
            print("Total Angsuran Pokok yang dibayarkan sebesar saran harga rumah")
            print(colored("===========================================================================================================","green"))
            print(colored("Total Angsuran Bunga Fix yang dibayarkan: ","yellow"),colored(TotalAngsuranBungaFix,"green"))
            print(colored("===========================================================================================================","green"))
            print(colored("Total Angsuran Bunga Floating yang dibayarkan: ","yellow"),colored( TotalAngsuranBungaFloating,"green"))
            print(colored("===========================================================================================================","green"))
            print(colored("Total Angsuran Bunga yang dibayarkan: ","yellow"),colored (TotalAngsuranBunga,"green"))
            print(colored("===========================================================================================================","green"))

            # Menampilkan Tabel Angsuran Setiap Bulan
            print(colored("----------------------------------------------------------------------------------------------------------------------------------------------------------------","yellow"))
            print("Bulan\t\tAngsuran Pokok\t\tAngsuran Bunga Fix\t\tAngsuran Bunga Floating\t\t\t\tTotal Angsuran per Bulan")
            print(colored("----------------------------------------------------------------------------------------------------------------------------------------------------------------","yellow"))
            for bulan in range(1, Konversi + 1):
                if bulan <= 60:
                    print(f"{bulan}\t\t{AngsuranPokok:.2f}\t\t{AngsuranBungaFix:.2f}\t\t\t\t\t0.00\t\t\t\t\t\t{AngsuranperBulan5Tahun:.2f}")
                else:
                    print(f"{bulan}\t\t{AngsuranPokok:.2f}\t\t0.00\t\t\t\t\t{AngsuranBungaFloating:.2f}\t\t\t\t\t\t{AngsuranperBulanSisaBulan:.2f}")

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

            # Memuat dan Menampilkan Gambar
            if SaranHargaRumah <= 150000000:
                image = Image.open('TipeA.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 150000001 <= SaranHargaRumah <= 300000000:
                image = Image.open('TipeB.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 300000001 <= SaranHargaRumah <= 450000000:
                image = Image.open('TipeC.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 450000001 <= SaranHargaRumah <= 600000000:
                image = Image.open('TipeD.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 600000001 <= SaranHargaRumah <= 850000000:
                image = Image.open('TipeE.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 850000001 <= SaranHargaRumah <= 1300000000:
                image = Image.open('TipeF.jpg')
                # Tampilkan gambar dalam pop-up
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 1300000001 <= SaranHargaRumah <= 1550000000:
                image = Image.open('TipeG.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 1550000001 <= SaranHargaRumah <= 1800000000:
                image = Image.open('TipeH.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 1800000001 <= SaranHargaRumah <= 2050000000:
                image = Image.open('TipeI.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 2050000001 <= SaranHargaRumah <= 2550000000:
                image = Image.open('TipeJ.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 2550000001 <= SaranHargaRumah <= 3050000000:
                image = Image.open('TipeK.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 3050000001 <= SaranHargaRumah <= 3550000000:
                image = Image.open('TipeL.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 3550000001 <= SaranHargaRumah <= 4050000000:
                image = Image.open('TipeM.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 4050000001 <= SaranHargaRumah <= 4550000000:
                image = Image.open('TipeN.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 4550000001 <= SaranHargaRumah <= 5050000000:
                image = Image.open('TipeO.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 5050000001 <= SaranHargaRumah <= 6050000000:
                image = Image.open('TipeP.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 6050000001 <= SaranHargaRumah <= 7050000000:
                image = Image.open('TipeQ.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 7050000001 <= SaranHargaRumah <= 8050000000:
                image = Image.open('TipeR.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 8050000001 <= SaranHargaRumah <= 9050000000:
                image = Image.open('TipeS.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 9050000001 <= SaranHargaRumah <= 10050000000:
                image = Image.open('TipeT.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 10050000001 <= SaranHargaRumah <= 15050000000:
                image = Image.open('TipeU.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
            elif 15050000001 <= SaranHargaRumah <= 20050000000:
                image = Image.open('TipeV.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 20050000001 <= SaranHargaRumah <= 25050000000:
                image = Image.open('TipeW.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 25050000001 <= SaranHargaRumah <= 30050000000:
                image = Image.open('TipeX.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 30050000001 <= SaranHargaRumah <= 35050000000: 
                image = Image.open('TipeY.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            elif 35050000001 <= SaranHargaRumah <= 40050000000: 
                image = Image.open('TipeZ.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
            else:
                image = Image.open('TipeAA.jpg')
                plt.imshow(image)
                plt.axis('off')
                plt.show()
                break
    else: 
        print(colored("Menu tidak valid. Silakan pilih menu yang sesuai.","yellow")) 

mengulang = input('Apakah anda ingin menggunakan program lagi?  y/n:')
if mengulang.lower()=='y':
    mengulang = True
else:
    mengulang = False
    print('-'*100,'\nProgram Selesai')     

while mengulang: 
    print(colored("===========================================================================================================","green"))
    print(colored("Menu program:","blue"))
    print(colored("A = Penentuan KPR berdasarkan harga rumah yang Anda inginkan","blue"))
    print(colored("B = Rekomendasi harga rumah sesuai dengan gaji yang Anda miliki","blue"))
    print(colored("===========================================================================================================","green"))
    while True:
        menu = input(colored("Masukkan menu yang Anda pilih (ex: A) : ","yellow")).upper()
        if menu == "A":
            print(colored("===========================================================================================================","green"))
            HargaRumah = int(input(colored("Masukkan harga rumah (ex: 500000000): ","yellow")))
            print(colored("===========================================================================================================","green"))
            PersenDP = int(input(colored("Masukkan %DP (ex: 20 ): ","yellow")))
            print(colored("===========================================================================================================","green"))
            Tenor = int(input(colored("Masukkan lama cicilan dalam tahun (ex: 10): ","yellow")))
            print(colored("===========================================================================================================","green"))
            SisaKerja = int(input(colored("Masukkan sisa masa kerja Anda (tahun): ","yellow")))
            print(colored("===========================================================================================================","green"))

            if SisaKerja < Tenor :
                print(colored("===========================================================================================================","green"))
                print(colored("Anda","red"),colored("TIDAK","red",attrs=['bold']),colored("disarankan untuk mengambil tenor dengan jangka waktu tersebut.","red")) 
                print(colored("Kami sarankan untuk mengambil tenor dengan jangka waktu di bawah atau setara dengan","red"), colored(SisaKerja,"red"), colored("tahun","red"))

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
                print(colored("===========================================================================================================","green"))
                print(colored("Total Angsuran Bunga Fix yang dibayarkan: ","yellow"),colored(TotalAngsuranBungaFix,"green"))
                print(colored("===========================================================================================================","green"))
                print(colored("Total Angsuran Bunga Floating yang dibayarkan: ","yellow"),colored( TotalAngsuranBungaFloating,"green"))
                print(colored("===========================================================================================================","green"))
                print(colored("Total Angsuran Bunga yang dibayarkan: ","yellow"),colored (TotalAngsuranBunga,"green"))
                print(colored("===========================================================================================================","green"))
                print(colored("Sehingga total KPR yang diambil sebesar: ","yellow"),colored( TotalKPR,"green"))
                print(colored("===========================================================================================================","green"))
                print(colored("Minimal gaji yang direkomdasikan untuk mengambil KPR tersebut sebesar: ","yellow"),colored(MinimalGaji,"green"))
                print(colored("===========================================================================================================","green"))

                # Menampilkan Tabel Angsuran Setiap Bulan
                print(colored("----------------------------------------------------------------------------------------------------------------------------------------------------------------","yellow"))
                print("Bulan\t\tAngsuran Pokok\t\tAngsuran Bunga Fix\t\tAngsuran Bunga Floating\t\t\t\tTotal Angsuran per Bulan")
                print(colored("----------------------------------------------------------------------------------------------------------------------------------------------------------------","yellow"))
                for bulan in range(1, Konversi + 1):
                    if bulan <= 60:
                        print(f"{bulan}\t\t{AngsuranPokok:.2f}\t\t{AngsuranBungaFix:.2f}\t\t\t\t\t0.00\t\t\t\t\t\t{AngsuranperBulan5Tahun:.2f}")
                        break
                    else:
                        print(f"{bulan}\t\t{AngsuranPokok:.2f}\t\t0.00\t\t\t\t\t{AngsuranBungaFloating:.2f}\t\t\t\t\t\t{AngsuranperBulanSisaBulan:.2f}")
                        break

                # Data untuk Diagram Garis
                bulan = list(range(1, Konversi + 1))  # Progres bulan
                y = []
                for i in range(1, Konversi + 1):
                    if i <= 60:
                        y.append(AngsuranperBulan5Tahun)
                        break
                    else:
                        y.append(AngsuranperBulanSisaBulan)
                        break

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
                print(colored("===========================================================================================================","green"))  
                print(colored("Total Angsuran Bunga Fix yang dibayarkan: ","yellow"),colored(TotalAngsuranBungaFix,"green"))
                print(colored("===========================================================================================================","green"))  
                print(colored("Total Angsuran Bunga Floating yang dibayarkan: ","yellow"),colored( TotalAngsuranBungaFloating,"green"))
                print(colored("===========================================================================================================","green"))  
                print(colored("Total Angsuran Bunga yang dibayarkan: ","yellow"),colored (TotalAngsuranBunga,"green"))
                print(colored("===========================================================================================================","green"))  
                print(colored("Sehingga total KPR yang diambil sebesar: ","yellow"),colored( TotalKPR,"green"))
                print(colored("===========================================================================================================","green"))  
                print(colored("Minimal gaji yang direkomdasikan untuk mengambil KPR tersebut sebesar: ","yellow"),colored(MinimalGaji,"green"))
                print(colored("===========================================================================================================","green"))  
                print(colored("===========================================================================================================","green"))  

                # Menampilkan Tabel Angsuran Setiap Bulan
                print(colored("----------------------------------------------------------------------------------------------------------------------------------------------------------------","yellow"))
                print("Bulan\t\tAngsuran Pokok\t\tAngsuran Bunga Fix\t\tAngsuran Bunga Floating\t\t\t\tTotal Angsuran per Bulan")
                print(colored("----------------------------------------------------------------------------------------------------------------------------------------------------------------","yellow"))
                for bulan in range(1, Konversi + 1):
                    if bulan <= 60:
                        print(f"{bulan}\t\t{AngsuranPokok:.2f}\t\t{AngsuranBungaFix:.2f}\t\t\t\t\t0.00\t\t\t\t\t\t{AngsuranperBulan5Tahun:.2f}")
                    else:
                        print(f"{bulan}\t\t{AngsuranPokok:.2f}\t\t0.00\t\t\t\t\t{AngsuranBungaFloating:.2f}\t\t\t\t\t\t{AngsuranperBulanSisaBulan:.2f}")

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
            print(colored("===========================================================================================================","green"))
            GajiBulanan = int(input(colored("Masukkan gaji bulanan Anda: ","yellow")))
            print(colored("===========================================================================================================","green"))
            Tenor = int(input(colored("Masukkan lama KPR yang ingin Anda ambil(dalam tahun): ","yellow")))
            print(colored("===========================================================================================================","green"))
            SisaKerja = int(input(colored("Masukkan sisa masa kerja Anda (tahun):","yellow")))
            print(colored("===========================================================================================================","green"))

            if SisaKerja < Tenor :
                print(colored("===========================================================================================================","green"))
                print(colored("Anda","red"),colored("TIDAK","red",attrs=['bold']),colored("disarankan untuk mengambil tenor dengan jangka waktu tersebut.","red")) 
                print(colored("Kami sarankan untuk mengambil tenor dengan jangka waktu di bawah atau setara dengan","red"), colored(SisaKerja,"red"), colored("tahun","red"))
                
                Konversi = SisaKerja * 12
                SisaBulan = Konversi - 60

                def BungaFix (Konversi):
                    if Konversi <= 60:
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
                print(colored("===========================================================================================================","green"))
                print(colored("Saran harga rumah yang dapat diambil sebesar: ","yellow"), colored(SaranHargaRumah,"green"))
                print(colored("===========================================================================================================","green"))
                print(colored("Total Angsuran Pokok yang dibayarkan sebesar saran harga rumah", "yellow"))
                print(colored("===========================================================================================================","green"))
                print(colored("Total Angsuran Bunga Fix yang dibayarkan: ","yellow"),colored(TotalAngsuranBungaFix,"green"))
                print(colored("===========================================================================================================","green"))
                print(colored("Total Angsuran Bunga Floating yang dibayarkan: ","yellow"),colored( TotalAngsuranBungaFloating,"green"))
                print(colored("===========================================================================================================","green"))
                print(colored("Total Angsuran Bunga yang dibayarkan: ","yellow"),colored (TotalAngsuranBunga,"green"))
                print(colored("===========================================================================================================","green"))
                print(colored("===========================================================================================================","green"))

                # Menampilkan Tabel Angsuran Setiap Bulan
                print(colored("----------------------------------------------------------------------------------------------------------------------------------------------------------------","yellow"))
                print("Bulan\t\tAngsuran Pokok\t\tAngsuran Bunga Fix\t\tAngsuran Bunga Floating\t\t\t\tTotal Angsuran per Bulan")
                print(colored("----------------------------------------------------------------------------------------------------------------------------------------------------------------","yellow"))
                for bulan in range(1, Konversi + 1):
                    if bulan <= 60:
                        print(f"{bulan}\t\t{AngsuranPokok:.2f}\t\t{AngsuranBungaFix:.2f}\t\t\t\t\t0.00\t\t\t\t\t\t{AngsuranperBulan5Tahun:.2f}")
                        break
                    else:
                        print(f"{bulan}\t\t{AngsuranPokok:.2f}\t\t0.00\t\t\t\t\t{AngsuranBungaFloating:.2f}\t\t\t\t\t\t{AngsuranperBulanSisaBulan:.2f}")
                        break

                # Data untuk Diagram Garis
                bulan = list(range(1, Konversi + 1))  # Progres bulan
                y = []
                for i in range(1, Konversi + 1):
                    if i <= 60:
                        y.append(AngsuranperBulan5Tahun)
                        break
                    else:
                        y.append(AngsuranperBulanSisaBulan)
                        break

                # Membuat Diagram Garis
                plt.plot(bulan, y, marker='o', linestyle='-', color='b')

                # Menampilkan judul dan label sumbu
                plt.title('Progres Bulan vs Total Angsuran per Bulan')
                plt.xlabel('Bulan')
                plt.ylabel('Total Angsuran per Bulan')

                # Menampilkan Diagram Garis
                plt.show()

                # Memuat dan Menampilkan Gambar
                if SaranHargaRumah <= 150000000:
                    image = Image.open('TipeA.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 150000001 <= SaranHargaRumah <= 300000000:
                    image = Image.open('TipeB.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 300000001 <= SaranHargaRumah <= 450000000:
                    image = Image.open('TipeC.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 450000001 <= SaranHargaRumah <= 600000000:
                    image = Image.open('TipeD.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 600000001 <= SaranHargaRumah <= 850000000:
                    image = Image.open('TipeE.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 850000001 <= SaranHargaRumah <= 1300000000:
                    image = Image.open('TipeF.jpg')
                    # Tampilkan gambar dalam pop-up
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 1300000001 <= SaranHargaRumah <= 1550000000:
                    image = Image.open('TipeG.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 1550000001 <= SaranHargaRumah <= 1800000000:
                    image = Image.open('TipeH.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 1800000001 <= SaranHargaRumah <= 2050000000:
                    image = Image.open('TipeI.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 2050000001 <= SaranHargaRumah <= 2550000000:
                    image = Image.open('TipeJ.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 2550000001 <= SaranHargaRumah <= 3050000000:
                    image = Image.open('TipeK.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 3050000001 <= SaranHargaRumah <= 3550000000:
                    image = Image.open('TipeL.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 3550000001 <= SaranHargaRumah <= 4050000000:
                    image = Image.open('TipeM.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 4050000001 <= SaranHargaRumah <= 4550000000:
                    image = Image.open('TipeN.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 4550000001 <= SaranHargaRumah <= 5050000000:
                    image = Image.open('TipeO.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 5050000001 <= SaranHargaRumah <= 6050000000:
                    image = Image.open('TipeP.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 6050000001 <= SaranHargaRumah <= 7050000000:
                    image = Image.open('TipeQ.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 7050000001 <= SaranHargaRumah <= 8050000000:
                    image = Image.open('TipeR.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 8050000001 <= SaranHargaRumah <= 9050000000:
                    image = Image.open('TipeS.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 9050000001 <= SaranHargaRumah <= 10050000000:
                    image = Image.open('TipeT.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 10050000001 <= SaranHargaRumah <= 15050000000:
                    image = Image.open('TipeU.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 15050000001 <= SaranHargaRumah <= 20050000000:
                    image = Image.open('TipeV.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 20050000001 <= SaranHargaRumah <= 25050000000:
                    image = Image.open('TipeW.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 25050000001 <= SaranHargaRumah <= 30050000000:
                    image = Image.open('TipeX.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 30050000001 <= SaranHargaRumah <= 35050000000: 
                    image = Image.open('TipeY.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 35050000001 <= SaranHargaRumah <= 40050000000: 
                    image = Image.open('TipeZ.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                else:
                    image = Image.open('TipeAA.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break

            else:
                Konversi = Tenor * 12
                SisaBulan = Konversi - 60

                def BungaFix (Konversi):
                    if Konversi <= 60:
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
                print(colored("===========================================================================================================","green"))
                print("Saran harga rumah yang dapat diambil sebesar: ", SaranHargaRumah)
                print("Total Angsuran Pokok yang dibayarkan sebesar saran harga rumah")
                print(colored("===========================================================================================================","green"))
                print(colored("Total Angsuran Bunga Fix yang dibayarkan: ","yellow"),colored(TotalAngsuranBungaFix,"green"))
                print(colored("===========================================================================================================","green"))
                print(colored("Total Angsuran Bunga Floating yang dibayarkan: ","yellow"),colored( TotalAngsuranBungaFloating,"green"))
                print(colored("===========================================================================================================","green"))
                print(colored("Total Angsuran Bunga yang dibayarkan: ","yellow"),colored (TotalAngsuranBunga,"green"))
                print(colored("===========================================================================================================","green"))

                # Menampilkan Tabel Angsuran Setiap Bulan
                print(colored("----------------------------------------------------------------------------------------------------------------------------------------------------------------","yellow"))
                print("Bulan\t\tAngsuran Pokok\t\tAngsuran Bunga Fix\t\tAngsuran Bunga Floating\t\t\t\tTotal Angsuran per Bulan")
                print(colored("----------------------------------------------------------------------------------------------------------------------------------------------------------------","yellow"))
                for bulan in range(1, Konversi + 1):
                    if bulan <= 60:
                        print(f"{bulan}\t\t{AngsuranPokok:.2f}\t\t{AngsuranBungaFix:.2f}\t\t\t\t\t0.00\t\t\t\t\t\t{AngsuranperBulan5Tahun:.2f}")
                    else:
                        print(f"{bulan}\t\t{AngsuranPokok:.2f}\t\t0.00\t\t\t\t\t{AngsuranBungaFloating:.2f}\t\t\t\t\t\t{AngsuranperBulanSisaBulan:.2f}")

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

                # Memuat dan Menampilkan Gambar
                if SaranHargaRumah <= 150000000:
                    image = Image.open('TipeA.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 150000001 <= SaranHargaRumah <= 300000000:
                    image = Image.open('TipeB.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 300000001 <= SaranHargaRumah <= 450000000:
                    image = Image.open('TipeC.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 450000001 <= SaranHargaRumah <= 600000000:
                    image = Image.open('TipeD.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 600000001 <= SaranHargaRumah <= 850000000:
                    image = Image.open('TipeE.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 850000001 <= SaranHargaRumah <= 1300000000:
                    image = Image.open('TipeF.jpg')
                    # Tampilkan gambar dalam pop-up
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 1300000001 <= SaranHargaRumah <= 1550000000:
                    image = Image.open('TipeG.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 1550000001 <= SaranHargaRumah <= 1800000000:
                    image = Image.open('TipeH.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 1800000001 <= SaranHargaRumah <= 2050000000:
                    image = Image.open('TipeI.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 2050000001 <= SaranHargaRumah <= 2550000000:
                    image = Image.open('TipeJ.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 2550000001 <= SaranHargaRumah <= 3050000000:
                    image = Image.open('TipeK.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 3050000001 <= SaranHargaRumah <= 3550000000:
                    image = Image.open('TipeL.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 3550000001 <= SaranHargaRumah <= 4050000000:
                    image = Image.open('TipeM.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 4050000001 <= SaranHargaRumah <= 4550000000:
                    image = Image.open('TipeN.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 4550000001 <= SaranHargaRumah <= 5050000000:
                    image = Image.open('TipeO.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 5050000001 <= SaranHargaRumah <= 6050000000:
                    image = Image.open('TipeP.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 6050000001 <= SaranHargaRumah <= 7050000000:
                    image = Image.open('TipeQ.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 7050000001 <= SaranHargaRumah <= 8050000000:
                    image = Image.open('TipeR.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 8050000001 <= SaranHargaRumah <= 9050000000:
                    image = Image.open('TipeS.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 9050000001 <= SaranHargaRumah <= 10050000000:
                    image = Image.open('TipeT.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 10050000001 <= SaranHargaRumah <= 15050000000:
                    image = Image.open('TipeU.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                elif 15050000001 <= SaranHargaRumah <= 20050000000:
                    image = Image.open('TipeV.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 20050000001 <= SaranHargaRumah <= 25050000000:
                    image = Image.open('TipeW.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 25050000001 <= SaranHargaRumah <= 30050000000:
                    image = Image.open('TipeX.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 30050000001 <= SaranHargaRumah <= 35050000000: 
                    image = Image.open('TipeY.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                elif 35050000001 <= SaranHargaRumah <= 40050000000: 
                    image = Image.open('TipeZ.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                else:
                    image = Image.open('TipeAA.jpg')
                    plt.imshow(image)
                    plt.axis('off')
                    plt.show()
                    break
                
        else: 
            print(colored("Menu tidak valid. Silakan pilih menu yang sesuai.","yellow"))
