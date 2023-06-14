import csv
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt


# Data pengguna yang telah terdaftar
registered_users = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3"
}

# Variabel untuk menyimpan data pengguna yang berhasil log in
logged_in_user = None

# Fungsi untuk memeriksa keberadaan pengguna dalam data pengguna yang terdaftar
def is_registered(username):
    return username in registered_users

# Fungsi untuk memeriksa kecocokan username dan password pada data pengguna yang terdaftar
def is_valid_credentials(username, password):
    if is_registered(username):
        return registered_users[username] == password
    return False

# Fungsi untuk mengatur pengguna yang berhasil log in
def set_logged_in_user(username):
    global logged_in_user
    logged_in_user = username

# Fungsi untuk menghitung dan menyimpan hasil KPR dalam format CSV
def hitung_dan_simpan():
    try:
        HargaRumah = int(entry_harga_rumah.get())
        PersenDP = int(entry_persen_DP.get())
        LamaCicilan = int(entry_lama_cicilan.get())
        SisaKerja = int(entry_Sisa_Kerja.get())

        if SisaKerja < LamaCicilan :
            messagebox.showinfo("informasi", "Anda tidak disarankan untuk mengambil tenor dengan jangka waktu tersebut. Kami sarankan untuk mengambil tenor dengan jangka waktu di bawah atau setara dengan sisa kerja anda")

            NominalDP = PersenDP * HargaRumah / 100
            Konversi = SisaKerja * 12
            KPR = HargaRumah - NominalDP
            SisaBulan = Konversi - 60

            def BungaFix(Konversi) :
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
        

            angsuran_pokok = KPR / Konversi
            KPRbagitahun = KPR / SisaKerja

            Bunga_Fix = BungaFix (Konversi)
            AngsuranBungaFix = (KPRbagitahun * Bunga_Fix) / 12

            Bunga_Floating = BungaFloating (Konversi)
            AngsuranBungaFloating = (KPRbagitahun * Bunga_Floating) / 12

            TotalAngsuranPokok = angsuran_pokok * Konversi
            TotalAngsuranBungaFix = AngsuranBungaFix * 60 if Konversi > 60 else AngsuranBungaFix * Konversi
            TotalAngsuranBungaFloating = AngsuranBungaFloating * SisaBulan if Konversi > 60 else 0
            TotalAngsuranBunga = TotalAngsuranBungaFix + TotalAngsuranBungaFloating

            AngsuranperBulan5Tahun = angsuran_pokok + AngsuranBungaFix
            AngsuranperBulanSisaBulan = angsuran_pokok + AngsuranBungaFloating

            TotalKPR = TotalAngsuranPokok + TotalAngsuranBunga
            MinimalGaji = TotalKPR / (Konversi * 0.3)

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
            



            # Menyimpan hasil KPR dalam file CSV
            with open('hasil_kpr.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Bulan", "Angsuran Pokok", "Angsuran Bunga Fix", "Angsuran Per Bulan Menggunakan Bunga Fix"])
                for bulan in range(1, Konversi + 1):
                    writer.writerow(
                        [bulan, round(angsuran_pokok, 2), round(AngsuranBungaFix, 2),
                        round(AngsuranperBulan5Tahun, 2)])

            messagebox.showinfo("Info", "Hasil KPR telah disimpan dalam file hasil_kpr.csv")

            # Membaca file CSV dan menampilkan hasil KPR dalam tabel (Treeview)
            with open('hasil_kpr.csv', 'r') as file:
                reader = csv.reader(file)
                data = list(reader)

            # Membuat jendela Tabel
            window_table = Toplevel()
            window_table.title("Hasil KPR")

            # Menambahkan keterangan di atas tabel
            keterangan_label = Label(window_table, text=f"Total KPR: Rp{TotalKPR:.2f}   |   Gaji yang Dibutuhkan: Rp{MinimalGaji:.2f}   |   Total Cicilan Pokok: Rp{TotalAngsuranPokok:.2f}   |   Total Bunga: Rp{TotalAngsuranBunga:.2f}")
            keterangan_label.pack(padx=10, pady=10) 

            # Membuat Treeview
            table = ttk.Treeview(window_table)
            table['columns'] = data[0]
            table.heading("#0", text='No.')
            table.column("#0", width=50, stretch=NO)

            for col in data[0]:
                table.heading(col, text=col)
                table.column(col, width=150, stretch=YES)

            # Menambahkan data ke dalam Treeview
            for i, row in enumerate(data[1:], start=1):
                table.insert(parent='', index='end', iid=i, text=str(i), values=row)

            # Menempatkan Treeview ke dalam jendela Tabel
            table.pack(fill=BOTH, expand=YES)
        else :
            NominalDP = PersenDP * HargaRumah / 100
            Konversi = LamaCicilan * 12
            KPR = HargaRumah - NominalDP
            SisaBulan = Konversi - 60

            def BungaFix(Konversi) :
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
        

            angsuran_pokok = KPR / Konversi
            KPRbagitahun = KPR / LamaCicilan

            Bunga_Fix = BungaFix (Konversi)
            AngsuranBungaFix = (KPRbagitahun * Bunga_Fix) / 12

            Bunga_Floating = BungaFloating (Konversi)
            AngsuranBungaFloating = (KPRbagitahun * Bunga_Floating) / 12

            TotalAngsuranPokok = angsuran_pokok * Konversi
            TotalAngsuranBungaFix = AngsuranBungaFix * 60 if Konversi > 60 else AngsuranBungaFix * Konversi
            TotalAngsuranBungaFloating = AngsuranBungaFloating * SisaBulan if Konversi > 60 else 0
            TotalAngsuranBunga = TotalAngsuranBungaFix + TotalAngsuranBungaFloating

            AngsuranperBulan5Tahun = angsuran_pokok + AngsuranBungaFix
            AngsuranperBulanSisaBulan = angsuran_pokok + AngsuranBungaFloating

            TotalKPR = TotalAngsuranPokok + TotalAngsuranBunga
            MinimalGaji = TotalKPR / (Konversi * 0.3)
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




            # Menyimpan hasil KPR dalam file CSV
            with open('hasil_kpr.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Bulan", "Angsuran Pokok", "Angsuran Bunga Fix", "Angsuran Per Bulan Menggunakan Bunga Fix"])
                for bulan in range(1, Konversi + 1):
                    writer.writerow(
                        [bulan, round(angsuran_pokok, 2), round(AngsuranBungaFix, 2),
                        round(AngsuranperBulan5Tahun, 2)])

            messagebox.showinfo("Info", "Hasil KPR telah disimpan dalam file hasil_kpr.csv")

            # Membaca file CSV dan menampilkan hasil KPR dalam tabel (Treeview)
            with open('hasil_kpr.csv', 'r') as file:
                reader = csv.reader(file)
                data = list(reader)

            # Membuat jendela Tabel
            window_table = Toplevel()
            window_table.title("Hasil KPR")

            # Menambahkan keterangan di atas tabel
            keterangan_label = Label(window_table, text=f"Total KPR: Rp{TotalKPR:.2f}   |   Gaji yang Dibutuhkan: Rp{MinimalGaji:.2f}   |   Total Cicilan Pokok: Rp{TotalAngsuranPokok:.2f}   |   Total Bunga: Rp{TotalAngsuranBunga:.2f}")
            keterangan_label.pack(padx=10, pady=10) 

            # Membuat Treeview
            table = ttk.Treeview(window_table)
            table['columns'] = data[0]
            table.heading("#0", text='No.')
            table.column("#0", width=50, stretch=NO)

            for col in data[0]:
                table.heading(col, text=col)
                table.column(col, width=150, stretch=YES)

            # Menambahkan data ke dalam Treeview
            for i, row in enumerate(data[1:], start=1):
                table.insert(parent='', index='end', iid=i, text=str(i), values=row)

            # Menempatkan Treeview ke dalam jendela Tabel
            table.pack(fill=BOTH, expand=YES)

    except ValueError:
        messagebox.showerror("Error", "Mohon masukkan angka yang valid")

# Fungsi untuk menampilkan jendela log in
def show_login_window():
    login_window = Toplevel()
    login_window.title("Log In")

    label_username = Label(login_window, text="Username: ")
    entry_username = Entry(login_window)
    label_username.pack()
    entry_username.pack()

    label_password = Label(login_window, text="Password: ")
    entry_password = Entry(login_window, show="*")
    label_password.pack()
    entry_password.pack()

    button_login = Button(login_window, text="Log In", command=lambda: login(entry_username.get(), entry_password.get(), login_window))
    button_login.pack()

# Fungsi untuk menampilkan jendela sign up
def show_signup_window():
    signup_window = Toplevel()
    signup_window.title("Sign Up")

    label_username = Label(signup_window, text="Username: ")
    entry_username = Entry(signup_window)
    label_username.pack()
    entry_username.pack()

    label_password = Label(signup_window, text="Password: ")
    entry_password = Entry(signup_window, show="*")
    label_password.pack()
    entry_password.pack()

    button_signup = Button(signup_window, text="Sign Up", command=lambda: signup(entry_username.get(), entry_password.get(), signup_window))
    button_signup.pack()

# Fungsi untuk melakukan log in
def login(username, password, login_window):
    if is_valid_credentials(username, password):
        set_logged_in_user(username)
        login_window.destroy()
        messagebox.showinfo("Success", "Log in successful!")
    else:
        messagebox.showerror("Error", "Invalid username or password")

# Fungsi untuk melakukan sign up
def signup(username, password, signup_window):
    if is_registered(username):
        messagebox.showerror("Error", "Username already exists")
    else:
        registered_users[username] = password
        messagebox.showinfo("Success", "Sign up successful!")
        signup_window.destroy()

# Fungsi untuk memeriksa log in dan menghitung KPR
def check_login_and_calculate():
    if logged_in_user:
        hitung_dan_simpan()
    else:
        messagebox.showerror("Error", "Please log in first")

# Membuat jendela GUI
window = Tk()
window.title("Program Simulasi KPR")

# Menambahkan gambar header
header_image = PhotoImage(file="header.png")
header_label = Label(window, image=header_image)
header_label.grid(row=0, column=0, columnspan=2)

# Label dan Entry untuk input harga rumah
label_harga_rumah = Label(window, text="Harga Rumah: ")
entry_harga_rumah = Entry(window)

# Label dan entry untuk input sisa kerja
label_Sisa_Kerja = Label(window, text="Sisa Waktu Kerja:")
entry_Sisa_Kerja = Entry(window)

# Label dan Entry untuk input persentase DP
label_persen_DP = Label(window, text="%DP: ")
entry_persen_DP = Entry(window)

# Label dan Entry untuk input lama cicilan
label_lama_cicilan = Label(window, text="Lama Cicilan (tahun): ")
entry_lama_cicilan = Entry(window)

# Tombol untuk menghitung dan menyimpan hasil KPR
button_hitung = Button(window, text="Hitung KPR", command=check_login_and_calculate)

# Tombol untuk log in
button_login = Button(window, text="Log In", command=show_login_window)

# Tombol untuk sign up
button_signup = Button(window, text="Sign Up", command=show_signup_window)

# Menempatkan elemen-elemen GUI ke dalam grid
label_harga_rumah.grid(row=1, column=0, padx=10, pady=5, sticky=W)
entry_harga_rumah.grid(row=1, column=1, padx=10, pady=5, sticky=E)
label_persen_DP.grid(row=2, column=0, padx=10, pady=5, sticky=W)
entry_persen_DP.grid(row=2, column=1, padx=10, pady=5, sticky=E)
label_lama_cicilan.grid(row=3, column=0, padx=10, pady=5, sticky=W)
entry_lama_cicilan.grid(row=3, column=1, padx=10, pady=5, sticky=E)
label_Sisa_Kerja.grid(row=4, column=0, padx=10, pady=5, sticky=W)
entry_Sisa_Kerja.grid(row=4, column=1, padx=10, pady=5, sticky=E)
button_hitung.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
button_login.grid(row=6, column=0, padx=10, pady=5)
button_signup.grid(row=6, column=1, padx=10, pady=5)

# Menampilkan jendela GUI
window.mainloop()
