from main import main

def minmax(mymas):
    global j, i, n, s, t, c, k, m
    for k in range(n):
        m = k
        i = k + 1
        while i < len(mymas):
            if mymas[i] < mymas[m]:
                m = i
            i += 1
        t = mymas[k]
        mymas[k] = mymas[m]
        mymas[m] = t

        if c == TRUE:
            for s in range(n):
                print(maymas[s])


def pyz(mymas):
    global j, i, n, s, t, c, k, m
    while t < n:
        for i in range(1, n + 1):
            if mymas[i] > mymas[i + 1]:
                mymas[i], mymas[i + 1] = mymas[i + 1], mymas[i]
        t += 1

        if c == TRUE:
            for s in range(n):
                print(maymas[s])


def vstav(mymas):
    global j, i, n, s, t, c, k, m
    for j in range(2, n):
        key = mymas[j]
        i = j - 1
        while (i > 0) and (mymas[i] > key):
            mymas[i + 1] = mymas[i]
            i = i - 1
        mymas[i + 1] = key

        if c == TRUE:
            for s in range(n):
                print(maymas[s])


def sli(mymas):
    global j, i, n, s, t, c, k, m
    while j > 1:
        max = mymas[1]
        id_max = 1
        for i in range(2, j):
            if mymas[i] > max:
                max = mymas[i]
                id_max = i
        mymas[id_max] = mymas[j]
        mymas[j] = max
        j = j - 1
