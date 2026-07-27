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
    # Filtramos la clave para que solo contenga letras del abecedario
    key_clean = "".join([c for c in key.lower() if c in alphabet])
    
    if not key_clean:
        raise ValueError("La clave para Vigenère debe contener letras.")
        
    result = ""
    key_index = 0
    
    for i in x:
        if i in alphabet:
            position = alphabet.index(i)
            # Usamos la clave limpia para evitar el error 'substring not found'
            k = alphabet.index(key_clean[key_index % len(key_clean)])
            
            # Aplicamos la aritmética modular: E(x) = (x + k) mod 26
            nueva_posicion = (position + k) % 26
            result += alphabet[nueva_posicion]
            
            key_index += 1
        else:
            result += i
    return result

# decodificador vigenere
def vigenere_decode(x: str, key: str):
    x = x.lower()
    key_clean = "".join([c for c in key.lower() if c in alphabet])
    
    if not key_clean:
        raise ValueError("La clave para Vigenère debe contener letras.")
        
    result = ""
    key_index = 0
    
    for i in x:
        if i in alphabet:
            position = alphabet.index(i)
            k = alphabet.index(key_clean[key_index % len(key_clean)])
            
            # Aplicamos la aritmética modular inversa: D(x) = (x - k) mod 26
            nueva_posicion = (position - k) % 26
            result += alphabet[nueva_posicion]
            
            key_index += 1
        else:
            result += i
    return result

"""
XOR cipher implementation:
"""
    # codificador XOR (Álgebra de Boole)
def xor_code(text: str, key: str):
    if not key:
        return text
        
    result = []
    for i in range(len(text)):
        # Convertimos a código ASCII
        char_code = ord(text[i])
        key_code = ord(key[i % len(key)])
        
        # Operación XOR bit a bit (^)
        xor_result = char_code ^ key_code
        
        # Guardamos como texto hexadecimal de 2 dígitos para evitar caracteres invisibles
        result.append(f"{xor_result:02x}")
        
    return "".join(result)

# decodificador XOR
def xor_decode(hex_text: str, key: str):
    if not key:
        return hex_text
        
    result = ""
    # Procesamos el texto hexadecimal de 2 en 2 caracteres
    for i in range(0, len(hex_text), 2):
        # Convertimos el par hexadecimal de vuelta a entero
        char_code = int(hex_text[i:i+2], 16)
        key_code = ord(key[(i//2) % len(key)])
        
        # Aplicamos XOR nuevamente para revertir (Álgebra de Boole)
        xor_result = char_code ^ key_code
        result += chr(xor_result)
        
    return result