string = input("Informe uma string: ")

string_invertida = ""
for char in string:
    string_invertida = char + string_invertida

print(f"String invertida: {string_invertida}")