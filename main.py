from defs import defs
#n - аКаОаЛ-аВаО баЛаЕаМаЕаНбаОаВ аВ аМаАббаИаВаЕ
#mymas - баЛаЕаМаЕаНб аМаАббаИаВаА

# def minmax(mymas):
#     global j,i,n,s,t,c,k,m
#     for k in range(n ):
#         m = k
#         i = k + 1
#         while i < len(mymas):
#             if mymas [i] < mymas[m]:
#                 m = i
#             i += 1
#         t = mymas[k]
#         mymas[k] = mymas[m]
#         mymas[m] = t
#
#         if c==TRUE:
#                 for s in range (n):
#                     print (maymas[s])
#
# def pyz(mymas):
#     global j,i,n,s,t,c,k,m
#     while t < n:
#          for i in range(1,n+1):
#               if mymas[i] > mymas[i+1]:
#                    mymas[i],mymas[i+1] = mymas[i+1],mymas[i]
#          t += 1
#
#          if c==TRUE:
#                 for s in range (n):
#                     print (maymas[s])
#
#
# def vstav(mymas):
#     global j,i,n,s,t,c,k,m
#     for j in range (2,n):
#         key = mymas[j]
#         i = j - 1
#         while (i > 0) and (mymas[i] > key):
#              mymas[i+1] = mymas[i]
#              i = i - 1
#         mymas[i+1] = key
#
#         if c==TRUE:
#                 for s in range (n):
#                     print (maymas[s])
#
# def sli (mymas):
#     global j,i,n,s,t,c,k,m
#     while j > 1:
#             max = mymas[1]
#             id_max = 1
#             for i in range(2,j):
#                 if mymas[i] > max:
#                     max = mymas[i]
#                     id_max = i
#             mymas[id_max] = mymas[j]
#             mymas[j] = max
#             j = j - 1
#
#             if c==TRUE:
#                 for s in range (n):
#                     print (maymas[s])

j=0
i=0
s=0
t=0
k=0
m=0
mymas = []

a=int(input("ааАаКаИаМ баПаОбаОаБаОаМ баОбаИбаЕ аОббаОббаИбаОаВаАбб аМаАббаИаВ: 1-аВбаБаОбаОаМ 2-аПбаЗбббаКаОаМ 3-аВббаАаВаКаАаМаИ 4-баЛаИбаИаЕаМ"))
n=int (input("ааЕаДаИбаЕ аКаОаЛ-аВаО баЛаЕаМаЕаНбаОаВ аМаАббаИаВаА"))

for i in range(n):
    row = input().split()
    for i in range(n):
        row[i] = int(row[i])
    mymas.append(row)    
##    for i in range (1,n):
##    mymas[i]=int(input())
b=int(input("абаЖаНаО аЛаИ аВбаВаОаДаИбб аПаОбаГаОаВб аДаЕаЙббаВаИб (1-YES/2-NO)?"))
if b<2:
    if b==1:
        c=True
    if b==2:
        c=False
##else:
##    return 0 kaquikequ

if a<3:
    if a==1:
        minmax(mymas)
        for s in range (n):
                    print (maymas[s]) 
    if a==2:
        pyz(mymas)
        for s in range (n):
                    print (maymas[s])
    if a==3:
        vstav(mymas)
        for s in range (n):
                    print (maymas[s])
    if a==4:
        sli(mymas)
        for s in range (n):
                    print (maymas[s]) 
## else:
##    return 0
