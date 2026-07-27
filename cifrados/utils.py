alphabet = "abcdefghijklmnopqrstuvwxyz"

"""
Cesar cipher implementation:
"""
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

"""
Vigenere cipher implementation:
"""

# codificador vigenere
def vigenere_code(x: str, key: str):
    x = x.lower()
    key = key.lower()
    result = ""
    key_index = 0
    
    for i in x:
        if i in alphabet:
            position = alphabet.index(i)
            # Obtenemos el desplazamiento basado en la letra actual de la clave
            k = alphabet.index(key[key_index % len(key)])
            
            # Aplicamos la aritmética modular: E(x) = (x + k) mod 26
            nueva_posicion = (position + k) % 26
            result += alphabet[nueva_posicion]
            
            # Avanzamos el índice de la clave solo si ciframos una letra válida
            key_index += 1
        else:
            result += i
    return result

# decodificador vigenere
def vigenere_decode(x: str, key: str):
    x = x.lower()
    key = key.lower()
    result = ""
    key_index = 0
    
    for i in x:
        if i in alphabet:
            position = alphabet.index(i)
            k = alphabet.index(key[key_index % len(key)])
            
            # Aplicamos la aritmética modular inversa: D(x) = (x - k) mod 26
            nueva_posicion = (position - k) % 26
            result += alphabet[nueva_posicion]
            
            key_index += 1
        else:
            result += i
    return result