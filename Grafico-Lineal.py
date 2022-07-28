from turtle import color
import matplotlib.pyplot as plt

#Años y población de España 2016-2020
x=[2016,2017,2018,2019,2020]
y=[46.48,46.50,46.8,47.1,47.35]

#Años y población Argentina 2016-2020
x2=x
y2=[43.59,44.04,44.49,44.95,45.38]

#Gráficas
plt.plot(x,y,marker='o',color='red',label='España')
plt.plot(x2,y2,marker='o',color='blue',label='Argentina')

plt.title('POblación de España y Argebtina entre 2016-2020')
plt.legend()

plt.show()