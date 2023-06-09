import matplotlib.pyplot as plt

# Data yang akan digunakan
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Membuat grafik
plt.plot(x, y)

# Menambahkan label pada sumbu x dan y
plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')

# Menambahkan judul grafik
plt.title('Grafik Linier')

# Menampilkan grafik
plt.show()
