# SÉRIES

### Definição
    lim (S_n) ou SUM (a_n)
    "limite da soma dos termos de uma sequência
    com n tendendo a infinito"

### Teorema
    Se SUM (a_n) converge, então
    lim (a_n) = 0
    "teste de divergência: limite do termo geral"

### Séries clássicas
    SUM (1/n) diverge     "uma p-série com p = 1"
    SUM (1/n^2) converge  "uma p-série com p = 2"


# SÉRIE GEOMÉTRICA

### Definição
    SUM [1, inf) (a*r^(n-1)) ou SUM [0, inf) (a*r^n)

    Convergência
    Converge se | r | < 1
    SUM [0, inf) (a*r^n) = a / (1 - r)

# SÉRIE TELESCÓPICA

### Definição
    S_n tem um número limitado de termos
    depois de cancelamentos

    Convergência
    Resolver limite de S_n


# SÉRIE HARMÔNICA

### Definição
    SUM (1/n)
    "é uma p-série com p = 1"

    Convergência
    Diverge


# TESTES

### Teste da integral
    Se f(x) é uma função contínua, positiva e decrescente
    em [k, inf) e f(n) = a_n, então
    1. se I [k, inf) f(x) dx é convergente,
       SUM [k, inf) (a_n) é convergente
    2. se I [k, inf) f(x) dx é divergente,
       SUM [k, inf) (a_n) é divergente

    "este teste não dá o valor da série"

    "o k de início da integral deve ser
    o mesmo k de início da série"

    "a função e a série não precisam ser
    sempre positivas ou decrescentes, apenas
    eventualmente e dali para frente"

-------------------------------------------------

### Teste da p-série
    Se k > 0, então
    SUM [k, inf) (1/n^p) converge para p > 1 e
                         diverge para p <= 1

-------------------------------------------------

### Teste da comparação
    Suponha que temos duas séries
    SUM (a_n) e SUM (b_n)
    com a_n, b_n >= 0 e a_n < b_n, então:
    1) se SUM (b_n) converge, SUM (a_n) converge
    2) se SUM (a_n) diverge, SUM (b_n) diverge
    "ambas as séries devem começar no mesmo k"
    "os requerimentos só precisam ser verdade eventualmente
    e dali para frente"

-------------------------------------------------

    ### Teste da comparação do limite
    Suponha que temos duas séries
    SUM (a_n) e SUM (b_n)
    com a_n >= 0, b_n > 0
    Seja c = lim n->inf a_n/b_n
    Se c é positivo e finito, ou
    a) as duas séries convergem, ou
    b) as duas divergem
    "tanto faz quem é o numerador e o denominador"

-------------------------------------------------

### Teste da alternância
    Suponha que temos uma série SUM (a_n) e
    a_n pode ser escrita como
    (-1)^n * b_n    ou    (-1)^(n+1) * b_n
    Então se
    1) lim n->inf b_n = 0   e
    2) {b_n} é uma sequência decrescente
    SUM (a_n) é convergente


# CONVERGÊNCIA ABSOLUTA/CONDICIONAL

    Definições
    Uma série SUM (a_n) é absolutamente convergente se
    SUM |a_n| converge.
    Uma série SUM (a_n) é condicionalmente convergente se
    SUM (a_n) converge e SUM |a_n| diverge.

    Fato
    Convergência absoluta é mais forte que convergência
    Se SUM |a_n| converge, então SUM (a_n) converge

-------------------------------------------------

### Teste da razão
    Suponha que temos uma série SUM (a_n)
    Definimos L = lim n->inf |(a_(n+1))/(a_n)|
    Então:
    1) se L < 1, a série converge absolutamente
    2) se L > 1, a série diverge
    3) L = 1, inconclusivo

-------------------------------------------------

### Teste da raiz
    Suponha que temos uma série SUM (a_n)
    Definimos L = lim n->inf |a_n|^(1/n)
    Então:
    1) se L < 1, a série converge absolutamente
    2) se L > 1, a série diverge
    3) L = 1, inconclusivo

    Fato
    lim n->inf n^(1/n) = 1

-------------------------------------------------

### Passos:

    1) Caso pareça que o limite do termo geral não vai para zero:
       Teste de Divergência
       lim a_n != 0 => diverge

    2) Caso seja uma p-série ou uma série geométrica:
       p-série converge para p > 1
       geométrica converge para | r | < 1

    3) Caso seja parecida com uma p-série ou com uma geométrica:
       Teste da Comparação (termos devem ser todos positivos)

    4) Caso seja uma fração de polinômios ou raízes de polinômios:
       Teste da Comparação (termos devem ser todos positivos)
       Teste da Comparação do limite (termos devem ser todos positivos)
       c = lim a_n / b_n, 0 < c < oo => a_n e b_n têm mesmo comportamento

    5) Caso possa ser escrita na forma (-1)^n * b_n ou (-1)^(n+1) * b_n:
       Teste da Série Alternada
       Teste de Convergência Absoluta

    6) Caso contenha fatoriais:
       Teste da Razão (único)

    7) Caso contenha constantes elevadas a expoentes contendo n:
       Teste da Razão

    8) Caso possa ser escrita como (b_n)^n:
       Teste da Raiz

    9) Caso a_n = f(n) e seja fácil de resolver a integral:
       Teste da Integral (f(x) eventualmente positiva e decrescente)

# SÉRIE DE POTÊNCIAS

    SUM [0, oo) c_n * (x - a)^n

    Normalmente faz o teste da razão ou da raiz.

    1. Sempre converge para x = a
    2. Raio de convergência:
       | x - a | < R
    3. Intervalo de convergência:
       a − R < x < a + R

### Casos especiais:
    1. Se a série converge apenas para x = a:
       R = 0
       I: x = a
    2. Se a série converge para todo x:
       R = oo
       I: -oo < x < oo

    Encontrando a série de potência de uma função:

    1) Fazer aparecer 1 / (1 - x)
    2) Esse termo é relacionado com a série SUM (x^n), desde que | x | < 1
    3) Se sobrar termo no numerador (com x ou sem x), fatora,
       coloca o termo multiplicando a série e distribui pra dentro da série.
    4) Se sobrar alguma constante, deixa pra fora da série.

    Derivada e Integral de Série de Potências
    "deriva ou integra o termo geral normalmente, regra do tombo"
    Se f(x) = SUM [0,oo) c_n * (x - a)^n tem raio de convergência R > 0, então:

            oo
    f'(x) = SUM n * c_n * (x - a)^(n - 1)              raio de conv = R
            n=1

                      oo          (x - a)^(n + 1)
    INT f(x) dx = C + SUM c_n * ------------------     raio de conv = R
                      n=0              n + 1
