# Graph Exploring
"Muchos problemas interesantes pueden resolverse mediante grafos. Si 
un grado posee demasiadas aristas o vértices puede ser imposible construirlo
explícitamente. Al ser inviable explorarlo en su totalidad podemos construir 
ciertas partes sobre la marcha, es lo que se llama *grafo implícito*, que 
mediante una descripción de sus vértices y aristas, podemos contruir partes
de él  a medida que se recorre."


# Ordenación topológica.

Dado un grafo *G<V,A>* orientado  y acíclico, un orden topológico es un orden
 lineal "<" ( menor extricto) definido sobre *V* tal que i < j => <j,i> no pertenece
  a *A*.
  
 ###  Características:
 
 - Este algoritmo recibe  *G* y devuelve una secuencia de elementos de
 *V* en orden topológico.
 
 - Mediante una búsqueda en profundidad, se va insertando cada vértice conforme
 se terminan de  explorar recursivamente sus adjyacentes.
 
 - Se asegura que cada vértice *i* precede en la secuencia a cualquier
 *j* para el que *<i,j>* pertenece a *A*.
 
 - Se representa mediante listas de adyacencia con un vector *l* de *n*
 listas.
 
 - La secuencia de salida puede representarse  mediante un vector *v* de
 *n* elementos que se rellena en orden inverso.



# Fuentes:


A. Salguero, F. Palomo, A. García, I. Medina. <br>
Diseño de Algoritmos.<br>
Universidad de Cádiz, 2016.

Narciso Martí Oliet, Yolanda Ortega Mallén y José Alberto
Verdejo López.<br>
Estructuras de datos y métodos algorítmicos: ejercicios resueltos.<br>
Prentice Hall, 2004.

Richard Neapolitan y Kumarss Naimipour.<br>
Foundations of Algorithms.<br>
4a edición, Jones and Bartlett Publishers, 2011.
