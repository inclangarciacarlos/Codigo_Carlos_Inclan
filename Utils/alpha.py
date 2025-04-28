import math
import os
import numpy as np
from .xfoil import calculate_alpha_0_cl_alpha
from .Cl_obj import crear_columnas_Clobj

def extract_file_names(ruta_xfoil):
    archivos = [f for f in os.listdir(ruta_xfoil) if f.startswith('NACA') and f.endswith('.txt')]
    return archivos

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

def calcular_CL_alpha(slope, AR, e):
    return slope / (1 + (slope / (math.pi * AR))) * e

def calcular_alpha(CL_obj, CL_alpha, alpha_cl0):
    return (CL_obj / CL_alpha) + alpha_cl0

def calcular_alpha_from_txt(filename, condiciones_iniciales):
    CL_obj = crear_columnas_Clobj(condiciones_iniciales)
    alpha, cl = analyze_xfoil_data(filename)
    slope, alpha_cl0 = calculate_alpha_0_cl_alpha(alpha, cl)
    AR = (condiciones_iniciales['envergadura'])**2/condiciones_iniciales['superficie_ala']
    e = condiciones_iniciales['e']
    CL_alpha = calcular_CL_alpha(slope, AR, e)
    alpha_teorico = math.degrees(calcular_alpha(CL_obj, CL_alpha, alpha_cl0))
    return alpha_teorico
    
def crear_columnas_alpha(condiciones_iniciales, ruta_xfoil):
    archivos = extract_file_names(ruta_xfoil)
    alphas = []
    for name in archivos:
        ruta = f'{ruta_xfoil}\\{name}'
        alpha_teorico = calcular_alpha_from_txt(ruta, condiciones_iniciales)
        alphas.append(alpha_teorico)
    return np.array(alphas)   
    
        
        
        
        
        