"""
=========================================================
PROBLEMA C – Canicas de colores
Parcial 4 | MM3014 Teoría de Probabilidades
=========================================================

EXPERIMENTO BASE:
  Una caja tiene 5 canicas rojas, 3 azules y 2 verdes.
  Se extraen 2 canicas SIN reemplazo.

PREGUNTAS:
  a) P(ambas son rojas)

  b) [BAYES] Hay dos cajas:
       Caja 1: 5 rojas, 3 azules, 2 verdes
       Caja 2: 2 rojas, 5 azules, 3 verdes
     Se elige una caja al azar, se sacan 2 canicas sin reemplazo.
     El resultado fue: 1 roja y 1 verde.
     Estimar: P(Caja 1 | resultado fue 1 roja y 1 verde)

CONCEPTOS USADOS:
  - Probabilidad simple: conteo de casos favorables sobre total.
  - Teorema de Bayes:
      P(Caja1 | obs) = P(obs | Caja1) * P(Caja1)
                       ─────────────────────────────
                              P(obs)
    En la simulación esto se hace directamente:
    filtramos todos los experimentos donde el resultado fue la observación,
    y dentro de esos contamos los que correspondían a Caja 1.

CÓMO CAMBIAR ESTE PROGRAMA:
  - Para cambiar la composición de cada caja: modifica CAJA_1 y CAJA_2.
    Cada caja es una lista con las canicas representadas como strings.
  - Para cambiar el número de canicas extraídas: modifica N_EXTRACCIONES.
  - Para cambiar el resultado observado del inciso b: modifica la función `es_resultado_observado`.
"""

import random

# ─────────────────────────────────────────────
# PARÁMETROS CONFIGURABLES
# ─────────────────────────────────────────────
SEMILLA        = 2026
N_REPETICIONES = 10_000
N_EXTRACCIONES = 2     # Número de canicas a extraer sin reemplazo

# Composición de las cajas (cada string representa el color de una canica)
# Para cambiar la cantidad, agrega o quita elementos de la lista.
CAJA_1 = ["roja"] * 5 + ["azul"] * 3 + ["verde"] * 2   # 10 canicas
CAJA_2 = ["roja"] * 2 + ["azul"] * 5 + ["verde"] * 3   # 10 canicas


# ─────────────────────────────────────────────
# FUNCIONES DEL EXPERIMENTO
# ─────────────────────────────────────────────

def extraer_sin_reemplazo(caja, n):
    """
    Extrae n canicas al azar sin reemplazo de la caja dada.
    Retorna una lista con los colores de las canicas extraídas.

    Parámetros:
      caja (list): lista de colores disponibles en la caja.
      n    (int) : número de canicas a extraer.
    """
    return random.sample(caja, n)


def es_resultado_observado(extracciones):
    """
    Define el resultado observado en el inciso b de Bayes.
    CONDICIÓN ACTUAL: exactamente 1 roja y 1 verde entre las extraídas.

    Para cambiar la observación (ej. '2 azules'):
      return extracciones.count("azul") == 2
    """
    return extracciones.count("roja") == 1 and extracciones.count("verde") == 1


# ─────────────────────────────────────────────
# SIMULACIÓN PRINCIPAL
# ─────────────────────────────────────────────

def simular():
    random.seed(SEMILLA)

    # ── Contadores inciso a (una sola caja) ───
    conteo_ambas_rojas = 0

    # ── Contadores inciso b (Bayes, dos cajas) ─
    conteo_resultado_obs     = 0   # veces que el resultado fue la observación
    conteo_caja1_y_resultado = 0   # veces que fue Caja 1 Y el resultado observado

    for _ in range(N_REPETICIONES):

        # ── Inciso a: extraer de CAJA_1 ──────
        extraccion_a = extraer_sin_reemplazo(CAJA_1, N_EXTRACCIONES)
        if extraccion_a.count("roja") == N_EXTRACCIONES:
            conteo_ambas_rojas += 1

        # ── Inciso b: elegir caja y extraer ──
        # P(Caja 1) = P(Caja 2) = 0.5 (se elige al azar)
        caja_elegida = random.choice([1, 2])
        caja         = CAJA_1 if caja_elegida == 1 else CAJA_2

        extraccion_b = extraer_sin_reemplazo(caja, N_EXTRACCIONES)

        if es_resultado_observado(extraccion_b):
            conteo_resultado_obs += 1
            if caja_elegida == 1:
                conteo_caja1_y_resultado += 1

    # ── Cálculo de probabilidades ─────────────
    p_ambas_rojas = conteo_ambas_rojas / N_REPETICIONES

    # P(Caja1 | observación) = casos(Caja1 ∩ obs) / casos(obs)
    p_caja1_dado_resultado = (
        conteo_caja1_y_resultado / conteo_resultado_obs
        if conteo_resultado_obs > 0 else 0
    )

    # ── Salida ────────────────────────────────
    print(f"P(ambas rojas) = {p_ambas_rojas:.4f}")
    print(f"P(Caja 1 | una roja y una verde) = {p_caja1_dado_resultado:.4f}")


# ─────────────────────────────────────────────
# PUNTO DE ENTRADA
# ─────────────────────────────────────────────
if __name__ == "__main__":
    simular()
