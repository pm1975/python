import random

gramy = "tak"

podane = []
wylosowane = []

while gramy == "tak":
    for i in range(6):
        takaJuzJest = 1
        podana = 0
        while takaJuzJest == 1:
            podana = int(input("Podaj liczbę numer "+str(i+1)+": "))
            takaJuzJest = 0
            for j in podane:
                if j == podana:
                    takaJuzJest = 1
        podane.append(podana)
        takaJuzJest = 1
        wylosowana = 0
        while takaJuzJest == 1:
            wylosowana = random.randint(1,50)
            takaJuzJest = 0
            for j in wylosowane:
                if j == wylosowana:
                    takaJuzJest = 1
        wylosowane.append(wylosowana)
    trafione = 0
    for z in podane:
        for j in wylosowane:
            if z == j:
                trafione = trafione + 1

    print("Twój wynik to: "+str(trafione))
    print("Wylosowane liczby: ")
    for i in wylosowane:
        print(i)
    podane.clear()
    wylosowane.clear()
    gramy = input("Czy chcesz zagrać jeszcze raz? (tak/nie) ")
