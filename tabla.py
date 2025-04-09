import numpy as np
import pandas as pd

# Crear arrays de datos con 6 filas cada uno
columna_1 = np.array(["NACA0012", "NACA0021", "NACA2412", "NACA2421", "NACA4415", "NACA4424"])
columna_1_1 = np.array([0, 0, 2, 2, 4, 4])
columna_1_2 = np.array([0, 0, 4, 4, 4, 4])
columna_1_3 = np.array([12, 21, 12, 21, 15, 24])
columna_2 = np.array([0.3776, 0.3776, 0.3776, 0.3776, 0.3776, 0.3776])
columna_3 = np.array([0.4102, 0.3820, 1.6887, 1.3036, 2.5339, 1.4162])
columna_4 = np.array([0.1293, 0.1175, 0.1758, 0.1522, 0.1412, 0.1252])
columna_5 = np.array([4.92, 4.9, 2.73, 2.76, 0.62, 0.88])

# Crear un DataFrame
df = pd.DataFrame({
    "NACA": columna_1,
    "camber": columna_1_1,
    "posicion_camber": columna_1_2,
    "espesor": columna_1_3,
    "Cl_obj": columna_2,
    "Cl": columna_3,
    "Cd": columna_4,
    "alpha_teorico (º)": columna_5,
})

# Exportar a CSV
df.to_csv("datos.csv", index=False, sep=';', encoding='utf-8')

print("Archivo CSV generado exitosamente.")


print(df.iloc[:,:4])
print(df.iloc[:,3:])