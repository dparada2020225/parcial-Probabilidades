# -*- coding: utf-8 -*-
"""
=========================================================
PROBLEMA D - Cartas
Parcial 4 | MM3014 Teoria de Probabilidades
=========================================================

EXPERIMENTO BASE:
  De una baraja estandar de 52 cartas se extraen 2 cartas SIN reemplazo.

PREGUNTAS:
  a) P(ambas cartas son ases)
  b) Sean:
       A = "la primera carta es un As"
       B = "la segunda carta es un As"
     Determinar si A y B son eventos independientes.

     Dos eventos son independientes si y solo si:
       P(A inter B) = P(A) * P(B)
     En la practica de simulacion comparamos ambos lados con una tolerancia
     pequena (TOLERANCIA), ya que los valores simulados nunca seran exactamente iguales.

CONCEPTOS USADOS:
  - Probabilidad simple: frecuencia relativa de cada evento.
  - Independencia de eventos: P(A inter B) aprox P(A) * P(B).
    Si son aproximadamente iguales -> independientes; si no -> dependientes.

COMO CAMBIAR ESTE PROGRAMA:
  - Para cambiar que tipo de carta define A y B: modifica la funcion `es_as`.
    Por ejemplo, para buscar reyes: return carta[0] == "K"
  - Para cambiar el numero de cartas extraidas: modifica N_EXTRACCIONES
    (y ajusta las funciones evento_a / evento_b si corresponde).
  - Para cambiar la tolerancia de independencia: modifica TOLERANCIA.
    La diferencia exacta teorica entre P(A inter B) y P(A)*P(B) es ~0.0014,
    por lo que TOLERANCIA = 0.001 permite detectar la dependencia correctamente.
"""

import random

# -----------------------------------------
# PARAMETROS CONFIGURABLES
# -----------------------------------------
SEMILLA        = 2026
N_REPETICIONES = 10_000
N_EXTRACCIONES = 2        # Numero de cartas a extraer
TOLERANCIA     = 0.001    # Margen para comparar P(A inter B) con P(A)*P(B)


# -----------------------------------------
# CONSTRUCCION DE LA BARAJA
# -----------------------------------------

def construir_baraja():
    """
    Crea una baraja estandar de 52 cartas.
    Cada carta es un string con formato "valor_palo".
    Ejemplo: "A_corazones", "K_picas", "5_treboles".

    Para modificar la baraja (ej. agregar comodines):
      agrega elementos a la lista antes de retornarla.
    """
    valores = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    palos   = ["corazones", "diamantes", "treboles", "picas"]
    return [f"{v}_{p}" for v in valores for p in palos]  # 52 cartas


# -----------------------------------------
# DEFINICION DE EVENTOS
# -----------------------------------------

def es_as(carta):
    """
    Determina si una carta es un As.
    Retorna True si el valor de la carta empieza con "A".

    Para buscar otro tipo (ej. reyes): return carta.startswith("K")
    """
    return carta.startswith("A")


def evento_a(cartas):
    """
    Evento A: la PRIMERA carta extraida es un As.
    cartas[0] es la primera carta del par extraido.
    """
    return es_as(cartas[0])


def evento_b(cartas):
    """
    Evento B: la SEGUNDA carta extraida es un As.
    cartas[1] es la segunda carta del par extraido.
    """
    return es_as(cartas[1])


# -----------------------------------------
# SIMULACION PRINCIPAL
# -----------------------------------------

def simular():
    random.seed(SEMILLA)
    baraja = construir_baraja()   # Se construye una vez; cada repeticion la mezcla

    # Contadores
    conteo_a     = 0   # veces que ocurre A
    conteo_b     = 0   # veces que ocurre B
    conteo_a_y_b = 0   # veces que ocurren A y B juntos (A inter B)

    for _ in range(N_REPETICIONES):
        # Extraer N_EXTRACCIONES cartas sin reemplazo
        cartas = random.sample(baraja, N_EXTRACCIONES)

        a = evento_a(cartas)
        b = evento_b(cartas)

        if a:
            conteo_a += 1
        if b:
            conteo_b += 1
        if a and b:
            conteo_a_y_b += 1

    # Calculo de probabilidades
    p_a         = conteo_a     / N_REPETICIONES
    p_b         = conteo_b     / N_REPETICIONES
    p_a_inter_b = conteo_a_y_b / N_REPETICIONES
    p_a_por_p_b = p_a * p_b

    # Dos eventos son independientes si P(A inter B) aprox P(A)*P(B)
    son_independientes = abs(p_a_inter_b - p_a_por_p_b) < TOLERANCIA

    # Salida
    print(f"P(ambas ases) = {p_a_inter_b:.4f}")
    print(f"P(A) * P(B) = {p_a_por_p_b:.4f}")
    print(f"Los eventos son independientes: {son_independientes}")


# -----------------------------------------
# PUNTO DE ENTRADA
# -----------------------------------------
if __name__ == "__main__":
    simular()
