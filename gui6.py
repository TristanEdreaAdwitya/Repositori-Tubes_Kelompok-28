import csv
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Fungsi untuk menghitung dan menyimpan hasil KPR dalam format CSV
def hitung_dan_simpan():
    try:
        HargaRumah = int(entry_harga_rumah.get())
        PersenDP = int(entry_persen_DP.get())
        LamaCicilan = int(entry_lama_cicilan.get())

        NominalDP = PersenDP * HargaRumah / 100
        Konversi = LamaCicilan * 12
        TotalPinjaman = HargaRumah - NominalDP

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

        angsuran_pokok = TotalPinjaman / Konversi
        angsuran_bunga_fix_perbulan = TotalPinjaman * bunga_fix / 12
        angsuran_per_bulan_menggunakan_bunga_fix = angsuran_pokok + angsuran_bunga_fix_perbulan

        if Konversi > 60:
            bunga_floating = 0.10
        else:
            bunga_floating = 0

        SisaBulan = Konversi - 60
        totalKPR5Tahun = angsuran_per_bulan_menggunakan_bunga_fix * 60
        angsuran_bunga_floating_perbulan = TotalPinjaman * bunga_floating / 12
        angsuran_per_bulan_menggunakan_bunga_floating = (TotalPinjaman - totalKPR5Tahun) / SisaBulan + angsuran_bunga_floating_perbulan

        total_KPR = (angsuran_per_bulan_menggunakan_bunga_fix + angsuran_per_bulan_menggunakan_bunga_floating) * Konversi
        minimal_gaji = total_KPR / (Konversi * 0.3)

        # Menyimpan hasil KPR dalam file CSV
        with open('hasil_kpr.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Bulan", "Angsuran Pokok", "Angsuran Bunga Fix", "Angsuran Per Bulan Menggunakan Bunga Fix"])
            for bulan in range(1, Konversi + 1):
                writer.writerow(
                    [bulan, round(angsuran_pokok, 2), round(angsuran_bunga_fix_perbulan, 2),
                     round(angsuran_per_bulan_menggunakan_bunga_fix, 2)])

        messagebox.showinfo("Info", "Hasil KPR telah disimpan dalam file hasil_kpr.csv")

        # Membaca file CSV dan menampilkan hasil KPR dalam tabel (Treeview)
        with open('hasil_kpr.csv', 'r') as file:
            reader = csv.reader(file)
            data = list(reader)

        # Membuat jendela Tabel
        window_table = Toplevel()
        window_table.title("Hasil KPR")

        # Menambahkan keterangan di atas tabel
        keterangan_label = Label(window_table, text="Total KPR: Rp%.2f   |   Gaji yang Dibutuhkan: Rp%.2f   |   Total Cicilan Pokok: Rp%.2f   |   Total Bunga: Rp%.2f"
                                               % (total_KPR, minimal_gaji, totalKPR5Tahun, total_KPR - TotalPinjaman))
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

# Label dan Entry untuk input persentase DP
label_persen_DP = Label(window, text="%DP: ")
entry_persen_DP = Entry(window)

# Label dan Entry untuk input lama cicilan
label_lama_cicilan = Label(window, text="Lama Cicilan (tahun): ")
entry_lama_cicilan = Entry(window)

# Tombol untuk menghitung dan menyimpan hasil KPR
button_hitung = Button(window, text="Hitung KPR", command=hitung_dan_simpan)

# Menempatkan elemen-elemen GUI ke dalam grid
label_harga_rumah.grid(row=1, column=0, padx=10, pady=5, sticky=W)
entry_harga_rumah.grid(row=1, column=1, padx=10, pady=5, sticky=E)
label_persen_DP.grid(row=2, column=0, padx=10, pady=5, sticky=W)
entry_persen_DP.grid(row=2, column=1, padx=10, pady=5, sticky=E)
label_lama_cicilan.grid(row=3, column=0, padx=10, pady=5, sticky=W)
entry_lama_cicilan.grid(row=3, column=1, padx=10, pady=5, sticky=E)
button_hitung.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Menampilkan jendela GUI
window.mainloop()
