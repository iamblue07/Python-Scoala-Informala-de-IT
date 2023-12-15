
#functie cu numar nedefinit de parametri care realizeaza suma parametrilor
def suma_parametri(*args): #functia poate primi prin intermediul args un numar nedefinit de parametri
    suma=0;
    for i in args:
        if (type(i)==int or type(i)==float): #daca acestia sunt in sau float le face suma in variabila suma
            suma= suma + i
    return suma
print(suma_parametri(10,15.1,16.9,11)) #exemplu de rulare

#funcție recursivă care primește ca parametru o lista cu numere întregi și returnează:
#suma totală a numerelor, suma numerelor pare, suma numerelor impare
def functie_recursiva(lista):
    if len(lista)!=0:  #daca lista nu este goala:
        suma_totala=lista[0]
        if lista[0]%2 == 0:
            suma_pare=lista[0];
            suma_impare=0;
        else:
            suma_pare=0;
            suma_impare=lista[0]
        lista.remove(lista[0]) #scoate primul element din lista
        totala, pare, impare = functie_recursiva(lista) #apeleaza recursiv ca sa parcurga urmatorul element din lista
        suma_totala+=totala
        suma_pare+=pare
        suma_impare+=impare
        return suma_totala, suma_pare, suma_impare #returneaza rezultatul
    else:
        return 0, 0, 0 #daca lista este goala, returneaza 0
print(functie_recursiva([15,21,8,10])) #exemplu de rulare

# funcție care citește de la tastatură și returnează valoarea
# dacă aceasta este un număr întreg, altfel returnează valoarea 0.
def check_intreg():
    print("Introduceti ceva:")
    try:
        x = int(input()) #incearca citirea unui intreg de la tastatura
        return x
    except ValueError: #daca nu s-a citit un intreg se va arunca exceptia ValueError
        return 0
print(check_intreg())  #apelul functiei

