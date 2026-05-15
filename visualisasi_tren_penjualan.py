# Import library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. MEMBUAT KETERANGAN GRAFIK
data = {
    'Bulan': ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni',
             'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'],
    'Penjualan (juta)': [120, 85, 150, 95, 200, 75, 180, 90, 130, 110, 160, 220],
    'Keuntungan (juta)': [30, 20, 35, 25, 40, 15, 45, 18, 32, 28, 38, 50]
}
df = pd.DataFrame(data)

# 2. ANALISIS DATA
# Mencari penjualan tertinggi menggunakan Pandas
max_penjualan = df[df['Penjualan (juta)'] == df['Penjualan (juta)'].max()]
min_penjualan = df[df['Penjualan (juta)'] == df['Penjualan (juta)'].min()]

# Menghitung rata-rata keuntungan menggunakan NumPy
rata_keuntungan = np.mean(df['Keuntungan (juta)'])

# 3. VISUALISASI DATA
plt.figure(figsize=(12, 6))

# Plot Penjualan
plt.subplot(1, 2, 1)
plt.bar(df['Bulan'], df['Penjualan (juta)'], color='skyblue')
plt.plot(max_penjualan['Bulan'], max_penjualan['Penjualan (juta)'], 'ro', label='Tertinggi')
plt.plot(min_penjualan['Bulan'], min_penjualan['Penjualan (juta)'], 'go', label='Terendah')
plt.title('Penjualan per Bulan')
plt.xticks(rotation=90)
plt.legend()

# Plot Keuntungan
plt.subplot(1, 2, 2)
plt.plot(df['Bulan'], df['Keuntungan (juta)'], 'm-', marker='o')
plt.title('Keuntungan per Bulan')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# 4. HASIL ANALISIS
print(f"\nHasil Analisis:")
print("========================================")
print(f"Penjualan Tertinggi: {max_penjualan['Penjualan (juta)'].values[0]} juta (Bulan {max_penjualan['Bulan'].values[0]})")
print(f"Penjualan Terendah : {min_penjualan['Penjualan (juta)'].values[0]} juta (Bulan {min_penjualan['Bulan'].values[0]})")
print(f"Rata-rata Keuntungan Tahunan: {rata_keuntungan:.2f} juta per bulan")
print("========================================\n")