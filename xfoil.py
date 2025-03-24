import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


def check_linearity(arr):
    """
    Checks if a 1D array follows a linear pattern using R².

    Parameters:
        arr (numpy array): Input 1D array.

    Returns:
        float: R² value (1.0 means perfectly linear).
    """
    x = np.arange(len(arr))  # Create x-values as indices
    y = arr

    # Fit a linear model (y = mx + b)
    m, b = np.polyfit(x, y, 1)

    # Predict values using the fitted model
    y_pred = m * x + b

    # Compute R²
    ss_total = np.sum((y - np.mean(y))**2)  # Total sum of squares
    ss_residual = np.sum((y - y_pred)**2)   # Residual sum of squares
    r2 = 1 - (ss_residual / ss_total)

    return r2

def analyze_xfoil_data(filename):
    """
    Analiza un archivo de datos de XFOIL para determinar la zona lineal,
    la pendiente de la curva C_L vs Alpha y el ángulo de ataque donde C_L = 0.
    """
    try:
        # Leer el archivo y extraer las líneas con datos numéricos
        with open(filename, "r") as f:
            lines = f.readlines()

        # Encontrar la línea donde comienzan los datos
        start_idx = None
        for i, line in enumerate(lines):
            if "alpha" in line.lower():  # Encontramos la cabecera de los datos
                start_idx = i + 2  # Datos empiezan dos líneas después
                break

        if start_idx is None:
            print("❌ No se encontró la cabecera 'alpha' en el archivo. Verifica el formato del archivo.")
            return None, None

        print(f"✔ Línea de inicio de datos encontrada en la línea {start_idx}")

        # Intentar cargar los datos desde esa línea
        try:
            data = np.loadtxt(lines[start_idx:], dtype=float)
        except Exception as e:
            print(f"❌ Error al cargar datos numéricos: {e}")
            return None, None

        print(f"✔ Datos cargados correctamente, tamaño: {data.shape}")

        # Verificar que hay al menos dos columnas
        if data.shape[1] < 2:
            print("❌ El archivo no tiene suficientes columnas. Se esperaban al menos 2 (alpha y Cl).")
            return None, None

        # Extraer columnas relevantes
        alpha = data[:, 0]  # Ángulo de ataque
        cl = data[:, 1]  # Coeficiente de sustentación
        return alpha, cl

    except Exception as e:
        print('falló')
        return None, None


def find_change_slope(arr, bound=0.9):
    i = 1
    while check_linearity(arr[:i+1]) > bound:
        i = i + 1
    return i


def calculate_slope(arrx, arry, i):
    return (arry[i]-arry[0]) / (arrx[i]-arrx[0])

def find_alpha_cl0(alpha, cl):
    """
    Encuentra el ángulo de ataque donde Cl = 0 mediante interpolación lineal.
    """
    for i in range(len(cl) - 1):
        if cl[i] * cl[i + 1] < 0:  # Cambio de signo
            # Interpolación lineal entre alpha[i] y alpha[i+1]
            alpha_cl0 = alpha[i] + (-cl[i]) * (alpha[i+1] - alpha[i]) / (cl[i+1] - cl[i])
            return alpha_cl0
    return None  # Si no se encuentra cambio de signo




# Prueba la función con tu archivo
filename = ("D:\\AAUNIVERSIDAD\\Practicas empresa\\Proyecto\\Xfoil\\NACA_2412.txt")
alpha, cl = analyze_xfoil_data(filename)
# CAMABIAR ESTA LÍNEAAAA
dif_cl = []
for i in range(len(alpha) -1):
    dif_cl = dif_cl + [calculate_slope(alpha, cl, i+1)]
dif_cl = np.array(dif_cl)
print(dif_cl)

#dif_cl = np.diff(cl) / np.diff(alpha)

# slope, alpha_cl0 = analyze_xfoil_data(filename)

r2 = check_linearity(dif_cl[:7])
print('r2', r2)

i = find_change_slope(dif_cl)
print('i',i)
slope = calculate_slope(alpha, cl, i)

# Cálculo de alpha donde Cl = 0
alpha_cl0 = find_alpha_cl0(alpha, cl)



if alpha is not None:
    print(f"\n✅ Resultados finales:")
    print(f"Pendiente en la zona lineal: {slope:.4f} 1/°")
    if alpha_cl0 is not None:
        print(f"Ángulo de ataque donde C_L = 0: {alpha_cl0:.4f}°")
    else:
        print("⚠ No se encontró un cambio de signo en C_L, verifica los datos.")

# Recta de la pendiente calculada en la zona lineal
b = cl[0] - slope * alpha[0]  # Calculamos la intersección con el eje C_L
cl_fit = slope * alpha + b  # Ecuación de la recta

# Gráfica
plt.figure(figsize=(8, 5))
plt.plot(alpha, cl, label="C_L vs Alpha")
plt.plot(alpha[:-1], dif_cl, label="Pendiente local dC_L/dAlpha")
plt.plot(alpha, cl_fit, label="Recta de pendiente calculada", linestyle="dotted", color="red")
plt.axhline(0, color="gray", linestyle="--", linewidth=0.8)
if alpha_cl0 is not None:
    plt.axvline(alpha_cl0, color="red", linestyle="--", label=f"α donde C_L=0: {alpha_cl0:.2f}°")
plt.xlabel("Ángulo de ataque (°)")
plt.ylabel("C_L")
plt.legend()
plt.show()