# constantes
rho_0 = 1.225  # Densidad a nivel del mar en kg/m3
lambda_ = -0.0065  # Gradiente térmico en K/m
T_0 = 288.15  # Temperatura a nivel del mar en K
g_0 = 9.81  # Gravedad en m/s^2
R = 287  # m^2/s^2K
mu_0 = 1.81e-5 #Viscosidad a nivel del mar en kg/m.s
S = 110.4  # Constante para el aire en K
gamma = 1.4 # Relación de calores específicos para el aire

#Cálculo del coeficiente de sustentación objetivo
# def crear_columnas_Clobj(peso_maximo,altitud_crucero, velocidad, superficie_ala):
def crear_columnas_Clobj(condiciones_iniciales):
    peso_maximo = condiciones_iniciales['peso_maximo']
    altitud_crucero = condiciones_iniciales['altitud_crucero']
    velocidad = condiciones_iniciales['velocidad_crucero']
    superficie_ala =condiciones_iniciales['superficie_ala']

    densidad = rho_0 * (1 + (lambda_ * altitud_crucero) / T_0) ** ((-g_0 / (R * lambda_)) - 1)
    coeficiente_sustentacion = (2 * peso_maximo * g_0) / (densidad * velocidad**2 * superficie_ala)
    return coeficiente_sustentacion

