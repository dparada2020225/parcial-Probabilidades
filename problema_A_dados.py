"""
=========================================================
PROBLEMA A – Dados
Parcial 4 | MM3014 Teoría de Probabilidades
=========================================================

EXPERIMENTO BASE:
  Lanzar dos dados justos de 6 caras y observar la suma.

PREGUNTAS:
  a) P(suma = 7)
  b) P(suma = 7 | al menos uno de los dados es par)

CONCEPTOS USADOS:
  - Probabilidad condicional: P(A|B) = P(A ∩ B) / P(B)
  - Para estimar P(A|B) filtramos solo los experimentos donde B ocurrió,
    luego contamos cuántos de esos también cumplen A.

CÓMO CAMBIAR ESTE PROGRAMA:
  - Para cambiar el número de caras de los dados: modifica CARAS_DADO
  - Para cambiar la suma objetivo: modifica SUMA_OBJETIVO
  - Para cambiar el número de repeticiones: modifica N_REPETICIONES
  - Para cambiar la condición del inciso b: reemplaza la función `condicion_b`
"""

import random

# ─────────────────────────────────────────────
# PARÁMETROS CONFIGURABLES
# ─────────────────────────────────────────────
SEMILLA         = 2026   # Semilla para reproducibilidad
N_REPETICIONES  = 10_000 # Número de experimentos a simular
CARAS_DADO      = 6      # Número de caras de cada dado
SUMA_OBJETIVO   = 7      # Suma que queremos estimar


# ─────────────────────────────────────────────
# FUNCIONES DEL EXPERIMENTO
# ─────────────────────────────────────────────

def lanzar_dado():
    """Simula un dado justo con CARAS_DADO caras. Retorna un entero entre 1 y CARAS_DADO."""
    return random.randint(1, CARAS_DADO)


def lanzar_dos_dados():
    """
    Lanza dos dados independientes.
    Retorna una tupla (dado1, dado2).
    """
    return lanzar_dado(), lanzar_dado()


def condicion_b(dado1, dado2):
    """
    Define la condición del evento B para el inciso b.
    CONDICIÓN ACTUAL: Al menos uno de los dados es par.

    Para cambiar la condición (ej. 'al menos uno es impar'):
      return (dado1 % 2 != 0) or (dado2 % 2 != 0)
    """
    return (dado1 % 2 == 0) or (dado2 % 2 == 0)


# ─────────────────────────────────────────────
# SIMULACIÓN PRINCIPAL
# ─────────────────────────────────────────────

def simular():
    random.seed(SEMILLA)

    # Contadores para el inciso a
    conteo_suma_objetivo = 0          # veces que la suma == SUMA_OBJETIVO

    # Contadores para el inciso b (probabilidad condicional)
    conteo_condicion_b        = 0     # veces que se cumple la condición B
    conteo_suma_y_condicion_b = 0     # veces que se cumple A ∩ B

    for _ in range(N_REPETICIONES):
        d1, d2 = lanzar_dos_dados()
        suma = d1 + d2

        # ── Inciso a ──────────────────────────────
        if suma == SUMA_OBJETIVO:
            conteo_suma_objetivo += 1

        # ── Inciso b ──────────────────────────────
        if condicion_b(d1, d2):
            conteo_condicion_b += 1
            if suma == SUMA_OBJETIVO:
                conteo_suma_y_condicion_b += 1

    # ── Cálculo de probabilidades ─────────────
    p_suma = conteo_suma_objetivo / N_REPETICIONES

    # P(A|B) = (casos donde A y B ocurren) / (casos donde B ocurre)
    p_suma_dado_condicion_b = (
        conteo_suma_y_condicion_b / conteo_condicion_b
        if conteo_condicion_b > 0 else 0
    )

    # ── Salida ────────────────────────────────
    print(f"P(suma = {SUMA_OBJETIVO}) = {p_suma:.4f}")
    print(f"P(suma = {SUMA_OBJETIVO} | al menos un par) = {p_suma_dado_condicion_b:.4f}")


# ─────────────────────────────────────────────
# PUNTO DE ENTRADA
# ─────────────────────────────────────────────
if __name__ == "__main__":
    simular()
