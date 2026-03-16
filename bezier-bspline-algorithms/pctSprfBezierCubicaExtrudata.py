import re
import math

def casteljau_curba(puncte, t):
    tmp = [p[:] for p in puncte]
    n = len(tmp) - 1
    dim = len(tmp[0])

    for r in range(1, n + 1):
        for i in range(0, n - r + 1):
            out = [0.0] * dim
            for d in range(dim):
                out[d] = (1 - t) * tmp[i][d] + t * tmp[i + 1][d]
            tmp[i] = out
    return tmp[0]

def puncte_din_linie(linie):
    pct = []
    for group in re.findall(r"\(([^)]+)\)", linie):
        coords = [float(x) for x in group.split(",")]
        pct.append(coords)
    return pct

def lerp(a, b, t):
    return [(1 - t) * a[i] + t * b[i] for i in range(len(a))]

def norma(v):
    return math.sqrt(sum(x * x for x in v))

def main():
    with open("exempluDate4", "r") as f:
        n = int(f.readline().strip())  # gradul curbei (cubic => 3)

        linie_puncte = f.readline().strip()  # P0..P3 pe o singura linie
        P = puncte_din_linie(linie_puncte)

        delta = float(f.readline().strip())  # δ > 0

        linie_versor = f.readline().strip()  # (vx,vy,vz)
        v_list = puncte_din_linie(linie_versor)
        if len(v_list) != 1:
            raise ValueError("Versorul trebuie dat ca un singur punct: (vx,vy,vz).")
        v = v_list[0]

        u0 = float(f.readline().strip())  # u0 in [0,1]
        v0 = float(f.readline().strip())  # v0 in [0,1]

    if n != 3:
        raise ValueError("Suprafata este extrudata dintr-o curba Bezier cubica, deci n trebuie sa fie 3.")
    if len(P) != 4:
        raise ValueError("Trebuie exact 4 puncte de control P0..P3 pentru curba cubica.")
    if delta <= 0:
        raise ValueError("delta trebuie sa fie > 0.")
    if not (0.0 <= u0 <= 1.0 and 0.0 <= v0 <= 1.0):
        raise ValueError("u0 si v0 trebuie sa fie in [0,1].")

    nv = norma(v)
    if abs(nv - 1.0) > 1e-7:
        raise ValueError(f"v trebuie sa fie versor (norma 1).")

    row0 = [p[:] for p in P]
    row1 = [[P[i][0] + delta * v[0], P[i][1] + delta * v[1], P[i][2] + delta * v[2]] for i in range(4)]

    Q0 = casteljau_curba(row0, u0)
    Q1 = casteljau_curba(row1, u0)
    R = lerp(Q0, Q1, v0)

    print(f"r(u0,v0) pentru u0={u0}, v0={v0} este:", tuple(R))

main()