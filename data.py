#SOAL NOMER 1
#Rumus awal 0, 1
def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else: 
        return Fibonacci(n-1) + Fibonacci(n-2)
    

print(Fibonacci(4))
