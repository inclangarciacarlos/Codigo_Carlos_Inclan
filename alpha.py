import math

def calcular_CL_alpha(C_l_alpha, AR, e):
    return C_l_alpha / (1 + (C_l_alpha / (math.pi * AR))) * e


def calcular_alpha(C_L, C_L_alpha, alpha_0):
    return (C_L / C_L_alpha) + alpha_0


def main():
    # Solicitar datos al usuario
    C_l_alpha = float(input("Ingrese C_l_alpha (en grados): "))
    envergadura = float(input("Ingrese la envergadura (b): "))
    superficie_alar = float(input("Ingrese la superficie alar (S): "))
    e = float(input("Ingrese e (eficiencia): "))
    C_L = float(input("Ingrese C_L: "))
    alpha_0 = float(input("Ingrese alpha_0 (en grados): "))

    # Convertir valores angulares a radianes
    C_l_alpha = C_l_alpha * (180 / math.pi)
    alpha_0 = math.radians(alpha_0)

    # Calcular Aspect Ratio (AR)
    AR = envergadura ** 2 / superficie_alar

    # Calcular C_L_alpha
    C_L_alpha = calcular_CL_alpha(C_l_alpha, AR, e)

    # Calcular alpha
    alpha = calcular_alpha(C_L, C_L_alpha, alpha_0)

    # Convertir alpha a grados para la salida
    alpha_grados = math.degrees(alpha)

    # Mostrar resultados
    print(f"\nResultados:")
    print(f"Aspect Ratio (AR) = {AR:.4f}")
    print(f"C_L_alpha = {C_L_alpha:.4f}")
    print(f"Alpha (α) = {alpha_grados:.2f} grados")


if __name__ == "__main__":
    main()
