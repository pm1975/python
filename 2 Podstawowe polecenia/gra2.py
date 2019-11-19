import random

gramy = "tak"

podane = []
wylosowane = []

while gramy == "tak":
    for i in range(6):

        takaJuzJest = 0
        podana = 0;
        while takaJuzJest == 0:
            podana = int(input("Podaj liczbę numer "+str(i+1)+": "))
            znalazlem = 0
            for i in podane:
                if i == podana:
                    znalazlem = 1;
            takaJuzJest = znalazlem;
        podane.append(podana)
        takaJuzJest = 0
        wylosowana = 0;
        while takaJuzJest == 0:
            wylosowana = random.randint(1,50)
            znalazlem = 0
            for i in wylosowane:
                if i == wylosowana:
                    znalazlem = 1;
            takaJuzJest = znalazlem;
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
