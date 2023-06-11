def hitung_bunga_fix(lama_kpr):
    if lama_kpr <= 60:
        return 0.04  # 4% bunga fix
    elif lama_kpr <= 120:
        return 0.06  # 6% bunga fix
    elif lama_kpr <= 180:
        return 0.08  # 8% bunga fix
    elif lama_kpr <= 240:
        return 0.1  # 10% bunga fix
    else:
        return 0.11  # 11% bunga fix


def hitung_kpr(gaji_bulanan, lama_kpr):
    maksimal_cicilan = gaji_bulanan * 0.3
    cicilan_pokok = maksimal_cicilan * 0.7  # 30% gaji bulanan dikurangi bunga fix

    bunga_fix = hitung_bunga_fix(lama_kpr)
    cicilan_bunga_fix = maksimal_cicilan * bunga_fix
    cicilan_bunga_floating = maksimal_cicilan * 0.1  # 10% bunga floating setelah 5 tahun

    saran_maksimal_kpr = cicilan_pokok * lama_kpr

    total_cicilan_pokok = cicilan_pokok * lama_kpr
    total_cicilan_bunga_fix = cicilan_bunga_fix * 60 if lama_kpr > 60 else cicilan_bunga_fix * lama_kpr
    total_cicilan_bunga_floating = cicilan_bunga_floating * (lama_kpr - 60) if lama_kpr > 60 else 0
    total_cicilan_bunga = total_cicilan_bunga_fix + total_cicilan_bunga_floating

    return cicilan_pokok, cicilan_bunga_fix, cicilan_bunga_floating, saran_maksimal_kpr, \
           total_cicilan_pokok, total_cicilan_bunga_fix, total_cicilan_bunga_floating, total_cicilan_bunga


gaji_bulanan = float(input("Masukkan gaji bulanan Anda: "))
lama_kpr = int(input("Masukkan lama KPR (dalam bulan): "))

cicilan_pokok, cicilan_bunga_fix, cicilan_bunga_floating, saran_maksimal_kpr, \
total_cicilan_pokok, total_cicilan_bunga_fix, total_cicilan_bunga_floating, total_cicilan_bunga = \
    hitung_kpr(gaji_bulanan, lama_kpr)

print("Cicilan Pokok/Bulan:", cicilan_pokok)
print("Cicilan Bunga Fix/Bulan:", cicilan_bunga_fix)
print("Cicilan Bunga Floating/Bulan:", cicilan_bunga_floating)
print("Saran Maksimal KPR yang Bisa Diambil:", saran_maksimal_kpr)
print("Total Angsuran Menggunakan Bunga Fix/Bulan:", total_cicilan_bunga_fix)
print("Total Angsuran Menggunakan Bunga Floating/Bulan:", total_cicilan_bunga_floating)
print("Total Cicilan Pokok yang Dibayarkan:", total_cicilan_pokok)
print("Total Cicilan Bunga Fix yang Dibayarkan:", total_cicilan_bunga_fix)
print("Total Cicilan Bunga Floating yang Dibayarkan:", total_cicilan_bunga_floating)
print("Total Cicilan Bunga yang Dibayarkan:", total_cicilan_bunga)
