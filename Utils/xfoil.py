import numpy as np
import math
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
        if cl[i] * cl[i + 1] <= 0:  # Cambio de signo
            # Interpolación lineal entre alpha[i] y alpha[i+1]
            alpha_cl0 = alpha[i] + (-cl[i]) * (alpha[i+1] - alpha[i]) / (cl[i+1] - cl[i])
            return alpha_cl0
    return None  # Si no se encuentra cambio de signo


def calculate_alpha_0_cl_alpha(alpha, cl):
    dif_cl = []
    for i in range(len(alpha) - 1):
        dif_cl = dif_cl + [calculate_slope(alpha, cl, i + 1)]
    dif_cl = np.array(dif_cl)
    i = find_change_slope(dif_cl)
    slope = calculate_slope(alpha, cl, i)
    slope = slope * (180 / math.pi)
    alpha_cl0 = find_alpha_cl0(alpha, cl)
    alpha_cl0 = math.radians(alpha_cl0)
    return slope, alpha_cl0
