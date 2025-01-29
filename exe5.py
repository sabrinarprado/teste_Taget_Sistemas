def inverter_string(s):
    string_invertida = ""
    for i in range(-1, -len(s)-1, -1):  # Começa do último índice até o primeiro
        string_invertida += s[i]  # Adiciona o caractere à nova string
    return string_invertida

entrada = input("Digite algo: ")
resultado = inverter_string(entrada)
print(f"String invertida: {resultado}")
