v1 = 0
v2 = 1
n = int(input("entre com o valor: "))
for i in range(0,n):
    s = v1 + v2
    v2 = v1 
    v1 = s

print(s)
