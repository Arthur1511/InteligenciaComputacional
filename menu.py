import funcoes
import timeit

print('#####################################################')
print('####        Problema do Caixeiro Viajante        ####')
print('#####################################################\n')

nomeArq = input('Digite o nome do arquivo para base de dados:')

distancias, qtdCidades = funcoes.calcularDistancias(nomeArq)

rota = []
fo = 0

while True:

    print("\n*******************Menu Principal************************* \n")
    print("ATENCAO: Necessario gerar solucao inicial antes de refinar\n")
    print("                1. Gere solucao inicial \n")
    print("                2. Descida \n")
    print("                3. Descida randomica \n")
    print("                4. Descida com Primeiro de Melhora \n")
    print("                0. Sair \n")
    var = int(input("                Escolha: "))

    if var == 1:
        print("\n************Geracao da Solucao Inicial**************** \n")
        print("                1. Gulosa (Vizinho mais proximo) \n")
        print("                2. Parcialmente gulosa (Vizinho mais proximo) \n")
        print("                3. Gulosa (Insercao Mais Barata) \n")
        print("                4. Parcialmente gulosa (Insercao Mais Barata) \n")
        print("                5. Aleatoria \n")
        print("                0. Sair \n")

        opcaoMenu = int(input("                Escolha: "))

        if opcaoMenu == 1:
            print()
            cidadeInicial = int(input("Insira a cidade inicial:"))
            inicio = timeit.default_timer()
            rota, fo = funcoes.vizinhoMaisProximo2(distancias, qtdCidades, cidadeInicial)
            fim = timeit.default_timer()
            print()
            print("Rota ->", rota, "\n", "FO=", fo)
            print("Tempo de execução(s):", fim - inicio)

        elif opcaoMenu == 2:
            print()
            cidadeInicial = int(input("Insira a cidade inicial:"))
            alpha = float(input("Insira o valor de Alfa:"))
            inicio = timeit.default_timer()
            rota, fo = funcoes.vizinhoMaisProximo(distancias, qtdCidades, cidadeInicial, alpha)
            fim = timeit.default_timer()
            print()
            print("Rota ->", rota, "\n", "FO=", fo)
            print("Tempo de execução(s):", fim - inicio)

        elif opcaoMenu == 3:
            inicio = timeit.default_timer()
            rota, fo = funcoes.insercaoMaisBarata(distancias, qtdCidades)
            fim = timeit.default_timer()
            print()
            print("Rota ->", rota, "\n", "FO=", fo)
            print("Tempo de execução(s):", fim - inicio)

        elif opcaoMenu == 4:
            print("teste3")

        elif opcaoMenu == 5:
            cidadeInicial = int(input("Insira a cidade inicial:"))
            inicio = timeit.default_timer()
            rota, fo = funcoes.aleatorio(distancias, qtdCidades, cidadeInicial)
            fim = timeit.default_timer()
            print("Rota ->", rota, "\n", "FO=", fo)
            print("Tempo de execução(s):", fim - inicio)

        else:
            continue

    elif var == 2:
        inicio = timeit.default_timer()
        rota_refinada, fo_refinada = funcoes.descida(distancias, rota, qtdCidades, fo)
        fim = timeit.default_timer()
        print("Rota Refinada ->", rota_refinada, "\n", "FO Refinado=", fo_refinada)
        print("Tempo de execução(s):", fim - inicio)

    elif var == 3:
        print()
        iterMax = int(input("Insira a quantidade maxima de iterações:"))
        inicio = timeit.default_timer()
        rota_refinada, fo_refinada = funcoes.descidaRandomica(distancias, qtdCidades, iterMax, rota, fo)
        fim = timeit.default_timer()
        print()
        print("Rota Refinada ->", rota_refinada, "\n", "FO Refinado=", fo_refinada)
        print("Tempo de execução(s):", fim - inicio)

    elif var == 4:
        inicio = timeit.default_timer()
        rota_refinada, fo_refinada = funcoes.descidaPrimeiraMelhora(distancias, rota, fo)
        fim = timeit.default_timer()
        print()
        print("Rota Refinada ->", rota_refinada, "\n", "FO Refinado=", fo_refinada)
        print("Tempo de execução(s):", fim - inicio)
    else:
        break

