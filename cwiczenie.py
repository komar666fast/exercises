# secik = {1, 223, 13, 16, 3, 6, 27}
# print(secik,'secik')
# lista = [1, 223, 13, 16, 3, 6, 27]
# print(lista, 'lista')
# tupla = (1, 223, 13, 16, 3, 6, 27)
# print(tupla, 'tupla')
# print(type(secik))
# print(type(lista))
# print(type(tupla))
# lista.append(100)
# print((lista), 'lista + 100')
# secik2 = set(lista)
# print(secik2, 'secik2')
# print(type(secik2))
# lista.insert(2, 666)
# print(lista, 'lista + insert')
# lista2 = []
# lista2 = lista.sort()
# print(lista)
# secik.discard(223)
# print(secik)
# i = 1
# while i < 6:
#     print(i)
#     i += 1
# else:

#   print("i is no longer less than 6")
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     if x == "banana":    
#       continue
#     print(x)

# Liczby parzyste od 0 do 100
# a = []
# i = 0
# while i <= 100:
#   i += 2
#   a.append(i - 2)
# print('Liczby parzyste od 0 do 100:','\n' + str(a))
# print('')

# # Liczby nieparzyste od 0 do 100
# b = []
# i = 0
# while i < 100:
#   i += 2
#   b.append(i - 1)
# print('Liczby nieparzyste od 0 do 100:','\n' + str(b))
# b.reverse
# print(b)

# parzyste = []
# nieparzyste = []
# for i in range(0, 101):
#   if i % 2 == 0:
#     parzyste.append(i)
#   elif i % 2 != 0:
#     nieparzyste.append(i)
#   else: pass
# print(parzyste,'\n')
# print(nieparzyste)
  
# def get_even_numbers_from_list(data):
#   x = []
#   if isinstance(data, list):
#     print('Podałeś listę, OK')
#     for i in data:
#       if int(i) % 2 == 0:
#         x.append(i)
#   else:
#     print('Podaj listę')
#   return x
    


# test_data_1 = [0, 4, 3, 6]
# test_data_2 = '4'
# test_data_3 = [1, 3, 5]
# test_data_4 = [-3, 0, 9]
# test_data_5 = '247'
# print(get_even_numbers_from_list(data = test_data_5))
# x= []
# for i in test_data_5:
#       if int(i) % 2 == 0:
#         x.append(i)
# print(x)

# DODAWANIE
# A = [[1, 2], [3, 4]]
# B = [[5, 6], [7, 8]]

# C = [[15, 0], [0, 0]]
# D = [[0, 0], [0, 0]]

# for i in range(len(A)):
#   for j in range(len(A[0])):
#     print(A[i][j])

# print('dodawanie macierzy')
# for i in range(len(A)):
#   for j in range(len(A[0])):
#     C[i][j] = A[i][j] + B[i][j]
# for r in C:
#   print(r)

# MNOZENIE
# print('mnozenie macierzy')
# for k in range(len(A)):
#   for l in range(len(B[0])):
#     for m in range(len(B)):
#       print('k:', k, 'l:', l, 'm:', m)
#       print('D',D[k][l])
#       print('A',A[k][m])
#       print('B',B[m][l])
#       D[k][l] = D[k][l] + (A[k][m] * B[m][l])
#       print('---')

# A = [1, 3, 3, 5]
# wynik = [set(A)]
# print(wynik)

# for r in D:
#   print(r)

# TRANSPONOWANIE
# X = [[12,7],
#     [4 ,5],
#     [3 ,8]]

# result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]

# for r in result:
#    print(r)

# ZADANIE Z RUNNER-UP SCORE
# data = [-10, 0, 10]
# data.sort()
# print(data)
# test = dict.fromkeys(data)
# print(test)
# set_data = list(dict.fromkeys(data))[-2]
# print(set_data)

# lista = []
# for i in range(1, 500):
#     lista.append(i)

# def del_even(x):
#     odd_list = []
#     for i in x:
#         if i % 2 != 0:
#             odd_list.append(i)
#     return odd_list
# print(lista)
# print(del_even(lista))