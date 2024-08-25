from js import document

def PolyAlexander_OnClk():
    
    import sympy
    from js import VecUpDown
    from js import VD
    from js import disabled_button
    
    document.getElementById("demo").innerHTML = ""; 

    NC = (len(VD)//2)   #NC = number of intersection of knot diagram
    dNC = 2*NC
    Var = 1

    for k in range(dNC):  #this for create the variables arc of knot
        if VecUpDown[k][0] == VecUpDown[k][2]:
            VecUpDown[k][3] = Var   #Var start with value = 1. Var is used to name the arcs. Ex. var = 'a', then var = 1 (column 1), etc...
        if VecUpDown[k][1] == VecUpDown[k][2]:  # if the second and third entries of VecUpDown are equals, means there was an intersection in the segment, and
            Var = Var+1                         # we must name a new variable. (then var = var+1).
            VecUpDown[k][3] = Var               # VecUpDown[3] store numbers that corresponding the variables (names of arcs), 1 <--> a, 2 <--> b, 3 <..> c, ...
        if Var == NC+1:                         # as we have NC variables, then var = NC+1, means we're back to the first variable, so VecUpDown[k][3] = 1
            VecUpDown[k][3] = 1
    # Next get the knot matrix and calculate its determinant
    KnotMatrixAux = []
    for i in range(NC):   #s quare matrix NC x NC filled with zeros
        KnotMatrixAux.append([0 for j in range(NC)])

    t = sympy.Symbol('t')   # symbolic variable t
    J = sympy.Symbol('J')   # symbolic variable J,
    Li = -1                 # used to representate the i-line of matrix KnotMatrixAux

    for i in range(dNC):            # MatrixNo[i][j], line i, column j
        if VecUpDown[i][4] != 0:    # VecUpDown[i][4] store the orientation +1 or -1. VecUpDown[i][4] is used to search or verify the not used vector
            Li = Li+1               # Note that there are NC lines, but the for "for" go from 0 to dNC.
            op = VecUpDown[i][5]    
            if VecUpDown[i][0] == VecUpDown[i][2]:  #v[1]=v[3]
                if (VecUpDown[i][4] < 0):
                    KnotMatrixAux[Li][VecUpDown[i][3] -1] = t-1   + (KnotMatrixAux[Li][VecUpDown[i][3] -1])
                    KnotMatrixAux[Li][VecUpDown[op][3]-1] = 1
                    KnotMatrixAux[Li][VecUpDown[op][3]-2] = -t    + (KnotMatrixAux[Li][VecUpDown[op][3]-2])
                else:  
                    KnotMatrixAux[Li][VecUpDown[i][3] - 1] = t - 1 + (KnotMatrixAux[Li][VecUpDown[i][3] - 1])
                    KnotMatrixAux[Li][VecUpDown[op][3] - 1] = -t + (KnotMatrixAux[Li][VecUpDown[op][3] - 1])
                    KnotMatrixAux[Li][VecUpDown[op][3] - 2] = 1
            if VecUpDown[i][1] == VecUpDown[i][2]:  #v[2]=v[3]
                if VecUpDown[i][4] < 0:
                    KnotMatrixAux[Li][VecUpDown[i][3] - 1] = -t + (KnotMatrixAux[Li][VecUpDown[i][3] - 1])
                    KnotMatrixAux[Li][VecUpDown[i][3] - 2] = 1
                    KnotMatrixAux[Li][VecUpDown[op][3] - 1] = t-1 + (KnotMatrixAux[Li][VecUpDown[op][3] - 1])
                else:   
                    KnotMatrixAux[Li][VecUpDown[i][3] - 1] = 1
                    KnotMatrixAux[Li][VecUpDown[i][3] - 2] = -t + (KnotMatrixAux[Li][VecUpDown[i][3] - 2])
                    KnotMatrixAux[Li][VecUpDown[op][3] - 1] = t - 1 + (KnotMatrixAux[Li][VecUpDown[op][3] - 1])
    
    KnotMatrix = []
    for i in range(NC-1):  
        KnotMatrix.append([0 for j in range(NC-1)])

    for i in range(NC-1):
        for j in range(NC-1):
            KnotMatrix[i][j] = KnotMatrixAux[i][j]
    
    ma = sympy.Matrix(KnotMatrix)
    p_t = ma.det()
    st = str(p_t)  
    if  st == 'nan':   
        p_t = ma.det(method='lu').simplify()  #LU method to calc. determinant
        p_t = p_t.expand()   

    if p_t.subs(t, 1) == -1: 
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
        while q != 0:   
            p4=(p3.subs(J, -i)).simplify()
            if p4 == 0:
                P = p1.subs(J,-i)
                display("Knot determinant: D = " + str(abs(P.subs(t, -1))), target="demo", append=True)
                display("Alexander Polynomial: p(t) = " + str(P.expand()), target="demo", append=True)
                break
            p4 = (p3.subs(J, i)).simplify()
            if p4 == 0:
                P = p1.subs(J, i)
                display("Knot determinant: D = " + str(abs(P.subs(t, -1))), target="demo", append=True)
                display("Alexander Polynomial: p(t) = " + str(P.expand()), target="demo", append=True)
                display("VecUpDown = " + str(VecUpDown), target="demo", append=True)
                break
            i = i+1
    return ma, VecUpDown
