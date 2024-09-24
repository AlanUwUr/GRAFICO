import numpy as np
import matplotlib.pyplot as plt

# Definir las ecuaciones del sistema
def eq1(x1):
    return (2 - 1.0001 * x1) / 1.0000

def eq2(x1):
    return (2 - 1.0000 * x1) / 1.0000

# Rango de valores para x1
x1_values = np.linspace(0, 2, 100)

# Calcular las líneas correspondientes a las dos ecuaciones
y1_values = eq1(x1_values)
y2_values = eq2(x1_values)

# Crear el gráfico
plt.plot(x1_values, y1_values, label='1.0001x1 + 1.0000x2 = 2')
plt.plot(x1_values, y2_values, label='1.0000x1 + 1.0000x2 = 2', linestyle='--')

# Configuración del gráfico
plt.xlabel('x1')
plt.ylabel('x2')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True)
plt.legend()
plt.title('Sistema de ecuaciones lineales')

# Mostrar el gráfico
plt.show()
