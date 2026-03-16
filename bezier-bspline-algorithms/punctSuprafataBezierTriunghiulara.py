import re

def algoritm_de_Casteljau_triunghiular(puncte, n, u, v, w):
    lenPct = len(puncte[0])

    index = 0
    P = {}
    for i in range(n + 1):
        for j in range(n - i + 1):
            P[(i, j)] = puncte[index][:]
            index += 1

    current = P
    for r in range(n, 0, -1):
        next = {}
        for i in range(r):
            for j in range(r - i):
                a = current[(i + 1, j)]
                b = current[(i, j + 1)]
                c = current[(i, j)]
                out = [0.0] * lenPct
                for d in range(lenPct):
                    out[d] = u * a[d] + v * b[d] + w * c[d]
                next[(i, j)] = out
        current = next
    return current[(0, 0)]

def main():
    with open("exempluDate3","r") as f:
        n = int(f.readline()) #gradul curbei

        fisierPuncte = f.readline().strip() #punctele de control pe o singura linie
        puncte = []
        for group in re.findall(r"\(([^)]+)\)", fisierPuncte):
            coords = [float(x) for x in group.split(",")]
            puncte.append(coords) #punctele de control

        u = float(f.readline().strip()) # u ∈ [0,1]
        v = float(f.readline().strip()) # v ∈ [0,1]
        w = float(f.readline().strip()) # w ∈ [0,1]

    s = u + v + w

    if abs(s - 1.0) > 1e-7:
        raise ValueError(f"u+v+w trebuie să fie 1. Acum este {s}.")

    p = algoritm_de_Casteljau_triunghiular(puncte, n, u, v, w)
    print(f"r(u,v,w) pentru u={u}, v={v}, w={w} este:", tuple(p))

main()