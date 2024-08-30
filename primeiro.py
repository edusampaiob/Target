def fibonacci(n):
    output = []

    if n == 0:
        return output
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        output = [0, 1]
        while len(output) < n:
            output.append(output[-1] + output[-2])
        return output


n = 8
sequencia = fibonacci(n)
print(sequencia)

if n in sequencia:
    print("Seu número está dentro da sequência.")
else:
    print("Seu número não está dentro da sequência.")
