def borde(l,m,n):
    pass

def laberinto(l, m, n ,i ,j):

    if l[i][j] ==" ":



        if borde(l,m ,n):
            s = True

        else:
            l[i][j] = "V"
            s, l = laberinto(l,m ,n ,i -1 ,j) or \
                laberinto(l, m , n, i +1 , j) or \
                laberinto(l , m , n, i , j-1) or \
                laberinto(l , m , n , i, j -1)

        if s:
            l[i][j] = "S"
    else:
        s = False

    return s,l






