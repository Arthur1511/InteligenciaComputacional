import funcoes
import timeit



inicio = timeit.default_timer()

# distancias, qtdCidades = funcoes.calcularDistancias("A280.txt")
distancias, qtdCidades = funcoes.lerDados("cv10.txt")

# for i in range(qtdCidades):

rota, fo = funcoes.vizinhoMaisProximo(distancias, qtdCidades, 4, 0.5)

# rota, fo = funcoes.insercaoMaisBarata(distancias, qtdCidades)

rota_refinada, fo_refinada = funcoes.descida(distancias, rota, qtdCidades, fo)

print("Rota ->", rota, "\n", "FO=", fo)
print("Rota Refinada ->", rota_refinada, "\n", "FO Refinado=", fo_refinada)
fim = timeit.default_timer()

# print("Tempo de execução(s):", fim-inicio)