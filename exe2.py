def numero_fibonacci(n):
    a = 0
    b = 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False

num = int(input("Digite um número: "))
if numero_fibonacci(num):
    print(f"O número {num} pertence a sequência Fibonacci.")
else:
    print(f"O número {num} não pertence a sequência Fibonacci.")

        