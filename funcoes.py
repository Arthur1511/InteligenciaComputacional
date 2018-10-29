import copy
import random
import numpy
import math


def lerDados(arquivo):
    file = open(arquivo, 'r')

    cidades = int(file.readline())

    file.readline()

    distancias = []

    for i in range(cidades):
        valores = file.readline().split()
        valores = [int(j) for j in valores]

        distancias.append(valores)
    file.close()
    return distancias, cidades


def calcularDistancias(arquivo):
    file = open(arquivo, 'r')

    qtdCidades = int(file.readline())

    vet_x = []
    vet_y = []
    distancias = []

    for i in range(qtdCidades):
        vet = []
        distancias.append(vet)
        for j in range(qtdCidades):
            distancias[i].append(float(0))

    for i in range(qtdCidades):
        coord = file.readline().split()
        coord = [float(j) for j in coord]
        vet_x.append(coord[1])
        vet_y.append(coord[2])

    for i in range(qtdCidades):
        for j in range(1, qtdCidades):
            distancias[i][j] = float(
                numpy.sqrt(numpy.power(vet_x[i] - vet_x[j], 2) + numpy.power(vet_y[i] - vet_y[j], 2)))
            distancias[j][i] = distancias[i][j]

    file.close()
    return distancias, qtdCidades


def buscaMenor(distancias, cidadeAtual, qtdCidades, cidadesVisitadas):
    menorDistancia = math.inf
    cidadeMaisProxima = -1
    for i in range(qtdCidades):
        if cidadeAtual != i and distancias[cidadeAtual][i] < menorDistancia and i not in cidadesVisitadas:
            menorDistancia = distancias[cidadeAtual][i]
            cidadeMaisProxima = i

    return menorDistancia, cidadeMaisProxima


def buscaParcial(distancias, cidadeAtual, qtdCidades, cidadesVisitadas, tamLCR):

    ordenado = copy.copy(distancias[cidadeAtual])

    for visitado in cidadesVisitadas:
        ordenado.remove(distancias[cidadeAtual][visitado])

    ordenado.sort()
    menorDistancia = ordenado[random.randrange(tamLCR)]

    for i in range(qtdCidades):
        if distancias[cidadeAtual][i] == menorDistancia and i not in cidadesVisitadas:
            cidadeMaisProxima = i

    return menorDistancia, cidadeMaisProxima


def vizinhoMaisProximo(distancias, qtdCidades, cidadeInicial, alpha):
    cidadesVisitadas = []
    cidadesNaoVisitadas = []
    fo = 0

    for i in range(qtdCidades):
        cidadesNaoVisitadas.append(i)

    cidadeAtual = cidadeInicial

    cidadesVisitadas.append(cidadeAtual)
    cidadesNaoVisitadas.remove(cidadeAtual)
    while cidadesNaoVisitadas:
        tamLCR = round((1 + alpha * (len(cidadesNaoVisitadas) - 1)))

        menorDistancia, proximaCidade = buscaParcial(distancias, cidadeAtual, qtdCidades, cidadesVisitadas, tamLCR)
        fo += menorDistancia

        cidadeAtual = proximaCidade
        cidadesVisitadas.append(cidadeAtual)
        cidadesNaoVisitadas.remove(cidadeAtual)

    fo += distancias[cidadesVisitadas[qtdCidades - 1]][cidadeInicial]
    cidadesVisitadas.append(cidadeInicial)

    return cidadesVisitadas, fo


def vizinhoMaisProximo2(distancias, qtdCidades, cidadeInicial):
    cidadesVisitadas = []
    cidadesNaoVisitadas = []
    fo = 0

    for i in range(qtdCidades):
        cidadesNaoVisitadas.append(i)

    cidadeAtual = cidadeInicial

    cidadesVisitadas.append(cidadeAtual)
    cidadesNaoVisitadas.remove(cidadeAtual)

    while cidadesNaoVisitadas:

        menorDistancia, proximaCidade = buscaMenor(distancias, cidadeAtual, qtdCidades, cidadesVisitadas)
        fo += menorDistancia
        cidadeAtual = proximaCidade

        cidadesVisitadas.append(cidadeAtual)
        cidadesNaoVisitadas.remove(cidadeAtual)

    fo += distancias[cidadesVisitadas[qtdCidades - 1]][cidadeInicial]
    cidadesVisitadas.append(cidadeInicial)

    return cidadesVisitadas, fo


def insercaoMaisBarata(matriz, tam):
    alpha = input("Digite o valor de alhpa:")

    tammatriz = ((tam - 2) * 3) - 1
    tammax = (tam - 3) * 3

    tammax = int(tammax)
    no = []

    alph = float(alpha)

    tamanhorlc = 1 + (alph * (tammax - 1))

    tamrlc = round(tamanhorlc)

    vet = []
    vet2 = []

    for i in range(0, tam):
        vet.append(99)
        vet2.append(i)

    for q in range(3, tam):
        vet[q] = q

    no.append(0)
    no.append(1)
    no.append(2)
    no.append(999)

    "aux = no"
    i = 0
    a = 0
    d = 0
    j = 0

    matriz2 = [[]]

    for d in range(0, tam - 3):

        k = 0
        a = 0
        cont = 1
        while (no[i] != 999):

            if (no[i + 1] == 999):
                prox = 0
            else:
                prox = no[i + 1]

            for j in range(0, tam):
                if (vet[j] != 99):
                    soma = (matriz[no[i]][j] + matriz[j][prox]) - matriz[no[i]][prox]
                    matriz2[a].insert(0, no[i])
                    matriz2[a].insert(1, vet[j])
                    matriz2[a].insert(2, prox)
                    matriz2[a].insert(3, soma)
                    matriz2.append([])
                    a = a + 1
            i = i + 1

        u = 0
        k = 0
        for u in range(0, tammax - 1):
            for k in range(0, tammax - 1):
                if (matriz2[u][3] < matriz2[k][3]):
                    auxt1 = matriz2[u][0]
                    auxt2 = matriz2[u][1]
                    auxt3 = matriz2[u][2]
                    auxt4 = matriz2[u][3]

                    matriz2[u][0] = matriz2[k][0]
                    matriz2[u][1] = matriz2[k][1]
                    matriz2[u][2] = matriz2[k][2]
                    matriz2[u][3] = matriz2[k][3]

                    matriz2[k][0] = auxt1
                    matriz2[k][1] = auxt2
                    matriz2[k][2] = auxt3
                    matriz2[k][3] = auxt4

        i = 0
        j = 0
        for i in range(0, tammatriz - 2):
            '''print('\n')'''
            for j in range(0, 4):
                '''print(matriz2[i][j])'''

        if (alph != 0):
            aleatorio = 1
        else:
            aleatorio = 0

        pos = matriz2[aleatorio][0]
        pos2 = no.index(pos)
        no.insert(pos2 + 1, matriz2[aleatorio][1])

        sub = 0

        for u in range(0, 1):
            if (matriz2[u][0] == 99):
                sub = sub + 1

        tamrlc = tamrlc - sub

        k = 0
        menor = 99
        for i in range(0, tammatriz - 2):
            if (matriz2[i][3] < menor):
                menor = matriz2[i][3]
                k = i

        for i in range(0, tam):
            if (matriz2[aleatorio][1] == vet[i]):
                vet[i] = 99
                break

        for i in range(0, tammatriz - 2):
            for j in range(0, 4):
                matriz2[i][j] = 99

        soma = 0
        i = 0

    tamanho = len(no)
    no[tamanho - 1] = 0

    somanova = 0

    for i in range(1, tamanho - 1):
        somanova += matriz[no[i]][no[i + 1]]

    return no, somanova


def calculaFo(distancias, rota):
    fo = 0

    for i in range(1, len(rota)):
        fo += distancias[rota[i - 1]][rota[i]]

    fo += distancias[rota[len(rota) - 1]][rota[0]]
    return fo


def descida(distancias, rota_construida, qtd_cidades, fo):
    melhor_fo = fo
    melhor_rota = rota_construida

    melhor_fo_vizinho = melhor_fo
    melhor_rota_vizinha = melhor_rota

    while 1:

        for i in range(1, qtd_cidades):
            for j in range(2, qtd_cidades):
                if i == j:
                    continue
                rota_vizinha = copy.copy(melhor_rota)
                aux = rota_vizinha[i]
                rota_vizinha[i] = rota_vizinha[j]
                rota_vizinha[j] = aux

                aux_fo = calculaFo(distancias, rota_vizinha)

                if aux_fo < melhor_fo_vizinho:
                    melhor_fo_vizinho = aux_fo
                    melhor_rota_vizinha = rota_vizinha

        if melhor_fo_vizinho < melhor_fo:
            melhor_fo = melhor_fo_vizinho
            melhor_rota = melhor_rota_vizinha

        else:
            break

    return melhor_rota, melhor_fo


def descidaPrimeiraMelhora(matriz, no, soma2):
    tamanho = len(no)
    k = 1
    j = 2
    somanova = 0
    contador = 0

    while (k <= tamanho - 2):
        j = 2
        while (j <= tamanho - 2):

            aux1 = no[k]
            no[k] = no[j]
            no[j] = aux1

            somanova = 0
            for i in range(0, tamanho - 1):
                somanova = somanova + matriz[no[i]][no[i + 1]]

            if (somanova < soma2):
                # print(no)
                soma2 = somanova
                # print(somanova)
                j = 2
                k = 0
                break
            else:
                aux1 = no[k]
                no[k] = no[j]
                no[j] = aux1
            j = j + 1
        k = k + 1

    return no, soma2


def aleatorio(distancias, qtdCidades, cidadeInicial):
    cidadesVisitadas = []
    cidadesNaoVisitadas = []
    fo = 0

    for i in range(qtdCidades):
        cidadesNaoVisitadas.append(i)

    cidadeAtual = cidadeInicial

    cidadesVisitadas.append(cidadeAtual)
    cidadesNaoVisitadas.remove(cidadeAtual)
    while cidadesNaoVisitadas:
        proximaCidade = random.choice(cidadesNaoVisitadas)
        adistancia = distancias[cidadeAtual][proximaCidade]

        fo += adistancia

        cidadeAtual = proximaCidade
        cidadesVisitadas.append(cidadeAtual)
        cidadesNaoVisitadas.remove(cidadeAtual)

    fo += distancias[cidadesVisitadas[qtdCidades - 1]][cidadeInicial]
    cidadesVisitadas.append(cidadeInicial)

    return cidadesVisitadas, fo


def descidaRandomica(distancias, qtdCidades, iterMax, s, fo1):  # descRandom(f(.), N(.), interMax, s)

    # uma estrutura de vizinhança N(:), s = solucao
    interacao = 0
    while (interacao < iterMax):

        # s' pertence N(s);
        solucao1 = random.randrange(1, qtdCidades)
        solucao2 = random.randrange(1, qtdCidades)
        interacao = interacao + 1

        rota_vizinha = copy.copy(s)
        aux = rota_vizinha[solucao1]
        rota_vizinha[solucao1] = rota_vizinha[solucao2]
        rota_vizinha[solucao2] = aux

        fo = calculaFo(distancias, rota_vizinha)

        if (fo < fo1):  # f(s') < f(s)
            interacao = 0
            s = rota_vizinha
            fo1 = fo

    return s, fo1


def descidaRealocada(distancias, rota_construida, qtd_cidades, fo):
    melhor_fo = fo
    melhor_rota = rota_construida

    melhor_fo_vizinho = melhor_fo
    melhor_rota_vizinha = melhor_rota

    while 1:

        for i in range(1, qtd_cidades):
            for j in range(2, qtd_cidades):
                if i == j:
                    continue
                rota_vizinha = copy.copy(melhor_rota)
                aux = rota_vizinha[i]
                rota_vizinha.remove(aux)
                rota_vizinha.insert(j, aux)

                aux_fo = calculaFo(distancias, rota_vizinha)

                if aux_fo < melhor_fo_vizinho:
                    melhor_fo_vizinho = aux_fo
                    melhor_rota_vizinha = rota_vizinha

        if melhor_fo_vizinho < melhor_fo:
            melhor_fo = melhor_fo_vizinho
            melhor_rota = melhor_rota_vizinha

        else:
            break

    return melhor_rota, melhor_fo


def descidaBloco2(distancias, rota_construida, qtd_cidades, fo):
    melhor_fo = fo
    melhor_rota = rota_construida

    melhor_fo_vizinho = melhor_fo
    melhor_rota_vizinha = melhor_rota

    while 1:

        for i in range(1, qtd_cidades - 3):
            for j in range(i + 2, qtd_cidades - 1):
                if i == j:
                    continue
                rota_vizinha = copy.copy(melhor_rota)
                aux1, aux2 = rota_vizinha[i], rota_vizinha[i + 1]
                rota_vizinha[i], rota_vizinha[i + 1] = rota_vizinha[j], rota_vizinha[j + 1]
                rota_vizinha[j], rota_vizinha[j + 1] = aux1, aux2

                aux_fo = calculaFo(distancias, rota_vizinha)

                if aux_fo < melhor_fo_vizinho:
                    melhor_fo_vizinho = aux_fo
                    melhor_rota_vizinha = rota_vizinha

        if melhor_fo_vizinho < melhor_fo:
            melhor_fo = melhor_fo_vizinho
            melhor_rota = melhor_rota_vizinha

        else:
            break

    return melhor_rota, melhor_fo


def descidaBloco3(distancias, rota_construida, qtd_cidades, fo):
    melhor_fo = fo
    melhor_rota = rota_construida

    melhor_fo_vizinho = melhor_fo
    melhor_rota_vizinha = melhor_rota

    while 1:

        for i in range(1, qtd_cidades - 6):
            for j in range(i + 3, qtd_cidades - 1):
                if i == j:
                    continue
                rota_vizinha = copy.copy(melhor_rota)
                aux1, aux2 = rota_vizinha[i], rota_vizinha[i + 1]
                rota_vizinha[i], rota_vizinha[i + 1] = rota_vizinha[j], rota_vizinha[j + 1]
                rota_vizinha[j], rota_vizinha[j + 1] = aux1, aux2

                aux_fo = calculaFo(distancias, rota_vizinha)

                if aux_fo < melhor_fo_vizinho:
                    melhor_fo_vizinho = aux_fo
                    melhor_rota_vizinha = rota_vizinha

        if melhor_fo_vizinho < melhor_fo:
            melhor_fo = melhor_fo_vizinho
            melhor_rota = melhor_rota_vizinha

        else:
            break

    return melhor_rota, melhor_fo


def shake(s, num_de_trocas):
    for i in range(num_de_trocas):
        troca1 = random.randrange(1, len(s) - 1)
        troca2 = random.randrange(1, len(s) - 1)
        aux = s[troca1]
        s[troca1] = s[troca2]
        s[troca2] = aux

    return s


def vnd(distancias, qtd_cidades, solucao_inicial, fo):

    solucao_corrente = solucao_inicial
    fo_corrente = fo

    grau_estrutura = 0

    while grau_estrutura < 4:
        print(grau_estrutura)
        if grau_estrutura == 0:
            solucao_vizinha, fo_vizinho = descida(distancias, solucao_corrente, qtd_cidades, fo)

        if grau_estrutura == 1:
            solucao_vizinha, fo_vizinho = descidaRealocada(distancias, solucao_corrente, qtd_cidades, fo)

        if grau_estrutura == 2:
            solucao_vizinha, fo_vizinho = descidaBloco2(distancias, solucao_corrente, qtd_cidades, fo)

        if grau_estrutura == 3:
            solucao_vizinha, fo_vizinho = descidaBloco3(distancias, solucao_corrente, qtd_cidades, fo)

        if fo_vizinho < fo_corrente:
            solucao_corrente = solucao_vizinha
            fo_corrente = fo_vizinho
            grau_estrutura = 0
        else:
            grau_estrutura += 1

    return solucao_vizinha, fo_vizinho


def vns(distancias, num_estruturas, solucao_inicial, fo):
    solucao_corrente = solucao_inicial
    fo_corrente = fo

    grau_estrutura = 1

    while grau_estrutura < num_estruturas:
        vizinho = shake(solucao_corrente, grau_estrutura)
        fo_vizinho = calculaFo(distancias, vizinho)

        if fo_vizinho < fo_corrente:
            solucao_corrente = vizinho
            fo_corrente = fo_vizinho
            grau_estrutura = 1
        else:
            grau_estrutura += 1

    return solucao_corrente, fo_corrente


def grasp(distancias, qtd_cidades, cidadeInicial, alpha, seed):
    random.seed(seed)
    criterio_de_parada = 10 * qtd_cidades
    melhor_fo = math.inf
    melhor_rota = []
    while criterio_de_parada != 0:
        rota, fo = vizinhoMaisProximo(distancias, qtd_cidades, cidadeInicial, alpha)
        rota, fo = descida(distancias, rota, qtd_cidades, fo)
        print(fo)
        # rota, fo = descidaPrimeiraMelhora(distancias, rota, fo)
        if fo < melhor_fo:
            melhor_fo = fo
            melhor_rota = rota
        criterio_de_parada -= 1

    return rota, fo


def simulated_annealing(distancias, alfa, sa_max, temperatura_ini, rota):
    solucao_corrente = rota
    iter_t = 0
    temperatura = temperatura_ini

    while temperatura > 0.0001:
        while iter_t < sa_max:

            iter_t += 1
            vizinho = shake(copy.copy(rota), 1)
            delta = calculaFo(distancias, vizinho) - calculaFo(distancias, rota)

            if delta < 0:
                rota = vizinho

                if calculaFo(distancias, vizinho) < calculaFo(distancias, solucao_corrente):
                    solucao_corrente = vizinho
            else:
                x = random.random()
                if x < math.pow(math.e, (-delta / temperatura)):
                    rota = vizinho

        temperatura *= alfa
        iter_t = 0

    rota = solucao_corrente

    return rota


def temperatura_inicial(distancias, beta, gama, sa_max, temperatura_ini, solucao_ini):
    continua = True
    temperatura = temperatura_ini

    while continua:
        aceitos = 0
        for iter_t in range(1, sa_max):
            vizinho = shake(copy.copy(solucao_ini), 1)
            delta = calculaFo(distancias, vizinho) - calculaFo(distancias, solucao_ini)

            if delta < 0:
                aceitos += 1

            else:
                x = random.random()
                if x < math.pow(math.e, (-delta / temperatura)):
                    aceitos += 1

        if aceitos >= gama * sa_max:
            continua = False

        else:
            temperatura *= beta

    return temperatura


def busca_tabu(distancias, qtd_cidades, rota_ini, bt_max, tabu_tam):
    melhor_rota = rota_ini
    melhor_fo = calculaFo(distancias, melhor_rota)
    rota_corrente = melhor_rota
    fo_corrente = melhor_fo
    iter_count = 0
    melhor_iter = 0
    tabu = []

    while iter_count - melhor_iter <= bt_max:
        troca = []
        melhor_fo_vizinho = fo_corrente
        melhor_rota_vizinha = rota_corrente

        for i in range(1, qtd_cidades):
            for j in range(2, qtd_cidades):
                if i == j:
                    continue
                rota_vizinha = copy.copy(rota_corrente)
                aux = rota_vizinha[i]
                rota_vizinha[i] = rota_vizinha[j]
                rota_vizinha[j] = aux

                aux_fo = calculaFo(distancias, rota_vizinha)

                if aux_fo < melhor_fo_vizinho:
                    melhor_fo_vizinho = aux_fo
                    melhor_rota_vizinha = rota_vizinha
                    troca = [j, i]

        if troca not in tabu or melhor_fo_vizinho < fo_corrente:
            if len(tabu) == tabu_tam:
                tabu.pop()
            tabu.append(troca)
            fo_corrente = melhor_fo_vizinho
            rota_corrente = melhor_rota_vizinha

        if fo_corrente < melhor_fo:
            melhor_fo = fo_corrente
            melhor_rota = rota_corrente
            melhor_iter = iter_count

        iter_count += 1

    return melhor_rota, melhor_fo
