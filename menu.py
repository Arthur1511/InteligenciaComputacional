import funcoes
import timeit

print('#####################################################')
print('####        Problema do Caixeiro Viajante        ####')
print('#####################################################\n')

print("\n*******************Formato de Arquivo************************* \n")
print("                1. Arquivo de coordenadas \n")
print("                2. Arquivo de com matriz de distancias \n")
print("                0. Sair \n")
var = int(input("                Escolha: "))

if var == 1:
    nomeArq = input('Digite o nome do arquivo para base de dados:')
    distancias, qtdCidades = funcoes.calcularDistancias(nomeArq)

if var == 2:
    nomeArq = input('Digite o nome do arquivo para base de dados:')
    distancias, qtdCidades = funcoes.lerDados(nomeArq)

if var == 0:
    exit(1)

rota = []
fo = 0

while True:

    print("\n*******************Menu Principal************************* \n")
    print("ATENCAO: Necessario gerar solucao inicial antes de refinar\n")
    print("                1. Gere solucao inicial \n")
    print("                2. Descida \n")
    print("                3. Descida randomica \n")
    print("                4. Descida com Primeiro de Melhora \n")
    print("                5. VNS \n")
    print("                6. GRASP \n")
    print("                7. VND \n")
    print("                8. Simulated Annealing \n")
    print("                9. Busca Tabu \n")
    print("                0. Sair \n")
    var = int(input("                Escolha: "))

    if var == 0:
        exit(1)
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
            print("Parcialmente gulosa (Vizinho mais proximo): \n")
            cidadeInicial = int(input("Insira a cidade inicial:"))
            alpha = float(input("Insira o valor de Alfa:"))
            inicio = timeit.default_timer()
            rota, fo = funcoes.vizinhoMaisProximo(distancias, qtdCidades, cidadeInicial, alpha)
            fim = timeit.default_timer()
            print()
            print("Rota ->", rota, "\n", "FO=", fo)
            print("Tempo de execução(s):", fim - inicio)

        elif opcaoMenu == 3:
            print()
            print("Gulosa (Insercao Mais Barata:) \n")
            inicio = timeit.default_timer()
            rota, fo = funcoes.insercaoMaisBarata(distancias, qtdCidades)
            fim = timeit.default_timer()
            print()
            print("Rota ->", rota, "\n", "FO=", fo)
            print("Tempo de execução(s):", fim - inicio)

        elif opcaoMenu == 4:
            print("Parcialmente gulosa (Insercao Mais Barata) \n")

        elif opcaoMenu == 5:
            print()
            print("Aleatoria \n")
            cidadeInicial = int(input("Insira a cidade inicial:"))
            inicio = timeit.default_timer()
            rota, fo = funcoes.aleatorio(distancias, qtdCidades, cidadeInicial)
            fim = timeit.default_timer()
            print("Rota ->", rota, "\n", "FO=", fo)
            print("Tempo de execução(s):", fim - inicio)

        else:
            continue

    elif var == 2:
        print()
        print("Descida: \n")
        inicio = timeit.default_timer()
        rota_refinada, fo_refinada = funcoes.descida(distancias, rota, qtdCidades, fo)
        fim = timeit.default_timer()
        print("Rota Refinada ->", rota_refinada, "\n", "FO Refinado=", fo_refinada)
        print("Tempo de execução(s):", fim - inicio)

    elif var == 3:
        print()
        print("Descida Randomica:")
        iterMax = int(input("Insira a quantidade maxima de iterações:"))
        inicio = timeit.default_timer()
        rota_refinada, fo_refinada = funcoes.descidaRandomica(distancias, qtdCidades, iterMax, rota, fo)
        fim = timeit.default_timer()
        print()
        print("Rota Refinada ->", rota_refinada, "\n", "FO Refinado=", fo_refinada)
        print("Tempo de execução(s):", fim - inicio)

    elif var == 4:
        print()
        print("Descida Primeira de Melhora")
        inicio = timeit.default_timer()
        rota_refinada, fo_refinada = funcoes.descidaPrimeiraMelhora(distancias, rota, fo)
        fim = timeit.default_timer()
        print()
        print("Rota Refinada ->", rota_refinada, "\n", "FO Refinado=", fo_refinada)
        print("Tempo de execução(s):", fim - inicio)

    elif var == 5:
        print()
        print("VNS:\n")
        inicio = timeit.default_timer()
        rota_refinada, fo_refinada = funcoes.vns(distancias, 5, rota, fo)
        fim = timeit.default_timer()
        print()
        print("Rota Refinada ->", rota_refinada, "\n", "FO Refinado=", fo_refinada)
        print("Tempo de execução(s):", fim - inicio)

    elif var == 6:
        print()
        print("GRASP:\n")
        cidadeInicial = int(input("Insira a cidade inicial:"))
        alpha = float(input("Insira o valor de Alfa:"))
        seed = int(input("Insira o valor da semente:"))
        inicio = timeit.default_timer()
        rota_refinada, fo_refinada = funcoes.grasp(distancias, qtdCidades, cidadeInicial, alpha, seed)
        fim = timeit.default_timer()
        print()
        print("Rota Refinada ->", rota_refinada, "\n", "FO Refinado=", fo_refinada)
        print("Tempo de execução(s):", fim - inicio)

    elif var == 7:
        print()
        print("VND:\n")
        inicio = timeit.default_timer()
        rota_refinada, fo_refinada = funcoes.vnd(distancias, qtdCidades, rota, fo)
        fim = timeit.default_timer()
        print()
        print("Rota Refinada ->", rota_refinada, "\n", "FO Refinado=", fo_refinada)
        print("Tempo de execução(s):", fim - inicio)

    elif var == 8:
        print()
        print("Simulated Annealing:\n")
        print("Calculando temperatura...")
        temperatura = round(funcoes.temperatura_inicial(distancias, 1.2, 0.95, 200 * qtdCidades, 100, rota))
        print("Temperatura inicial =", temperatura)
        inicio = timeit.default_timer()
        rota_refinada = funcoes.simulated_annealing(distancias, 0.8, 200 * qtdCidades, temperatura, rota)
        fim = timeit.default_timer()
        print()
        print("Rota Refinada ->", rota_refinada, "\n", "FO Refinado=", funcoes.calculaFo(distancias, rota_refinada))
        print("Tempo de execução(s):", fim - inicio)

    elif var == 9:
        print()
        print("Busca Tabu:\n")
        inicio = timeit.default_timer()
        rota_refinada, fo_refinada = funcoes.busca_tabu(distancias, qtdCidades, rota, 3, 3)
        fim = timeit.default_timer()
        print()
        print("Rota Refinada ->", rota_refinada, "\n", "FO Refinado=", fo_refinada)
        print("Tempo de execução(s):", fim - inicio)

    else:
        print("OPÇAO INVALIDA!!")
        continue
