N=int(input())
A=list(map(int,input().split()))

numero_mas_cercano=A[0]
distancia_cercana=A[0]

for numero in A:
        distancia_act=abs(numero)
        if distancia_act < distancia_cercana:
            distancia_cercana = distancia_act
            numero_mas_cercano=numero

print(numero)
        

    