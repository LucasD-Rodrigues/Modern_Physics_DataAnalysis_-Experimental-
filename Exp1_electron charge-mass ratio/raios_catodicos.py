import numpy as np
from numpy.polynomial import Polynomial
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams.update({
    "text.usetex": True,
    "font.family": "serif",  # or 'sans-serif' for a modern look
    "font.serif": ["Computer Modern Roman"],  # default LaTeX font
    "axes.labelsize": 16,    # LaTeX font size
    "font.size": 15,
    "legend.fontsize": 15,
    "xtick.labelsize": 16,
    "ytick.labelsize": 16
})

####################################
unc_I = 0.01
unc_U = 1

#parâmetros numéricos
mu0 = 4*np.pi*10**-7
R_b = 0.20 #(m)
N_voltas = 154
r1 = 0.02 #(m)
r2 = 0.03
r3 = 0.04
r4 = 0.05

U = [100,120,140,160,180,200,220,240,250,280,300]

###################################

k = lambda r: (r**2 / 2) * 64/125 * (mu0*N_voltas/R_b)**2

def U_func(I,r):
    return ((r**2 / 2) * 64/125 * (mu0*N_voltas/R_b)**2)*I**2


#para r=0.02 m

I1 = np.array([2.22, 2.49, 2.69, 2.96, 3.09, 3.33, 3.50, 3.62, 3.77, 3.97, 4.11])
I2 = np.array([2.43, 2.59, 2.77, 3.04, 3.27, 3.45, 3.65, 3.83, 3.91, 4.1, 4.25])

I_r1 = ((I1 + I2)*0.5).round(2)

x_r1 = U_func(I_r1, r1)
y_r1 = U

lin_regression1 = Polynomial.fit(x=x_r1, y=y_r1, deg=1)
b1, a1 = (lin_regression1.convert()).coef

x1_plot = np.linspace(x_r1.min(), x_r1.max(), 500)
y1_plot = lin_regression1(x1_plot)

#para r=0.03

I1 = np.array([1.36, 1.61, 1.78, 1.92, 2.07, 2.19, 2.30, 2.43, 2.48, 2.60, 2.71])
I2 = np.array([1.46, 1.70, 1.89, 2.05, 2.17, 2.29, 2.40, 2.52, 2.63, 2.72, 2.84])

I_r2 = 0.5*(I1 + I2)
x_r2 = U_func(I_r2, r2)

y_r2 = U

lin_regression2 = Polynomial.fit(x=x_r2, y=y_r2, deg=1)
b2, a2 = (lin_regression2.convert()).coef

x2_plot = np.linspace(x_r2.min(), x_r2.max(), 500)
y2_plot = lin_regression2(x2_plot)

#para r = 0.04 m

I1 = np.array([1.00, 1.16, 1.32, 1.44, 1.53, 1.62, 1.71, 1.79, 1.83, 1.95, 2.03])
I2 = np.array([1.00, 1.20, 1.34, 1.46, 1.55, 1.65, 1.73, 1.83, 1.86, 1.97, 2.06])

I_r3 = 0.5*(I1 + I2)
x_r3 = U_func(I_r3, r3)
y_r3 = U

lin_regression3 = Polynomial.fit(x=x_r3, y=y_r3, deg=1)
b3, a3 = (lin_regression3.convert()).coef

x3_plot = np.linspace(x_r3.min(), x_r3.max(), 500)
y3_plot = lin_regression3(x3_plot)

#para r = 0.05 m
I1 = np.array([0.80, 0.94, 1.04, 1.13, 1.22, 1.30, 1.38, 1.45, 1.49, 1.57, 1.63])
I2 = np.array([0.84, 0.97, 1.07, 1.15, 1.25, 1.33, 1.41, 1.48, 1.50, 1.59, 1.68])

I_r4 = 0.5*(I1 + I2)
x_r4 = U_func(I_r4, r4)
y_r4 = U

lin_regression4 = Polynomial.fit(x=x_r4, y=y_r4, deg=1)
b4, a4 = (lin_regression4.convert()).coef

x4_plot = np.linspace(x_r4.min(), x_r4.max(), 500)
y4_plot = lin_regression4(x4_plot)

np.savez("raios_catodicos_data.npz", x1_plot=x1_plot, x2_plot=x2_plot, y1_plot=y1_plot, y2_plot=y2_plot, x3_plot=x3_plot, y3_plot=y3_plot, x4_plot=x4_plot, y4_plot=y4_plot, x_r1=x_r1, y_r1=y_r1, x_r2=x_r2, y_r2=y_r2, x_r3=x_r3, y_r3=y_r3, x_r4=x_r4, y_r4=y_r4, a1=a1, a2=a2, a3=a3, a4=a4)

print("saved")




