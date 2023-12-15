lista=[7,8,9,2,3,1,4,10,5,6]
print("Lista:",lista)


lista_ascendenta=lista.copy()
lista_ascendenta.sort()
print("Lista ascendenta:", lista_ascendenta)


lista_descendenta=lista.copy()
lista_descendenta.sort(reverse=True)
print("Lista descendenta:",lista_descendenta)


print("Numerele cu indici pari din lista:",lista[0::2])
print("Numerele cu indici impari din lista:", lista[1::2])

print("Numerele multiplu de 3 din lista:")
for i in lista:
    if i%3==0:
        print(i)