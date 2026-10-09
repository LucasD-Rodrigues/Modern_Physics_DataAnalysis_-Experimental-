import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

spectrum1 = pd.read_csv("Spectral Data/espectro-azul.csv")
spectrum2 = pd.read_csv("Spectral Data/espectro-azul2.csv")
spectrum3 = pd.read_csv("Spectral Data/espectro-verde.csv")
spectrum4 = pd.read_csv("Spectral Data/espectro-verde2.csv")
spectrum5 = pd.read_csv("Spectral Data/espectro-verde3.csv")

data1 = pd.DataFrame(spectrum1)

wavelenght1 = data1['wavelength']
spectrum1 = data1['spectral data']

plt.plot(wavelenght1, spectrum1)
plt.xlabel("Comprimento de onda")
plt.ylabel("Intensidade (U.A)")
plt.title("Espectro azul 1")
plt.show()
