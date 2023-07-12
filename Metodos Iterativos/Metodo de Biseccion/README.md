---
# Método de Bisección

El método de bisección es un método numérico para hallar ceros de una función en un intervalo específico. 

Las condiciones para hallar raices de una función $ f $ en un intervalo $[a,b]$ con el método de Bisección son
 
- $f$ debe ser continua en $(a,b)$.
- $f$ debe ser continua por la derecha en $x = a$ y por la izquierda en $x = b$.
- $f$ debe tener signos opuestos en los extremos del intervalo, es decir, $f(a)f(b) < 0$.

En el archivo Metodo_biseccion.ipynb construimos el código que implementa el algoritmo de bisección para funciones que cumplen con las condiciones anteriores. 

El archivo Metodo_biseccion.py ejecuta éste algoritmo, que tiene una función de python llamada **biseccion** que requiere los siguientes parámetros

- Una función f predefinida (con el método *lambda*) en función de una sola variable,
- $a$ y $b$ que son los extremos del intervalo,
- Exponente $n$ del error relativo $10^{-n}$ de la aproximación,
- La precisión de los resultados,
- El número de iteraciones.