import numpy as np
import pandas as pd

from Utils import crear_columnas_nombres
from Utils import create_simulation_columns
from Utils import crear_columnas_Clobj
from Utils import crear_columnas_alpha



def funcion_principal(condiciones_iniciales, ruta_xfoil, ruta_simulaciones):
    col_1, col_1_1, col_1_2, col_1_3 = crear_columnas_nombres(ruta_xfoil)
    col_2 = crear_columnas_Clobj(condiciones_iniciales)
    col_3, col_4 = create_simulation_columns(ruta_simulaciones)
    col_5 = crear_columnas_alpha(condiciones_iniciales, ruta_xfoil)



    df = pd.DataFrame({
        "NACA": col_1,
        "camber": col_1_1,
        "posicion_camber": col_1_2,
        "espesor": col_1_3,
        "Cl_obj": col_2,
        "Cl": col_3,
        "Cd": col_4,
        "alpha": col_5
    })

    return df
if __name__ == "__main__":
    ruta_xfoil = r"D:\AAUNIVERSIDAD\Practicas empresa\Proyecto\PYTHON\Proyecto NACAS\pythonProject1\Xfoil"
    ruta_simulaciones = r"D:\AAUNIVERSIDAD\Practicas empresa\Proyecto\PYTHON\Proyecto NACAS\pythonProject1\Simulaciones"
    condiciones_iniciciales = {
    "velocidad_crucero":63.89,
    "altitud_crucero":3660,
    "peso_maximo":1000,
    "cuerda":1.5,
    "envergadura":10,
    "superficie_ala":15,
    "e":0.88
    }
    print(funcion_principal(condiciones_iniciciales, ruta_xfoil, ruta_simulaciones))
