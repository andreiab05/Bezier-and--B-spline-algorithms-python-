import math
import numpy as np

def translation(tx, ty):
    return np.array([
        [1,0,tx],
        [0,1,ty],
        [0,0,1]
    ], dtype = float)

def rotation(a,b):
    cos_t = b / math.sqrt(a*a + b*b)
    sin_t = -a / math.sqrt(a*a + b*b)
    return np.array([
        [cos_t, -sin_t, 0],
        [sin_t, cos_t, 0],
        [0, 0, 1]
    ], dtype = float)

def reflection0x():
    return np.array([
        [1,0,0],
        [0,-1,0],
        [0,0,1]
    ], dtype = float)

def reflection0y():
    return np.array([
        [-1,0,0],
        [0,1,0],
        [0,0,1]
    ], dtype = float)

def main():
    mod = input("Alegeti modul de introducere a dreptei:\n1. Coeficientii dreptei ax + by + c =0.\n2.Punct (x,y) si vector director (vx,vy):\n")
    if mod == "1":
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
    elif mod == "2":
        x = float(input("x0 = "))
        y = float(input("y0 = "))
        vx = float(input("vx = "))
        vy = float(input("vy = "))

        a = -vy
        b = vx
        c = -(a * x + b * y)

    n = int(input("Introduceti numarul de varfuri al poligonului: "))
    coordonate = []
    while n < 1:
        n = int(input("Numar invalid, introduceti alt numar de varfuri: "))
    for i in range(n):
        x, y = map(float, input().split())
        coordonate.append([x, y, 1])

    print("Matricile transformarilor sunt: \n")

    if a == 0 and c == 0:
        print("Dreapta trece prin origine.\n")
        T = reflection0x()
        print(T)
        print("\n")

    elif b == 0 and c == 0:
        print("Dreapta trece prin origine.\n")
        T = reflection0y()
        print(T)
        print("\n")

    elif a == 0:
        print("Dreapta este orizontala.\n")
        T = translation(0, -c/b) @ reflection0x() @ translation(0, c/b)
        print(translation(0, -c/b))
        print("\n")
        print(reflection0x())
        print("\n")
        print(translation(0, c/b))
        print("\n")

    elif b == 0:
        print("Dreapta este verticala.\n")
        T = translation(-c/a, 0) @ reflection0y() @ translation(c/a, 0)
        print(translation(-c/a, 0))
        print("\n")
        print(reflection0y())
        print("\n")
        print(translation(c/a, 0))
        print("\n")

    else:
        print("Dreapta este oblica.\n")
        T = translation(0, -c/b) @ rotation(a, b) @ reflection0x() @ np.linalg.inv(rotation(a,b)) @ translation(0, c/b)
        print(translation(0, -c / b))
        print("\n")
        print(rotation(a, b))
        print("\n")
        print(reflection0x())
        print("\n")
        print(np.linalg.inv(rotation(a,b)))
        print("\n")
        print(translation(0, c / b))
        print("\n")

    before = np.array(coordonate).T
    after = T @ before

    print("Matricea transformarii compuse:\n")
    print(T)

    print("\nMatricea coordonatelor omogene ale varfurilor imaginii poligonului dat:\n")
    print(after)

main()