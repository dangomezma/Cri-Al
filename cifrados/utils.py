alphabet = "abcdefghijklmnopqrstuvwxyz"

# codificador cesar
def cesar_code(x:str, k:int):
    x = x.lower()
    result = ""
    for i in x:
        if i in alphabet:
            position = alphabet.index(i)
            # Se aplica la aritmética modular: E(x) = (x + k) mod 26
            nueva_posicion = (position + k) % 26
            result += alphabet[nueva_posicion]
        else:
            result += i
    return result

# decodificador cesar
def cesar_decode(x:str, k:int):
    return cesar_code(x, -k)

# retorna todas las posibles codificaciones del string
def bruteforce(x:str):
    for i in range(26):
        result = cesar_decode(x, i)
        print(f"{i}: {result}")