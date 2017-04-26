#Eh possivel iterar com while tambem
# Para criar um loop, baseado em uma condicao

lista_2 = [2, 4]
index = 0

while index < len(lista_2):
    if lista_2[index]%2!=0:
        break
    index+=1
else:# Executado apenas quando o loop terminar normalmente
    print('Esta lista tem apenas numeros pares')
