b=int(input("Digite o valor da base: "))
e=int(input("Digite o valor do expoente: "))
r=b
for g in range(1,e):
   r=r*b 
print("Resultado é: ","{:.2f}".format(r))
