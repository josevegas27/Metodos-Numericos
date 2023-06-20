from math import * 

def punto_fijo(funcion,p_0,exponente_precision,iteraciones):
    '''
    Descripcion: Aplica el algoritmo de punto fijo a una funcion y retorna una tabla con las iteraciones y una aproximacion de la raiz.\n
    Recibe: Una funcion (definida con el metodo lambda), la aproximacion inicial p_0, el exponente del error relativo 10^{-exponente} y las iteraciones que se realizaran.\n
    '''
    i = 0 #Contador de iteraciones 

    cota = 10**(-exponente_precision) # cota o error relativo requerido
    e_n = 1

    print('  {0:18s} {1:21s} {2:27s}'.format('i','p_n','e_n'))  #Formato de la tabla 
    print('{0:3d} {1:20} {2:24}'.format(i,p_0,e_n))             # Agragando los valores iniciales en la tabla
    i = 1
    while i<=iteraciones:
        p_1 = f(p_0)                                            # Se determina el punto fijo en cada iteracion
        e_n = abs(p_1 - p_0)/abs(p_1)                           # Se determina el error relativo del punto fijo actual respecto al anterio.
        print('{0:3d} {1:20} {2:24}'.format(i,p_1,e_n))         # Se agragan a la tabla los valores obtenidos
        if e_n < cota:                                          # Si el error relativo es menor al requerido se imprime por pantalla el punto fijo
            return f'La raiz es p_{i} = {p_1}'
        p_0 = p_1                                               # Si no, se cambia el valor inicial de la aproximacion por el siguiente
        i += 1
    return f'Se detuvo la inteacion hasta i={i-1} con p_{i-1}={p_1}'