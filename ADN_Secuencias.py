import re

def hasMutation(dna):

    columna=[]
    cout_mutations = 0;
    cout_no_mutations = 6;  
    for secuencia in dna:

        #verifica mediante expresion regular si se encuentra una secuencia 
        #de cuatro letras iguales asociadas a la mutacion, la verificación 
        # es de forma horizontal dentro de la matriz.
        if re.search("A{4}",secuencia) is not None:
            print(re.search("A{4}",secuencia))
            cout_mutations = cout_mutations + 1 

        elif re.search("T{4}",secuencia) is not None:
            print(re.search("T{4}",secuencia))
            cout_mutations = cout_mutations + 1 

        elif re.search("G{4}",secuencia) is not None:
            print(re.search("G{4}",secuencia))
            cout_mutations = cout_mutations + 1 

        elif re.search("C{4}",secuencia) is not None:
            print(re.search("C{4}",secuencia))
            cout_mutations = cout_mutations + 1 
            

    #verifica mediante expresion regular si se encuentra una secuencia 
    #de cuatro letras iguales asociadas a la mutacion, la verificación 
    # es de forma vertical dentro de la matriz. 
    
    for i in range(0,6):
        columna = [fila[i] for fila in dna]  
        StrColumnas = "".join(columna)

        if re.search("A{4}",StrColumnas) is not None:
            print(StrColumnas)
            cout_mutations = cout_mutations + 1 

        elif re.search("T{4}",StrColumnas) is not None:
            print(StrColumnas)
            cout_mutations = cout_mutations + 1 

        elif re.search("G{4}",StrColumnas) is not None:
            print(StrColumnas)
            cout_mutations = cout_mutations + 1 

        elif re.search("C{4}",StrColumnas) is not None:
            print(re.search("C{4}",secuencia))
            print('Entra')
            print(StrColumnas)
            cout_mutations = cout_mutations + 1 

    if cout_mutations >= 2:
        cout_no_mutations = cout_no_mutations - cout_mutations
        return True, cout_mutations, cout_no_mutations
    else:
        return False,0,6


"""
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

"""