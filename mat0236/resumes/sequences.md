# SEQUÊNCIAS

## Definição de convergência
    Uma sequência a_n -> L se dado qualquer
    epsilon > 0, existe N >= 0 tal que
    |a_n - L| < epsilon para todo n >= N

## Teorema
    Se existe f(x) tal que f(n) = a_n e lim f(x) = L,
    então lim (a_n) = L
    "o limite é igual ao limite da contínua"

## Teorema
    Se lim (a_n) = L e lim (c_n) = L
    e a_n <= b_n <= c_n,
    então b_n -> L
    "sanduíche"

## Teorema
    Se lim |a_n| = 0, então lim a_n = 0
    "só vale se o limite for igual a zero"

## Teorema
    A sequência r^n só converge se -1 < r <= 1
    lim (r^n) = /  0  se  -1 < r < 1
                \  1  se  r = 1
    "sequência geométrica"

## Teorema
    Se lim (a_2n) = L e lim (a_2n+1) = L,
    então lim (a_n) = L
    "termos pares e ímpares convergem"

## Teorema
    Se f é contínua em x = L e a_n -> L então
    f(a_n) -> f(L)
    "o limite passa pra dentro da função"

## Teorema
    Toda sequência monótona e limitada é convergente
    "o último"

    Calculando limite de sequência

    1) Calcular limite da função contínua
    2) Atentar para a ordem de crescimento

    c < log(n) < n^k < a^n < n! < n^n

    f(n) / g(n) -> 0 <=> O.C.(f(n)) > O.C.(g(n))
    f(n) / g(n) -> L <=> O.C.(f(n)) = O.C.(g(n))

    Caso clássico
    (1 + k/n)^n -> k
    "faz e^ln e resolve o limite"