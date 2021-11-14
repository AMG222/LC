"""Ejercicio 1"""
def dic1(x):
    L = [y.split("/") for y in x.split()]
    lista = {}
    for i in L:
        if i[1] in lista:
            lista[i[1]] += 1
        else:
            lista[i[1]] = 1
    return sorted(lista), lista

"""Coste 3.5*n+n*log2(n) -> O(n)"""

"""Ejercicio 2"""
def dic2(x):
    L = [y.split("/") for y in x.split()]
    listaPa = {}
    listaCat = {} 
    """Map palabra->categorias->num categorias"""
    for i in L:
        pa = i[0].lower()
        cat = i[1]
        if pa in listaPa:
            listaPa[pa] += 1
        else:
            listaPa[pa] = 1
        
        if pa not in listaCat:
            listaCat[pa] = {}
        if cat in listaCat[pa]:
            listaCat[pa][cat] += 1
        else:
            listaCat[pa][cat] = 1
    return sorted(listaPa), listaPa, listaCat

"""Coste 4*n+n*log2(n) -> O(n)"""

"""Ejercicio 3"""
def dic3(x):
    L = [y.split("/") for y in x.split()]
    tuplas = {}
    st = "('<S>', '" + L[0][1] + "')"
    if st in tuplas:
      tuplas[st] += 1
    else:
      tuplas[st] = 1
    for i in range(0,len(L)):
      if i != len(L)-1:
        cat0 = L[i][1]
        cat1 = L[i+1][1]
        st = "('" + cat0 + "', '" + cat1 + "')"
        if st in tuplas:
          tuplas[st] += 1
        else:
          tuplas[st] = 1
      else:
        st = "('" + cat0 + "', '</S>')"
        if st in tuplas:
          tuplas[st] += 1
        else:
          tuplas[st] = 1
    return tuplas
      
      

"""Coste 4*n -> O(n)"""

"""Ejercicio 4"""

def prob(w, cadena):
    llaves1, lista1 = dic1(cadena)
    llaves2, listaPa, listaCat = dic2(cadena)
    for i in listaCat[w]:
      print("P(", i, "|", w, ") = ", listaCat[w][i]/listaPa[w])
    for i in listaCat[w]:
      print("P(", w, "|", i, ") = ", listaCat[w][i]/lista1[i])
"""Coste 8*n+2*n*log2(n) -> O(n)"""

cadena ="El/DT perro/N come/V carne/N de/P la/DT carnicerÃ­a/N y/C de/P la/DT nevera/N y/C canta/V el/DT la/N la/N la/N ./Fp"
llaves, lista = dic1(cadena)
for i in llaves:
    print(i, lista[i])

llaves, listaPa, listaCat = dic2(cadena)
for i in llaves:
    print(i, listaPa[i], end = ' ')
    for j in listaCat[i]:
      print(j, listaCat[i][j], end = ' ')
    print('')

lista = dic3(cadena)
for i in lista:
  print(i, lista[i])
 
prob("la", cadena)