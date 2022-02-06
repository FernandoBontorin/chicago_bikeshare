# coding: utf-8 

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
# Fefo: Iterei e imprimi 20 linhas
for i in range(20):
    print(data_list[i + 1])

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
# Fefo: Iterei e imprimi 20 elementos de sua respectiva linha
for i in range(20):
    print(data_list[i + 1][6])

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
# Fefo: Usando a interface de entrada e saida sugeridas, percorri o dataset adicionando os elementos a uma lista.


def column_to_list(data, index):
    """
    Cria uma lista com todos os elementos de uma coluna na mesma ordem do dataset
    :param data: dataset com linhas e colunas
    :param index: indice da coluna requerida
    :return: lista de elementos da coluna
    """
    column_values = []
    for i in range(len(data)):
        if data[i][index]:
            column_values.append(data[i][index])
        else:
            column_values.append("")
    return column_values

# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
# assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.
# Fefo: Não entendi exatamente se era para não criar uma função ou se era para não usar .count(), acabei criando:


def count_elements_in_list(elements_list, element):
    """
    Essa função conta a quantidade de um dado elemento em uma dada lista de elementos
    :param elements_list: lista de elementos
    :param element: elemento a ser contado
    :return: o numero de vezes que o elemento aparece na lista
    """
    count = 0
    for v in elements_list:
        if v == element:
            count = count + 1
    return count


male = count_elements_in_list(column_to_list(data_list, -2), "Male")
female = count_elements_in_list(column_to_list(data_list, -2), "Female")


# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
# assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)


def count_gender(data_list):
    """
    Conta a quantidade de generos masculinos e femininos presentes em um dataset
    :param data_list: dataset com linhas e colunas
    :return: lista com contagem ordenada de masculinos e femininos respectivamente
    """
    return [count_elements_in_list(column_to_list(data_list, -2), "Male"),
            count_elements_in_list(column_to_list(data_list, -2), "Female")]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
# assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.


def most_popular_gender(data_list):
    """
    Essa função devolve o genero mais popular ou se os 2 apresentarem a mesma população, retorna "Equal"
    :param data_list: dataset com linhas e colunas
    :return: uma string com qual genero é o mais popular ou se os dois são iguais
    """
    # nomeei algumas variaveis com o prefixo '_' para não ter o mesmo de outras fora do escopo da função
    _male = 0
    _female = 0
    for _i in range(len(data_list)):
        if data_list[i][-2]:
            if data_list[i][-2] == "Male":
                _male = male + 1
            elif data_list[i][-2] == "Female":
                _female = female + 1
    _answer = "Equal"
    genders_counts = count_gender(data_list)
    _male = genders_counts[0]
    _female = genders_counts[1]
    if _male > _female:
        _answer = "Male"
    if _female > _male:
        _answer = "Female"
    return _answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")
user_types_list = column_to_list(data_list, -3)
types = set(user_types_list)
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, [user_types_list.count(t) for t in types])
plt.ylabel('Quantidade')
plt.xlabel('Tipo de usuario')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipo de Usuario')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Existem alguns registros (linhas) que não contem valor no campo."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().
# vamos trabalhar só com inteiros para manipular com mais facilidade
trip_duration_list = list(map(int, column_to_list(data_list, 2)))
# pode ser feito a atribuir valores iterando cada elemento, mas são problemas de ordenamento
trip_duration_list.sort()
min_trip = trip_duration_list[0]
max_trip = trip_duration_list[-1]
mean_trip = 0.
median_trip = 0.
len_trip_duration_list = len(trip_duration_list)
mean_trip_sum = 0
for trip_duration in trip_duration_list:
    mean_trip_sum = mean_trip_sum + trip_duration
mean_trip = mean_trip_sum/len_trip_duration_list
"""
  Aqui me inspirei muito, mas o conceito é o seguinte, a mediana é diferente para listas pares e impares. Em impares,
  é o elemento do meio da lista ordenada, em pares, se faz uma media entre os 2 elementos no meio. Para 
  sabermos se é par eu faço um modulo de 2 (x % 2) que retorna 1 quando não é. Como o indice do python inicia em 0
  o meio é o tamanho/2 -1, quando par, preciso adicionar o elemento a frente, agora para fazer uma unica função,
  eu posso pegar o elemento usando o resultado negativo do modulo de 2, caso impar ele vai pegar o mesmo elemento e 
  como (A + A) / 2 = A

"""
median_trip = float(trip_duration_list[int(len_trip_duration_list/2)-1]
                     + trip_duration_list[int(len_trip_duration_list/2)-len_trip_duration_list % 2])/2


print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)
# Fefo: o dataset parece não ser o mesmo com o qual foi criado os gabaritos
# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
# assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
# assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
start_stations = set(column_to_list(data_list, 3))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# Fefo: o dataset parece não ser o mesmo com o qual foi criado os gabaritos
# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
# assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
#      """
#      Função de exemplo com anotações.
#      Argumentos:
#          param1: O primeiro parâmetro.
#          param2: O segundo parâmetro.
#      Retorna:
#          Uma lista de valores x.
#
#      """

input("Aperte Enter para continuar...")
# TAREFA 12
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"


def count_items(item_list: list) -> (list, list):
    """
    Essa função lista as categorias de itens e as suas respetivas quantidades.
    :param item_list: lista de itens
    :return: uma tupla contendo lista de tipos e lista com a contagem de elementos dos tipos
    """
    item_types = set(item_list)
    count_items_of_each_types = [item_list.count(t) for t in item_types]
    return item_types, count_items_of_each_types


if answer == "yes":
    # Fefo: o dataset parece não ser o mesmo com o qual foi criado os gabaritos
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    # assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------
