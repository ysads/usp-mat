# -*- coding: utf-8 -*-
#
# 8910368 - Ygor Sad Machado
#
from random import random, seed

# Fixa a semente do gerador de números aleatórios para manter
# a consistência nos resultados da simulação
seed(1)

# Calcula a distância Manhattan entre dois pontos p1 e p2
def manhattan_distance(p1, p2):
    return sum(abs(a-b) for a, b in zip(p1, p2))

# Gera um ponto aleatório num grid quadrado de lado L
def rand_coord(l):
    return [random() * l, random() * l]

# Realiza o experimento um determinado número de vezes para
# um valor de L e um número de ambulâncias fixados
def experiment(num, l, ambulances):
    sum_distance = 0

    for i in range(int(num)):
        accident = rand_coord(l)

        # Gera uma lista contendo o número de ambulâncias recebido
        coord_ambulances = [rand_coord(l) for j in range(ambulances)]

        # Soma somente a menor distância entre alguma ambulância e
        # o local do acidente
        sum_distance += min(
            [manhattan_distance(accident, amb) for amb in coord_ambulances]
        )

    return sum_distance / num

def item_a():
    print("A. ")

    for n in [1e5, 1e6, 1e7]:
        expectation = experiment(num=n, l=1, ambulances=1)
        print("{it:.1e} iterations => {e}".format(it=n, e=expectation))

    print("\n")

def item_b():
    print("B. ")

    for length in range(2,8):
        expectation = experiment(num=1e6, l=length, ambulances=1)
        print("L={l} => {e}".format(l=length, e=expectation))

    print("\n")

def item_c():
    print("C. ")

    for n in [1e5, 1e6, 1e7]:
        expectation = experiment(num=1e6, l=1, ambulances=2)
        print("{it:.1e} iterations => {e}".format(it=n, e=expectation))

    print("\n")

def item_d():
    print("D.")

    for n in [1e5, 1e6, 1e7]:
        print("{it:.1e} iterations".format(it=n))

        for length in range(1,5):
            num_ambulances = 0
            expectation = 1e20

            while (expectation >= length / 3.0):
                num_ambulances += 1
                expectation = experiment(num=n, l=length, ambulances=num_ambulances)

            print(
                "L={l} | expectation={e} => {amb} ambulances".format(
                    l=length, e=expectation, amb=num_ambulances
                )
            )
        print("\n")

item_a()
item_b()
item_c()
item_d()
