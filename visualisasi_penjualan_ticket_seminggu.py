import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

harga_tiket = {
    'VIP': 1000000,
    'Reguler': 500000,
    'Festival': 250000
}
# Data penjualan tiket per hari
data = {
    'Hari': ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'],
    'VIP': [12, 8, 15, 10, 20, 25, 30],
    'Reguler': [25, 30, 28, 35, 40, 50, 55],
    'Festival': [40, 45, 50, 60, 55, 80, 70]
}

# Buat DataFrame
df = pd.DataFrame(data)

# Menyiapkan data untuk grafik
hari = df['Hari']
vip = df['VIP']
reguler = df['Reguler']
festival = df['Festival']

# Buat stacked bar chart
plt.figure(figsize=(10, 6))
plt.bar(hari, vip, label='VIP', color='gold')
plt.bar(hari, reguler, bottom=vip, label='Reguler', color='orange')
plt.bar(hari, festival, bottom=vip+reguler, label='Festival', color='lightgreen')

# Judul dan keterangan
plt.title('Jumlah Penjualan Tiket per Hari (Stacked)')
plt.xlabel('Hari')
plt.ylabel('Jumlah Tiket Terjual')
plt.legend(title='Kategori Tiket')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

df['Pendapatan'] = (
    df['VIP'] * harga_tiket['VIP'] +
    df['Reguler'] * harga_tiket['Reguler'] +
    df['Festival'] * harga_tiket['Festival']
)

total_pendapatan = df['Pendapatan'].sum()
hari_tertinggi = df.loc[df['Pendapatan'].idxmax(), 'Hari']
kategori_terlaris = df[['VIP', 'Reguler', 'Festival']].sum().idxmax()
jumlah_terlaris = df[kategori_terlaris].sum()

# Tampilkan hasil
print("=== Laporan Penjualan Tiket ===")
print(df[['Hari', 'VIP', 'Reguler', 'Festival', 'Pendapatan']])
print("\nTotal Pendapatan Mingguan: Rp {:,}".format(total_pendapatan))
print(f"Hari dengan Pendapatan Tertinggi: {hari_tertinggi}")
print(f"Kategori Tiket Terlaris: {kategori_terlaris} ({jumlah_terlaris} tiket)")