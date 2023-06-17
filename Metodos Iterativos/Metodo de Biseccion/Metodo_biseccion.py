import pandas as pd

def biseccion(f,a ,b, expon, n, interaciones):
    i = 1
    p_anterior = a
    error_relativo_aproximado = 10**(-expon)
    p = (a + b)/2
    e_a2 = 0
    diccionario = {'i':[],'a_n':[],'b_n':[],'p_n':[],'f(p_n)':[],'e_r':[]}

    while (i<= interaciones):
        c = f(p)
        e_a2 = abs((p_anterior - p)/p)
        

        diccionario['i'].append(i)
        diccionario['a_n'].append(round(a,n))
        diccionario['b_n'].append(round(b,n))
        diccionario['p_n'].append(round(p,n))
        diccionario['f(p_n)'].append(round(c,n))
        diccionario['e_r'].append(round(e_a2,n+2))

        frame = pd.DataFrame(diccionario, dtype=str )

        if (c == 0):
            print(f'La raiz es p{i} = {round(p,n)}')
            return frame

        if (e_a2)<error_relativo_aproximado:
            print(f'La raiz aproximada es p{i}={round(p,n)}')
            return frame

        if f(a)*c<0:
            a = a
            b = p
        elif f(a)*c>0:
            a = p
            b = b 
        p_anterior = p
        p = (a + b)/2
        i += 1

    print(f'No se ha alcanzado la precisión requerida hasta i={i-1} obteniendo p_{i-1}={round(p,n)}')
    return frame