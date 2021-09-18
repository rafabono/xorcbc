import sys

TAM_BLOQUE = 4
key = ""
msg_cifrado = ""

def xorhex(a, b):
    return (hex(int(a, 16) ^ int(b, 16)))[2:]

if __name__ == '__main__':
    
    msg_cifrado_limpio = msg_cifrado.replace(" ", "")    
    iter = 1
    mensaje_descifrado = ''
    for i in range(0, len(msg_cifrado_limpio), TAM_BLOQUE):
        trozo_cifrado = msg_cifrado_limpio[i:i+TAM_BLOQUE]
        if iter == 1:
            trozo_descifrado = xorhex(trozo_cifrado,key)
            iter = 2
        else:
            trozo_descifrado = xorhex(xorhex(trozo_cifrado,key),trozo_cifrado_anterior)
        trozo_cifrado_anterior = trozo_cifrado
        mensaje_descifrado = mensaje_descifrado + trozo_descifrado
        
    print("Mensaje descifrado en hexadecimal:")
    print(mensaje_descifrado)
