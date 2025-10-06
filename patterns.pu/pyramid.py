n = 9
for i in range (1, n+1):
  for j in range(n-i):
       print(" ", end =" ")
  for k in range (2*i-1):
     print("*",end=" ")
  print()     
          
    # advacnce logic
n=5
for i in range (n):
  print(" "*(n-i) + "*"*(2*i-1))
print()  