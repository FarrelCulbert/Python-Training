n = int(input("enter number of rows: "))
#1
# for i in range (1, n+1):
#     print("*" * i)
#2
# for i in range (1, n+1):
#      print("*" * (n - i))
#3
# for i in range (1, n+1):
#      print(" " * (n - i), end="")
#      print("*" * (2*i-1))
#4
for i in range (n,0,-1):
     print(" " * (n - i), end="")
     print("*" * (2*i-1))