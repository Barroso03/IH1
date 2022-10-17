def tupla():
    tupla = ("I",)
    print(tupla)
    print(type(tupla))
  # mete "r", "o", "n", "h", "a", "c", "k" en la tupla
    print("Para agregar elementos a la tupla, se debe crear una lista, agregar los elementos y luego convertir la lista en tupla")
    tupla= list(tupla)
    tupla.append("r")
    tupla.append("o")
    tupla.append("n")
    tupla.append("h")
    tupla.append("a")
    tupla.append("c")
    tupla.append("k")
    tupla= tuple(tupla)
    print(tupla)
  
    tupla= list(tupla)
    tupla1= tupla[0:4]
    tupla2= tupla[4:8]
    tupla1= tuple(tupla1)
    tupla2= tuple(tupla2)
    print("la tupla1:",tupla1)
    print("la tupla2:",tupla2)
    tupla3= list(tupla1)
    tupla3.extend(tupla2)
    tupla3= tuple(tupla3)
    print("La tupla3:",tupla3)
  # cuenta los datos de la tupla1
    print("La tupla1 tiene",len(tupla1),"elementos")
    # cuenta los datos de la tupla2
    print("La tupla2 tiene",len(tupla2),"elementos")
    # cuenta los datos de la tupla3
    print("La tupla3 tiene",len(tupla3),"elementos")
  # mira si la suma de los elementos de la tupla1 y la tupla2 es igual a la tupla3

    if len(tupla1)+len(tupla2)==len(tupla3):
        print("La suma de los elementos de la tupla1 y la tupla2 es igual a la tupla3")
    else:
        print("La suma de los elementos de la tupla1 y la tupla2 no es igual a la tupla3")
    # dime el indice de h en la tupla3
    print("El indice de h en la tupla3 es:",tupla3.index("h"))
    #Now, use a FOR loop to check whether each letter in the following list is present in tup3:
    #How many times does each letter in letters appear in tup3?
    lista= ["a", "e", "i", "o", "u"]
    print("¿Estan la a,e,i,o,u en la tupla3?")
    for i in lista:
        if i in tupla3:
            print("Si esta",i,"en la tupla3")
        else:
            print("No esta",i,"en la tupla3")
    #How many times does each letter in letters appear in tup3?
    print("¿Cuantas veces aparece cada letra en la tupla3?")
    for i in lista:
        print("La letra",i,"aparece",tupla3.count(i),"veces en la tupla3")

  
    


tupla()

