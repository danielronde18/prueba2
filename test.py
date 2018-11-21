# Ejercicio5
# imprima el mensaje: "hola mundo!" 
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
print("hola mundo ")

x=np.zeros((2,2),float)
print(x)
z=np.shape(x)
print(z)
def rellena(x):
    for i in range(z[0]):
        x[i][i]=1#np.random.random()
    return x

print(rellena(x))

x1=np.linspace(-1,1,100)
def f(x):
    return x**2




plt.figure()
plt.plot(x1,f(x1))
plt.show
plt.savefig("curva")