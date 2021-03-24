import re

def hasMutation(dna):
    bool1 = False
    bool2 = False
    columna=[]
    contador = 0
    for secuencia in dna:

        #verifica mediante expresion regular si se encuentra una secuencia 
        #de cuatro letras iguales asociadas a la mutacion, la verificación 
        # es de forma horizontal dentro de la matriz.
        if re.search("A{4}",secuencia) is not None:
            contador = contador + 1 
            bool1 = True

        elif re.search("T{4}",secuencia) is not None:
            contador = contador + 1 
            bool1 = True

        elif re.search("G{4}",secuencia) is not None:
            contador = contador + 1 
            bool1 = True

        elif re.search("C{4}",secuencia) is not None:
            contador = contador + 1 
            bool1 = True

    #verifica mediante expresion regular si se encuentra una secuencia 
    #de cuatro letras iguales asociadas a la mutacion, la verificación 
    # es de forma vertical dentro de la matriz. 
    if bool1:
        for i in range(0,6): 
            columna = [fila[i] for fila in dna]  
            StrColumnas = "".join(columna)

            if re.search("A{4}",StrColumnas) is not None:
                contador = contador + 1 
                bool2 = True

            elif re.search("T{4}",StrColumnas) is not None:
                contador = contador + 1 
                bool2 = True

            elif re.search("G{4}",StrColumnas) is not None:
                contador = contador + 1 
                bool2 = True

            elif re.search("C{4}",StrColumnas) is not None:
                contador = contador + 1 
                bool2 = True
        if bool2:
            return True
    else:
        return False
    print(contador) 


dn = ["ATGCGA", 
      "CAGTGC", 
      "TTATGT", 
      "CGAAGA", 
      "TACCCC",
      "TCATAA" ]

if (hasMutation(dn)):
    print("Existen mutaciones")
else:
    print("No existen mutaciones")    