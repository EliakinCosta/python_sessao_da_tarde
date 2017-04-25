lista = [1, 2, 3, 4, 5, 6, 7, 8]

nova_lista = []

for elemento in lista:
    if elemento%2==0:
        nova_lista.append(elemento)
        
print(nova_lista)
