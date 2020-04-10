## CLASSES DE FUNÇÕES
    Seja U c R^2 aberto.
    Seja f: U c R^2 -> R
    Dizemos que f é de classe C^1 se:
    as derivadas parciais existem em todo U e são contínuas

### TEOREMA
    f é de classe C^1 => f é diferenciável

## SUBCONJUNTO ABERTO / FECHADO
    Seja X um espaço métrico.
    Um subconjunto U c X é aberto se:
    para todo x pert. a U existe r > 0 | B_r(x) c U

    Ou seja, para qualquer x desse subconjunto,
    dá pra fazer uma bola centrada em x
    e essa bola está inteira dentro do subconjunto.

    F c X é fechado <=> X \ F é aberto

## SUBCONJUNTO LIMITADO / ILIMITADO
    Seja X um espaço métrico.
    Um subconjunto A c X é limitado se:
    existe x pert. X e r >= 0 | A c B_r(x)

    Ou seja, é limitado se estiver contido em alguma bola de raio finito.
    É ilimitado caso contrário.

## VIZINHANÇA
    Seja X um espaço métrico.
    Um subconjunto V c X é vizinhança de x pert. a X se:
    existe r > 0 | B_r(x) c V

    Ou seja, V é vizinhança de x se é possível fazer uma bola
    centrada em x e essa bola está inteira dentro de V.

## COMPACTO
    Um subconjunto K c R^n é compacto se K é FECHADO e LIMITADO.

## CONTINUIDADE
    Uma função de R^n -> R^m é contínua se:
    para todo epsilon existe um delta tal que
    se x pert. B_delta(a) => f(x) pert. B_epsilon(f(a))

    Ou então, em termos de limite:
    Uma função de R^n -> R^m é contínua se:

    lim  f(x) = f(a)
    x->a

## DIFERENCIABILIDADE
    Sejam A c R^m e f: A -> R^n.
    Suponha que A contém uma  vizinhança de a.
    Dizemos que f é diferenciável em a se:
    Existe uma matriz B de ordem n x m tal que

          f(a + h) - f(a) - B.h
    lim  ---------------------- = 0
    h->0         || h ||

    A matriz B é chamada de derivada de f em a e é denotada por Df(a).

    Exemplo de verificação de diferenciabilidade no ponto (0,0)
    de uma função de R^2 -> R definida por partes


             |     xy
             | ----------- , se (x,y) != (0,0)
    f(x,y) = |  x^2 + y^2
             |
             |      0      , se (x,y) = (0,0)


                 f(h,k) - f(0,0) - Grad f(0,0).(h,k)
        lim     ------------------------------------ = 0
    (h,k)->(0,0)         || (h,k) ||

    Existência de derivadas parciais não garante diferenciabilidade!

## TEOREMA 1 - DIFERENCIABILIDADE E DERIVADAS DIRECIONAIS
    Sejam A c R^m e f: A -> R^n.
    Se f é diferenciável em a pert. A,
    então todas as derivadas direcionais de f existem em a e

    del f
    ----- (a) = Df(a).u
    del u

## TEOREMA 2 - DIFERENCIABILIDADE E CONTINUIDADE
    Sejam A c R^m e f: A -> R^n.
    Se f é diferenciável em a pert. A,
    então f é contínua em a.

## REGRA DA CADEIA
    f: R^2 -> R
    g: R^2 -> R
    h: R^2 -> R^2

    f = g o h
    f(x,y) = g(h(x,y))
    h(x,y) = (u(x,y),v(x,y))
    f(x,y) = g(u(x,y),v(x,y))

    Df(x,y) = D(g o h)(x,y)
            = Dg(h(x,y)).Dh(x,y)

## VETOR TANGENTE A UMA LINHA
    f: R -> R^2 (função do tipo "parametrização")
    f(t) = (cos(t),sin(t))
    O vetor tangente em cada ponto da linha é dado por f'(t):
    f'(t) = (-sin(t),cos(t))

## RETA TANGENTE A UMA LINHA
    Seja L uma linha descrita pela função f(t)
    Seja a um ponto de L, a = f(t_0)
    f'(t_0) = T, vetor tangente a L no ponto t_0.
    Reta tangente no ponto a é a reta que passa em a e tem direção de T:
    {x pert. R^n : x = a + lambda T; lambda pert. R}

    ex: f : R -> R^3, f(t) = (cos(t),sin(t),t)
    então f'(t) = (-sin(t),cos(t),1)
    para t = pi/2:
    f(pi/2) = (0,1,pi/2)
    f'(pi/2) = (-1,0,1)
    Reta tangente a f em pi/2:
    (x,y,z) = (0,1,pi/2) + lambda(-1,0,1), lambda pert. R

## DEFINIÇÃO: FUNÇÃO SOBREJETORA
    Uma função f: R^n -> R^m é sobrejetora se:
    para cada y em R^m existe x em R^n tal que f(x) = y.
    "para todos os y do contradomínio tem um x no domínio | f(x) = y"

## DEFINIÇÃO: FUNÇÃO INJETORA
    Uma função f: R^n -> R^m é injetora se:
    para cada x1, x2 pert. R^n tem-se f(x1) != f(x2).
    "a função leva cada um dos x do domínio a um y diferente no contradomínio"

## DEFINIÇÃO: FUNÇÃO LOCALMENTE SOBREJETORA
    Seja x_0 um ponto no domínio de F: R^n -> R^m com F(x_0) = b_0.
    Então F é localmente sobrejetora em x_0 se:
    dada qualquer bola aberta B_r(x_0) em torno de x_0 em R^n,
    existe uma bola B_s(b_0) em torno de b_0 em R^m tal que
    para cada b em B_s(b_0), existe pelo menos um x em B_r(x_0)
    tal que F(x) = b.

## DEFINIÇÃO: FUNÇÃO LOCALMENTE INJETORA
    F é localmente injetora em x_0 se existem
    uma bola B_r(x_0) em torno de x_0 em R^n e
    uma bola B_s(b_0) em torno de b_0 em R^m tais que
    para todo b pert. B_s(b_0) existe no máximo um x em B_r(x_0)
    tal que F(x) = b.

## DEFINIÇÃO: DIFEOMORFISMO
    Sejam U e V abertos do R^n e f: U -> V uma bijeção.
    Dizemos que f é um difeomorfismo se:
    f e f^-1 são diferenciáveis.

    Dois fatos óbvios:
    1) a composta de difeomorfismos é um difeomorfismo
    2) a inversa de um difeomorfismo é um difeomorfismo

## TEOREMA DA FUNÇÃO INVERSA
    O teorema da função inversa diz basicamente que:
    se f'(x_0) é invertível, então f é invertível numa vizinhança de x_0.

    Se f: R^n -> R^n é uma função de classe C^R e Df é invertível num ponto x_0
    então f é localmente um difeomorfismo de classe C^R

    Obs. o T. F. Inversa vale sse o T. F. Implícita vale.

## TEOREMA DA FUNÇÃO IMPLÍCITA
    Suponha que seja dada a relação F(x,y) = 0.
    Para cada valor x podem existir 0, 1 ou mais valores de y
    satisfazendo a equação.
    Se I = (x_0 - h, x_0 + h) é um intervalo tal que
    para cada x pert. a I existe exatamente um y satisfazendo a equação,
    então F(x,y) = 0 define y como uma função de x implicitamente sobre I.

    Um teorema de função implícita é um teorema que
    determina condições sob as quais uma relação como F(x,y) = 0
    define y como função de x ou x como função de y.
    A solução é local, isto é, o tamanho do intervalo I
    pode ser menor que o domínio da relação F.

    O exemplo mais simples de um teorema de função implícita:
    se F é diferenciável e P é um ponto em que F não se anula,
    então é possível expressar y como função de x
    em uma região contendo esse ponto.

    Teorema: suponha que F, F_x e F_y são contínuas sobre um
    subconjunto aberto A de R^2 contendo o ponto P = (x_0,y_0).
    Suponha que:
    F(x_0,y_0) = 0,    F_y(x_0,y_0) != 0
    Então existem números h e k que determinam
    um retângulo R contido em A tal que:
    para cada x em I = {x : |x-x_0| < h}
    existe um único y em J = {y : |y-y_0| < k}
    que satisfaz a equação F(x,y) = 0.
    A totalidade dos pontos (x,y) formam uma função f
    cujo domínio contém I e cuja imagem está em J.

    Para encontrar os pontos em que existem os intervalos I e J:
    1) Tira o gradiente da função.

                           del F(a,b)
    2) (a,b) são tais que ------------ != 0
                             del y

                del F(a,b)
               ------------
                  del x
    f'(a) = - --------------
                del F(a,b)
               ------------
                  del y