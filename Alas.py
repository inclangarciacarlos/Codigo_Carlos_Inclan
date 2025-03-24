import math

# constantes
rho_0 = 1.225  # Densidad a nivel del mar en kg/m3
lambda_ = -0.0065  # Gradiente térmico en K/m
T_0 = 288.15  # Temperatura a nivel del mar en K
g_0 = 9.81  # Gravedad en m/s^2
R = 287  # m^2/s^2K
mu_0 = 1.81e-5 #Viscosidad a nivel del mar en kg/m.s
S = 110.4  # Constante para el aire en K
gamma = 1.4 # Relación de calores específicos para el aire

# Función para obtener los datos del usuario
def obtener_inputs():
    print("Introduce los siguientes valores:")

    velocidad_crucero = float(input("Velocidad de crucero (m/s): "))
    altitud_crucero = float(input("Altitud de crucero (m): "))
    peso_maximo = float(input("Peso máximo del avión (kg): "))
    cuerda = float(input("Cuerda del perfil (m): "))
    envergadura = float(input("Envergadura del ala (m): "))
    superficie_ala = float(input("Superficie alar del ala (m^2): "))

    return velocidad_crucero, altitud_crucero, peso_maximo, cuerda, envergadura, superficie_ala

#Cálculo de la densidad del aire a la altitud de crucero
def calcular_densidad(altitud):

    #Fórmula de densidad a la altitud dada
    densidad = rho_0 * (1+(lambda_ * altitud) / T_0) ** ((-g_0 / (R * lambda_)) -1)

    return densidad

#Cálculo de la temperatura a la altitud de crucero
def calcular_temperatura(altitud):
    T = T_0 + lambda_ * altitud #Temperatura a la altitud dada
    return T

#Cálculo de la viscosidad dinámica a la altitud de crucero
def calcular_viscosidad(altitud):
    T = calcular_temperatura(altitud)
    viscosidad = mu_0 * (T / T_0) ** 1.5 * (T_0 + S) / (T + S)
    return viscosidad

#Cálculo del número de Reynolds
def calcular_numero_reynolds(densidad, velocidad, cuerda, viscosidad):
    Re = (densidad * velocidad * cuerda) / viscosidad
    return Re

#Cálculo del coeficiente de sustentación objetivo
def calcular_coeficiente_sustentacion(peso, densidad, velocidad, superficie_ala):
    coeficiente_sustentacion = (2 * peso * g_0) / (densidad * velocidad**2 * superficie_ala)
    return coeficiente_sustentacion

# Cálculo de la velocidad del sonido a la altitud de crucero
def calcular_velocidad_sonido(temperatura):
    velocidad_sonido = math.sqrt(gamma * R * temperatura)
    return velocidad_sonido

# Cálculo del número de Mach
def calcular_mach(velocidad, velocidad_sonido):
    mach = velocidad / velocidad_sonido
    return mach


# Función principal
def main():
    # Obtener los datos del usuario
    velocidad_crucero, altitud_crucero, peso_maximo, cuerda, envergadura, superficie_ala = obtener_inputs()

    # Calcular la densidad del aire a la altitud de crucero
    densidad_aire = calcular_densidad(altitud_crucero)

    # Calcular la temperatura a la altitud de crucero
    temperatura_aire = calcular_temperatura(altitud_crucero)

    # Calcular la viscosidad dinámica a la altitud de crucero
    viscosidad_aire = calcular_viscosidad(altitud_crucero)

    # Calcular el número de Reynolds
    numero_reynolds = calcular_numero_reynolds(densidad_aire, velocidad_crucero, cuerda, viscosidad_aire)

    # Calcular el coeficiente de sustentación
    coeficiente_sustentacion = calcular_coeficiente_sustentacion(peso_maximo, densidad_aire, velocidad_crucero, superficie_ala)

    # Calcular la velocidad del sonido
    velocidad_sonido = calcular_velocidad_sonido(temperatura_aire)

    # Calcular el número de Mach
    numero_mach = calcular_mach(velocidad_crucero, velocidad_sonido)

    # Mostrar los resultados
    print("\nResultados:")
    print(f"Densidad del aire a {altitud_crucero} m: {densidad_aire:.4f} kg/m^3")
    print(f"Temperatura a {altitud_crucero:.1f} m: {temperatura_aire:.2f} K")
    print(f"Viscosidad dinámica a {altitud_crucero} m: {viscosidad_aire:.8f} Pa·s")
    print(f"Número de Reynolds: {numero_reynolds:.2f}")
    print(f"Coeficiente de sustentación (C_L): {coeficiente_sustentacion:.4f}")
    print(f"Número de Mach: {numero_mach:.3f}")

# Ejecutamos el programa
if __name__ == "__main__":
    main()
