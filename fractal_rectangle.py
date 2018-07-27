import graphics as gr

wingow = gr.GraphWin("Main Wind", 600, 600)

alpha= 0.1

def new_point(A,B):
    return (A[0]*(1-alpha) + B[0]*alpha, A[1]*(1-alpha) + B[1]*alpha)

def fractal_rectangle(A,B,C,D, deep=10):
    if deep < 1:
        return
    pairs_points = [(A, B), (B,C), (C,D), (D,A)]
    for M, N in pairs_points:
        gr.Line(gr.Point(*M), gr.Point(*N)).draw(wingow)
    A1 = new_point(A,B)
    B1 = new_point(B,C)
    C1 = new_point(C,D)
    D1 = new_point(D,A)
    fractal_rectangle(A1,B1,C1,D1, deep-1)

A = (100,100)
B = (500,100)
C = (500,500)
D = (100,500)
deep = 100

fractal_rectangle(A,B,C,D, deep)
