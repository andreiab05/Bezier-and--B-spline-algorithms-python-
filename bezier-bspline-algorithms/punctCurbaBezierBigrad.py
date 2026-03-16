import re

def algoritm_de_Casteljau(puncte, t):
    n = len(puncte)
    temp = [puncte[i].copy() for i in range (n)]
    for l in range(1, n):
        for k in range(n-l):
            for d in range(len(temp[k])):
                temp[k][d] = (1 - t) * temp[k][d] + t * temp[k + 1][d]
    return temp[0]

def suprf_bezier(suprf, u, v):
    puncte_rand = []
    for rand in suprf:
        puncte_rand.append(algoritm_de_Casteljau(rand, v))

    return algoritm_de_Casteljau(puncte_rand, u)

def main():
    with open("exempluDate2","r") as f:
        n = int(f.readline())
        m = int(f.readline()) #gradul curbei

        linie_puncte = f.readline().strip() #punctele de control pe o singura linie
        puncte = []
        for group in re.findall(r"\(([^)]+)\)", linie_puncte):
            coords = [float(x) for x in group.split(",")]
            puncte.append(coords) #punctele de control

        u = float(f.readline().strip()) # u ∈ [0,1]
        v = float(f.readline().strip()) # v ∈ [0,1]

    suprf = []
    index = 0
    for i in range(n + 1):
        rand = []
        for j in range(m + 1):
            rand.append(puncte[index])
            index += 1
        suprf.append(rand)

    p = suprf_bezier(suprf, u, v)
    print(f"r(u,v) pentru u={u}, v={v} este:", tuple(p))

main()