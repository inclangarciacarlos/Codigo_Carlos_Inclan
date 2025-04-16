import os
def extraer_NACA_nums(nombre):
    codigo = nombre[4:8]
    return [codigo[0], codigo[1], codigo[2:]]
def crear_listas(ruta):
    # Paso 1: Extraer los nombres de los archivos
    archivos = [f[:-4] for f in os.listdir(ruta) if f.startswith('NACA') and f.endswith('.txt')]
    col_1 = archivos

    # Paso 2: Crear columnas a partir de col_1
    col_1_1 = []
    col_1_2 = []
    col_1_3 = []

    for nombre in col_1:
        d1, d2, ultimos = extraer_NACA_nums(nombre)
        col_1_1.append(d1)
        col_1_2.append(d2)
        col_1_3.append(ultimos)

    return col_1, col_1_1, col_1_2, col_1_3

# USO
ruta = r"D:\AAUNIVERSIDAD\Practicas empresa\Proyecto\PYTHON\Proyecto NACAS\pythonProject1\Xfoil"
col_1, col_1_1, col_1_2, col_1_3 = crear_listas(ruta)

# Mostrar resultados
for i in range(len(col_1)):
    print(f"{col_1[i]}  {col_1_1[i]}  {col_1_2[i]}  {col_1_3[i]}")