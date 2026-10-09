import numpy as np
import matplotlib.pyplot as plt
from photoelectric_effect import peak_wavelengths

c = 3 * 10**8 #(m/s)
e = 1.602 * 10**-19 #(C)

V = np.array([0.286, 0.309, 0.368, 0.524, 1.013, 1.043, 1.137, 1.192, 1.238, 1.306])

peak_frequencies = np.array(sorted(c / peak_wavelengths))

adjust = np.polyfit(peak_frequencies, V, 1)
print(f"Planck constant: {adjust[0] * e} J·s")

plt.scatter(peak_frequencies, V)
plt.plot(peak_frequencies, adjust[0] * peak_frequencies + adjust[1], color="red")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Tensão de parada (V)")
plt.show()


