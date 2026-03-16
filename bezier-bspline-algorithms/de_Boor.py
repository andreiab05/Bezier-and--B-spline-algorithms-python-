import sys

def intervalNoduri(noduri, t):
    n = len(noduri) - 4
    for i in range(3, n + 1):
        if noduri[i] <= t <= noduri[i + 1]:
            return i
    return n


def de_Boor(k, grad, noduri, puncte, t):
    d = [puncte[i + k - grad].copy() for i in range(grad + 1)]

    for r in range(1, grad + 1):
        for i in range(grad - r + 1):
            denominator = noduri[i + k + 1] - noduri[i + k - grad + r]
            if abs(denominator) < 1e-10:
                alpha = 0
            else:
                alpha = (t - noduri[i + k - grad + r]) / denominator
            d[i] = [
                (1 - alpha) * d[i][0] + alpha * d[i + 1][0],
                (1 - alpha) * d[i][1] + alpha * d[i + 1][1]
            ]

    return d[0]

def main():
    print("Introduceti punctele de control sub forma x,y: ")
    puncte = []
    for i in range(5):
        x, y = map(float, input().split())
        puncte.append([x, y])
    print("Introduceti cele 9 noduri: ")
    noduri = []
    for i in range(9):
        T = float(input())
        noduri.append(T)

    if not (noduri[0] == noduri[1] == noduri[2]):
        print("Primele 3 noduri trebuie sa fie egale!")
        sys.exit()

    if not (noduri[6] == noduri[7] == noduri[8]):
        print("Ultimele 3 noduri trebuie sa fie egale!")
        sys.exit()

    for i in range(1, len(noduri)):
        if noduri[i] < noduri[i-1]:
            print("Eroare: Nodurile trebuie sa fie in ordine crescatoare!")
            sys.exit()

    t = int(input("Parametrul t: "))
    k = intervalNoduri(noduri, t)
    r = de_Boor(k, 3, noduri, puncte, t)

    print(f"Punctul de pe curba in parametrul t este: ({r[0]}, {r[1]})")

main()

#testare sa fie crescatoare
