#import js
from js import document

def PolyAlexander_OnClk():
    
    #from IPython.display import display
    import sympy
    from js import VecUpDown
    from js import VD
    from js import disabled_button
    #import math
    
    #from js import DiagramKnot
    #from js import Cx, Cy

    #from sympy import Symbol
    #from sympy.matrices import Matrix
             
    #disabled_button("btn_PolyAlexander","false")
    document.getElementById("demo").innerHTML = ""; 
    #display("Calculating...", target="demo", append=True)

    NC = (len(VD)//2)   #NC = number of intersection of knot diagram; // = integer division
    dNC = 2*NC
    Var = 1

    for k in range(dNC):  #this for create the variables arc of knot
        if VecUpDown[k][0] == VecUpDown[k][2]:
            VecUpDown[k][3] = Var   #Var start with value = 1. Var is used to name the arcs. Ex. var = 'a', then var = 1 (column 1), etc...
        if VecUpDown[k][1] == VecUpDown[k][2]:  # if the seconc and third entries of VecUpDown are equals, means there was an intersection in the segment, and
            Var = Var+1                         # we must name a new variable. (then var = var+1).
            VecUpDown[k][3] = Var               # VecUpDown[3] store numbers that corresponding the variables (names of arcs), 1 <--> a, 2 <--> b, 3 <..> c, ...
        if Var == NC+1:                         # as we have NC variables, then var = NC+1, means we're back to the first variable, so VecUpDown[k][3] = 1
            VecUpDown[k][3] = 1
    # Next get the node matrix and calculate its determinant
    KnotMatrixAux = []
    for i in range(NC):   #s quare matrix NC x NC filled with zeros
        KnotMatrixAux.append([0 for j in range(NC)])

    t = sympy.Symbol('t')   # symbolic variable t
    J = sympy.Symbol('J')   # symbolic variable J,
    Li = -1                 # used to representate the i-line of matrix KnotMatrixAux

    for i in range(dNC):            # MatrixNo[i][j], line i, column j
        if VecUpDown[i][4] != 0:    # VecUpDown[i][4] store the orientation +1 or -1. VecUpDown[i][4] is used to search or verify the not used vector
            Li = Li+1               # Note that there are NC lines, but the for "for" go from 0 to dNC.
                                    # Quando o vetor oposto é usado VecUpDown[i][4] do oposto continua zero. e no futuro, pulamos este vetor, devido ao fato de ter sido usado.
            op = VecUpDown[i][5]    # retorna posicao do vetor oposto
            if VecUpDown[i][0] == VecUpDown[i][2]:  #v[1]=v[3]
                if (VecUpDown[i][4] < 0):
                    KnotMatrixAux[Li][VecUpDown[i][3] -1] = t-1   + (KnotMatrixAux[Li][VecUpDown[i][3] -1])
                    KnotMatrixAux[Li][VecUpDown[op][3]-1] = 1
                    KnotMatrixAux[Li][VecUpDown[op][3]-2] = -t    + (KnotMatrixAux[Li][VecUpDown[op][3]-2])
                else:  #quer dizer que VecUpDown[i][4] > 0
                    KnotMatrixAux[Li][VecUpDown[i][3] - 1] = t - 1 + (KnotMatrixAux[Li][VecUpDown[i][3] - 1])
                    KnotMatrixAux[Li][VecUpDown[op][3] - 1] = -t + (KnotMatrixAux[Li][VecUpDown[op][3] - 1])
                    KnotMatrixAux[Li][VecUpDown[op][3] - 2] = 1
            if VecUpDown[i][1] == VecUpDown[i][2]:  #v[2]=v[3]
                if VecUpDown[i][4] < 0:
                    KnotMatrixAux[Li][VecUpDown[i][3] - 1] = -t + (KnotMatrixAux[Li][VecUpDown[i][3] - 1])
                    KnotMatrixAux[Li][VecUpDown[i][3] - 2] = 1
                    KnotMatrixAux[Li][VecUpDown[op][3] - 1] = t-1 + (KnotMatrixAux[Li][VecUpDown[op][3] - 1])
                else:   # quer dizer que VecUpDown[i][4] > 0
                    KnotMatrixAux[Li][VecUpDown[i][3] - 1] = 1
                    KnotMatrixAux[Li][VecUpDown[i][3] - 2] = -t + (KnotMatrixAux[Li][VecUpDown[i][3] - 2])
                    KnotMatrixAux[Li][VecUpDown[op][3] - 1] = t - 1 + (KnotMatrixAux[Li][VecUpDown[op][3] - 1])
    #print(KnotMatrixAux)
    KnotMatrix = []
    for i in range(NC-1):   #matrix quadrada de ordem = (num. cruzamentos -1), preenchida com zeros, pois tem-se que deletar uma linha e uma coluna
        KnotMatrix.append([0 for j in range(NC-1)])

    for i in range(NC-1):
        for j in range(NC-1):
            KnotMatrix[i][j] = KnotMatrixAux[i][j]
    #print('Matriz do Nó Final = ', KnotMatrix) #ver matriz do nó
    ma = sympy.Matrix(KnotMatrix)
    p_t = ma.det()
    st = str(p_t)   #transforma p_t em uma string
    if  st == 'nan':   #se p_t = nan, é porque ocorreu erro no cálculo do determinante, e assim aplicar o método LU para obter o determinante
        p_t = ma.det(method='lu').simplify()  #usa o méthodo LU para o calc. do determinante
        p_t = p_t.expand()   #para expandir o polinômio, 'lu' retorna polinômio sem simplificar

    # Aqui proc para obter o polinômio de alexander a partir de P(t) = determinante da matrix quadrada de ordem (n-1)
    if p_t.subs(t, 1) == -1:  #para garantir que P(1)=1.
        p_t = -p_t
    p1 = (t**J)*p_t
    p2 = p1.subs(t, 1/t)
    p3 = p1-p2
    i = 1
    q = 1
    if p_t == 1:
        display("Knot determinant: D = " + str(1), target="demo", append=True)
        display("Alexander Polynomial: p(t) = " + str(1), target="demo", append=True)
    if p_t != 1:
        while q != 0:   #intercalando j = -i e j = i, até encontrar polinomio de alexander
            p4=(p3.subs(J, -i)).simplify()
            if p4 == 0:
                P = p1.subs(J,-i)
                display("Knot determinant: D = " + str(abs(P.subs(t, -1))), target="demo", append=True)
                display("Alexander Polynomial: p(t) = " + str(P.expand()), target="demo", append=True)
                #display("Cx = " + str(Cx), target="demo", append=True)
                #display("Cy = " + str(Cy), target="demo", append=True)
                break
            p4 = (p3.subs(J, i)).simplify()
            if p4 == 0:
                P = p1.subs(J, i)
                display("Knot determinant: D = " + str(abs(P.subs(t, -1))), target="demo", append=True)
                display("Alexander Polynomial: p(t) = " + str(P.expand()), target="demo", append=True)
                display("VecUpDown = " + str(VecUpDown), target="demo", append=True)
                break
            i = i+1
    #disabled_button("btn_PolyAlexander","false")
    return ma, VecUpDown
