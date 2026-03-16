import re
import numpy as np
import matplotlib.pyplot as plt

def algoritm_de_Casteljau_rational(puncte, ponderi, t):
    N = len(puncte) #n + 1
    b = [list(p) for p in puncte]
    w = ponderi.copy()
    for j in range(1, N):
        for i in range(N - j):
            w_ij = (1 - t) * w[i] + t * w[i + 1]

            b[i][0] = (1 - t) * w[i] / w_ij * b[i][0] + t * w[i + 1] / w_ij * b[i + 1][0]
            b[i][1] = (1 - t) * w[i] / w_ij * b[i][1] + t * w[i + 1] / w_ij * b[i + 1][1]

            w[i] = w_ij

    return b[0]

def afisare_grafica(puncte, ponderi, t, punct_curba):
    ts = np.linspace(0.0, 1.0, 200)
    curba = [algoritm_de_Casteljau_rational(puncte,ponderi,t) for t in ts]

    xs = [p[0] for p in curba]
    ys = [p[1] for p in curba]

    control_x = [p[0] for p in puncte]
    control_y = [p[1] for p in puncte]

    plt.figure()

    plt.plot(control_x, control_y, marker = 'o', linestyle = "--", label="Poligon de control")

    plt.plot(xs, ys, label = "Curba Bezier rationala")

    plt.scatter([punct_curba[0]], [punct_curba[1]], label=f"r(t={t})")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.axis("equal")
    plt.grid(True)

    plt.show()

def main():
    with open("exempluDate","r") as f:
        n = int(f.readline()) #gradul curbei

        linie_puncte = f.readline().strip() #punctele de control pe o singura linie
        puncte = []
        for x, y in re.findall(r"\(([^,]+),([^)]+)\)", linie_puncte): #despartirea punctelor sub forma (x,y)
            puncte.append((float(x), float(y))) #punctele de control

        ponderi = list(map(float, f.readline().split())) #ponderi

        t = float(f.readline().strip()) # t ∈ [0,1]

    punct_curba = algoritm_de_Casteljau_rational(puncte, ponderi, t)
    print("Punctul pe curba in functie de valoarea ", t, " este: ", punct_curba)

    afisare_grafica(puncte, ponderi, t, punct_curba)

main()