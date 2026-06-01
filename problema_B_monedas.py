"""
=========================================================
PROBLEMA B – Monedas
Parcial 4 | MM3014 Teoría de Probabilidades
=========================================================

EXPERIMENTO BASE:
  Lanzar tres monedas justas (cara = 1, cruz = 0).

PREGUNTAS:
  a) P(exactamente 2 caras)
  b) E[X], donde X = número de caras obtenidas

CONCEPTOS USADOS:
  - Probabilidad de un evento: P(A) = casos favorables / total
  - Valor esperado: E[X] = promedio de los valores de X en todas las repeticiones.
    Se estima como la suma total de caras dividida entre el número de experimentos.

CÓMO CAMBIAR ESTE PROGRAMA:
  - Para cambiar el número de monedas: modifica N_MONEDAS
  - Para cambiar el número de caras exactas del inciso a: modifica CARAS_EXACTAS
  - Para cambiar el número de repeticiones: modifica N_REPETICIONES
"""

import random

# ─────────────────────────────────────────────
# PARÁMETROS CONFIGURABLES
# ─────────────────────────────────────────────
SEMILLA        = 2026
N_REPETICIONES = 10_000
N_MONEDAS      = 3    # Cantidad de monedas a lanzar
CARAS_EXACTAS  = 2    # Número exacto de caras para el inciso a


# ─────────────────────────────────────────────
# FUNCIONES DEL EXPERIMENTO
# ─────────────────────────────────────────────

def lanzar_moneda():
    """
    Simula una moneda justa.
    Retorna 1 (cara) o 0 (cruz) con igual probabilidad.
    """
    return random.randint(0, 1)


def lanzar_monedas():
    """
    Lanza N_MONEDAS monedas independientes.
    Retorna el número total de caras obtenidas.
    """
    return sum(lanzar_moneda() for _ in range(N_MONEDAS))


# ─────────────────────────────────────────────
# SIMULACIÓN PRINCIPAL
# ─────────────────────────────────────────────

def simular():
    random.seed(SEMILLA)

    conteo_caras_exactas = 0   # veces que salieron exactamente CARAS_EXACTAS caras
    suma_total_caras     = 0   # acumulado de X para calcular E[X]

    for _ in range(N_REPETICIONES):
        x = lanzar_monedas()   # x = número de caras en este experimento

        # ── Inciso a ──────────────────────────────
        if x == CARAS_EXACTAS:
            conteo_caras_exactas += 1

        # ── Inciso b ──────────────────────────────
        suma_total_caras += x

    # ── Cálculo de resultados ─────────────────
    p_caras_exactas = conteo_caras_exactas / N_REPETICIONES
    esperanza_x     = suma_total_caras / N_REPETICIONES

    # ── Salida ────────────────────────────────
    print(f"P(exactamente {CARAS_EXACTAS} caras) = {p_caras_exactas:.4f}")
    print(f"E[X] = {esperanza_x:.4f}")


# ─────────────────────────────────────────────
# PUNTO DE ENTRADA
# ─────────────────────────────────────────────
if __name__ == "__main__":
    simular()
