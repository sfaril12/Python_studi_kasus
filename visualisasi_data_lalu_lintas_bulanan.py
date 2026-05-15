import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# =====================
# DATA PREPARATION (Menggunakan NumPy)
# =====================
data = {
    "Bulan": ["Januari", "Februari", "Maret", "April", "Mei", "Juni", 
             "Juli", "Agustus", "September", "Oktober", "November", "Desember"],
    "Motor": np.array([6000, 5800, 6200, 6100, 6300, 6400, 6500, 6600, 6700, 6800, 7000, 7500]),
    "Mobil": np.array([4000, 3800, 4100, 3900, 4200, 4300, 4400, 4500, 4600, 4700, 4800, 5000]),
    "Truk": np.array([1500, 1400, 1600, 1550, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2500])
}

df = pd.DataFrame(data)
df["Total"] = np.add(np.add(df["Motor"], df["Mobil"]), df["Truk"])  # Penjumlahan dengan NumPy

# =====================
# ANALISIS DENGAN NUMPY
# =====================
# 1. Tampilkan data
print("1. Data Lalu Lintas per Bulan:")
print(df.to_string(index=False, justify='center'))

# 2. Cari bulan tersibuk menggunakan NumPy
index_max = np.argmax(df["Total"].values)
bulan_terpadat = df["Bulan"].iloc[index_max]

# 3. Hitung total kendaraan per kategori dengan NumPy
total_motor = np.sum(df["Motor"].values)
total_mobil = np.sum(df["Mobil"].values)
total_truk = np.sum(df["Truk"].values)

# 4. Hitung rata-rata dengan NumPy
rata_rata = np.mean(df["Total"].values)

# =====================
# VISUALISASI DENGAN MATPLOTLIB
# =====================
plt.figure(figsize=(15, 6))

# Plot 1: Trend Tahunan
plt.subplot(1, 2, 1)
plt.plot(df["Bulan"], df["Total"], marker='o', linestyle='-', color='b', linewidth=2,markersize=8)
plt.title("Trend Lalu Lintas Tahunan", fontsize=14)
plt.xlabel("Bulan", fontsize=12)
plt.ylabel("Total Kendaraan", fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, linestyle=':', alpha=0.7)

# Plot 2: Distribusi Kendaraan
plt.subplot(1, 2, 2)
kategori = ["Motor", "Mobil", "Truk"]
total = [total_motor, total_mobil, total_truk]
colors = ['#3498db', '#e74c3c', '#9b59b6']

bars = plt.bar(kategori, total, color=colors, edgecolor='black')

# Tambahkan label angka di atas bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:,}',
             ha='center', 
             va='bottom',
             fontsize=12)

plt.title("Distribusi Jenis Kendaraan", fontsize=14)
plt.xlabel("Kategori", fontsize=12)
plt.ylabel("Total", fontsize=12)

plt.tight_layout()
plt.show()

# =====================
# HASIL ANALISIS
# =====================
print("\n2. Bulan tersibuk:", bulan_terpadat)
print(f"3. Kategori terbanyak: Motor ({total_motor:,} unit)" if total_motor > total_mobil and total_motor > total_truk else 
      f"Mobil ({total_mobil:,} unit)" if total_mobil > total_truk else 
      f"Truk ({total_truk:,} unit)")
print(f"4. Rata-rata kendaraan per bulan: {rata_rata:,.0f} unit")