#Dado un entero positivo n (> 1), comprobar si es primo o compuesto.
n = int(input("n="))
is_prime = True
for i in range(2, n):
   if n % i == 0:
     is_prime = False
     break

print(is_prime)