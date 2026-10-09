import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.family'] = 'serif'
rcParams['font.size'] = 12
rcParams['axes.labelsize'] = 12

spectrum1 = pd.read_csv("Spectral Data/espectro-azul.csv")
spectrum2 = pd.read_csv("Spectral Data/espectro-azul2.csv")
spectrum3 = pd.read_csv("Spectral Data/espectro-verde.csv")
spectrum4 = pd.read_csv("Spectral Data/espectro-verde2.csv")
spectrum5 = pd.read_csv("Spectral Data/espectro-verde3.csv")
spectrum6 = pd.read_csv("Spectral Data/espectro-vermelho.csv")
spectrum7 = pd.read_csv("Spectral Data/espectro-vermelho2.csv")
spectrum8 = pd.read_csv("Spectral Data/espectro-violeta.csv")
spectrum9 = pd.read_csv("Spectral Data/espectro-violeta2.csv")
spectrum10 = pd.read_csv("Spectral Data/espectro-amarelo.csv")

data1 = pd.DataFrame(spectrum1)
data2 = pd.DataFrame(spectrum2)
data3 = pd.DataFrame(spectrum3)
data4 = pd.DataFrame(spectrum4)
data5 = pd.DataFrame(spectrum5)
data6 = pd.DataFrame(spectrum6)
data7 = pd.DataFrame(spectrum7)
data8 = pd.DataFrame(spectrum8)
data9 = pd.DataFrame(spectrum9)
data10 = pd.DataFrame(spectrum10)

wavelenght1 = data1['wavelength']
spectrum1 = data1['spectral data']
wavelenght2 = data2['wavelength']
spectrum2 = data2['spectral data']
wavelenght3 = data3['wavelength']
spectrum3 = data3['spectral data']
wavelenght4 = data4['wavelength']
spectrum4 = data4['spectral data']
wavelenght5 = data5['wavelength']
spectrum5 = data5['spectral data']
wavelenght6 = data6['wavelength']
spectrum6 = data6['spectral data']
wavelenght7 = data7['wavelength']
spectrum7 = data7['spectral data']
wavelenght8 = data8['wavelength']
spectrum8 = data8['spectral data']
wavelenght9 = data9['wavelength']
spectrum9 = data9['spectral data']
wavelenght10 = data10['wavelength']
spectrum10 = data10['spectral data']

wavelenghts = [wavelenght1, wavelenght2, wavelenght3, wavelenght4, wavelenght5, wavelenght6, wavelenght7, wavelenght8, wavelenght9, wavelenght10]

spectra = [spectrum1, spectrum2, spectrum3, spectrum4, spectrum5, spectrum6, spectrum7, spectrum8, spectrum9, spectrum10]

peak_wavelengths = []
for i in range(len(spectra)):
    peak_wavelength = wavelenghts[i][spectra[i].idxmax()]
    peak_wavelengths.append(peak_wavelength)

peak_wavelengths = np.array(sorted(peak_wavelengths))*1e-9
print(peak_wavelengths)

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(wavelenght1, spectrum1)
plt.plot(wavelenght2, spectrum2, color="lightblue")
plt.xlabel("Comprimento de onda (nm)")
plt.ylabel("Intensidade (U.A)")


plt.subplot(2, 2, 2)
plt.plot(wavelenght3, spectrum3, color="green")
plt.plot(wavelenght4, spectrum4, color="lightgreen")
plt.plot(wavelenght5, spectrum5, color="darkgreen")
plt.xlabel("Comprimento de onda (nm)")   
plt.ylabel("Intensidade (U.A)")

plt.subplot(2, 2, 3)
plt.plot(wavelenght10, spectrum10, color="orange")
plt.plot(wavelenght6, spectrum6, color="red")
plt.plot(wavelenght7, spectrum7, color="lightcoral")
plt.xlabel("Comprimento de onda (nm)")
plt.ylabel("Intensidade (U.A)")

plt.subplot(2, 2, 4)
plt.plot(wavelenght8, spectrum8, color="purple")
plt.plot(wavelenght9, spectrum9, color="violet")
plt.xlabel("Comprimento de onda (nm)")
plt.ylabel("Intensidade (U.A)")

plt.show()

