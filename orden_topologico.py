def profundidad(l, i, m, v,k):
    m[i] = True

    for i in l:
        if not m[i]:
            profundidad(l,i,m,v,k)

    v[k] = i
    k = k -1


def orden_topologico(lista_adyacencia, numero_vertices):

    visitados =[False]*numero_vertices
    solucion =[0] *numero_vertices

    k = numero_vertices

    for i in range(0, numero_vertices):

        if not visitados[i]:
            profundidad(lista_adyacencia, i, visitados,solucion, k)

    return solucion








if __name__ == '__main__':
    # TODO implement
  pass