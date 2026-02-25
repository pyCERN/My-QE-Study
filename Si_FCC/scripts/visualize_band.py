import numpy as np
import matplotlib.pyplot as plt

file_path = '../si_bands.dat.gnu'
data = np.loadtxt(file_path)

k_path, energy = data[:, 0], data[:, 1]

# Valence band maximum (highest occupied level)
vbm = 6.4408

# Conduction band minimum
cbm = min(energy[energy > vbm])

print(f"Band gap = {cbm - vbm}eV")

plt.figure(figsize=(8, 6))
# plt.scatter(k_path, energy - vbm, s=1, color="blue", label="Bands")
plt.scatter(k_path, energy, s=1, color="blue", label="Bands")

# plt.axhline(0, color="red", linestyle="--", linewidth=1, label="Fermi level (VBM)")
plt.axhline(vbm, color="red", linestyle="--", linewidth=1, label="Fermi level (VBM)")
plt.title("Silicon band structure", fontsize=14)
plt.xlabel("K-path (L - $\Gamma$ - X - U, K - $\Gamma$)", fontsize=12)
# plt.ylabel("Energy (E - $E_{VBM}$) [eV]", fontsize=12)
plt.ylabel("Energy [eV]", fontsize=12)
plt.grid(True, alpha=0.3)
# plt.show()
plt.savefig("silicon_band.png", dpi=300)