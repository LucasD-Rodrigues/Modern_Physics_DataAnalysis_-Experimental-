import numpy as np
import matplotlib.pyplot as plt
from photoelectric_effect import peak_wavelengths
from matplotlib import rcParams

rcParams['font.family'] = 'serif'
rcParams['font.size'] = 12
rcParams['axes.labelsize'] = 12

c = 3 * 10**8 #(m/s)
e = 1.602 * 10**-19 #(C)

V = np.array([0.286, 0.309, 0.368, 0.524, 1.013, 1.043, 1.137, 1.192, 1.238, 1.306])
V = np.array([0.263, 0.373, 0.484, 0.704, 0.855, 0.870, 1.028, 1.070, 1.137, 1.192])

peak_frequencies = np.array(sorted(c / peak_wavelengths))

print(peak_frequencies)
print(V)

adjust = np.polyfit(peak_frequencies, V, 1)
print(f"Planck constant: {adjust[0] * e} J·s")

plt.scatter(peak_frequencies, V)
plt.plot(peak_frequencies, adjust[0] * peak_frequencies + adjust[1], color="black", linestyle="dashed", label = r"$h \approx 6.2 \times 10^{-34}$")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Tensão de parada (V)")
plt.legend()
plt.title("Ajuste linear do comportamento da tensão")
plt.show()


