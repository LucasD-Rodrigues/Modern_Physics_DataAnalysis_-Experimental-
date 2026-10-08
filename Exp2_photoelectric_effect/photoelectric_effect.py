import numpy as np
import pandas as pd

spectrum1 = np.loadtxt("espectro-azul.txt")

data1 = pd.DataFrame(spectrum1)

print(data1)