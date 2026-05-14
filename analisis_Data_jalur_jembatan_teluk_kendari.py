import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate

#Inputkan semua data-data yang ada
data = {
    "Bulan": ["Januari", "Februari", "Maret", "April", "Mei", "Juni", 
             "Juli", "Agustus", "September", "Oktober", "November", "Desember"],
    "Motor": [6000, 5800, 6200, 6100, 6300, 6400, 6500, 6600, 6700, 6800, 7000, 7500],
    "Mobil": [4000, 3800, 4100, 3900, 4200, 4300, 4400, 4500, 4600, 4700, 4800, 5000],
    "Truk": [1500, 1400, 1600, 1550, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2500]
}

df = pd.DataFrame(data)
df["Total"] = df[["Motor", "Mobil", "Truk"]].sum(axis=1)

print("1. Data Lalu Lintas per Bulan:")
print(tabulate(df, headers='keys', tablefmt='pretty', showindex=False))

# menghitung dan menentukan jumlah motor,mobil, dan truk
bulan_terpadat = df.loc[df["Total"].idxmax(), "Bulan"]

total_kendaraan = df[["Motor", "Mobil", "Truk"]].sum()
kategori_terbanyak = total_kendaraan.idxmax()
rata_rata = df["Total"].mean()

print("\n2. Bulan dengan lalu lintas terpadat:", bulan_terpadat)
print(f"3. Kategori terbanyak: {kategori_terbanyak} ({total_kendaraan[kategori_terbanyak]} unit)")
print(f"4. Rata-rata kendaraan per bulan: {rata_rata:.0f} unit")
sns.set_theme(style="whitegrid", palette="pastel")

# buat tampilan grafik
plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 1)
sns.lineplot(
    data=df,
    x="Bulan",
    y="Total",
    marker="o",
    linewidth=2.5,
    color="green"
)
plt.title("Trend Lalu Lintas Tahunan", fontsize=14, pad=20)
plt.xlabel("Bulan", fontsize=12)
plt.ylabel("Total Kendaraan", fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.subplot(1, 2, 2)
sns.barplot(
    x=total_kendaraan.index,
    y=total_kendaraan.values,
    palette=["#ff9999", "#66b3ff", "#99ff99"]
)
plt.title("Total Kendaraan per Kategori (1 Tahun)", fontsize=14, pad=20)
plt.xlabel("Jenis Kendaraan", fontsize=12)
plt.ylabel("Total", fontsize=12)
plt.bar_label(plt.gca().containers[0], fmt="77.900", padding=3)
plt.bar_label(plt.gca().containers[1], fmt="52.300", padding=3)
plt.bar_label(plt.gca().containers[2], fmt="22.550", padding=3)
plt.tight_layout()
plt.show()
