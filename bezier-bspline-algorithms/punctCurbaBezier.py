def algoritm_de_Casteljau(puncte, t):
    n = len(puncte)
    temp = [puncte[i].copy() for i in range (n)]
    for l in range(1, n):
        for k in range(n-l):
            x = (1 - t) * temp[k][0] + t * temp[k + 1][0]
            y = (1 - t) * temp[k][1] + t * temp[k + 1][1]
            temp[k] = [x, y]
    return temp[0]

def derivata_de_Casteljau(puncte, t):
    n = len(puncte) - 1
    puncte_derivata = []
    for i in range(n):
        x = n * (puncte[i+1][0] - puncte[i][0])
        y = n * (puncte[i+1][1] - puncte[i][1])
        puncte_derivata.append([x, y])
    return algoritm_de_Casteljau(puncte_derivata, t)

def main():
    n = int(input("Introduceti gradul curbei: "))
    print("Introduceti punctele de control sub forma x,y: ")
    puncte = []
    for i in range(n + 1):
        x, y = map(float, input().split())
        puncte.append([x, y])
    t = float(input("Introduceti valoarea lui t ∈ [0,1]: "))

    punct_curba = algoritm_de_Casteljau(puncte, t)
    print("Punctul pe curba in functie de valoarea ", t, " este: ", punct_curba)

    derivata_curba = derivata_de_Casteljau(puncte, t)
    print("Derivata in functie de valoarea ", t, " este: ", derivata_curba)

main()