import re

def hasMutation(dna):
    #bool1 , bool2
    columna=[]
    contador = 0
    for secuencia in dna:

        #verifica mediante expresion regular si se encuentra una secuencia 
        #de cuatro letras iguales asociadas a la mutacion, la verificación 
        # es de forma horizontal dentro de la matriz.
        if re.search("A{4}",secuencia) is not None:
            horizontal = re.search("A{4}",secuencia);
            print(horizontal)
            contador = contador + 1 
            bool1 = True

        elif re.search("T{4}",secuencia) is not None:
            horizontal = re.search("T{4}",secuencia);
            print(horizontal)
            contador = contador + 1 
            bool1 = True

        elif re.search("G{4}",secuencia) is not None:
            horizontal = re.search("G{4}",secuencia);
            print(horizontal)
            contador = contador + 1 
            bool1 = True

        elif re.search("C{4}",secuencia) is not None:
            horizontal = re.search("C{4}",secuencia);
            print(horizontal)
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
                horizontal = re.search("A{4}",StrColumnas);
                print(horizontal)
                contador = contador + 1 
                bool1 = True

            elif re.search("T{4}",StrColumnas) is not None:
                horizontal = re.search("T{4}",StrColumnas);
                print(horizontal)
                contador = contador + 1 
                bool1 = True

            elif re.search("G{4}",StrColumnas) is not None:
                horizontal = re.search("G{4}",StrColumnas);
                print(horizontal)
                contador = contador + 1 
                bool1 = True

            elif re.search("C{4}",StrColumnas) is not None:
                horizontal = re.search("C{4}",StrColumnas);
                print(horizontal)
                contador = contador + 1 
                bool1 = True

    print(contador) 


dn = ["ATGCGA", 
      "CAGTGC", 
      "TTATGT", 
      "TGAAGA", 
      "TACCCC",
      "TCAAAA" ]

hasMutation(dn)