def inverter_string(string):
    string_invertida = ''
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]
    return string_invertida

texto = input("Informe uma string: ")
print(f'String invertida: {inverter_string(texto)}')
