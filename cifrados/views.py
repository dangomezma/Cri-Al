from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render

#lógica que ya estaba implementada en utils.py
from .utils import cesar_code, cesar_decode, vigenere_code, vigenere_decode, xor_code, xor_decode

@csrf_exempt # Desactivamos la seguridad CSRF temporalmente para facilitar la conexión local con el JS
def procesar_cifrado(request):
    if request.method == 'POST':
        try:
            # Recibimos los datos enviados desde JavaScript
            data = json.loads(request.body)
            texto = data.get('texto', '')
            metodo = data.get('metodo', '')
            accion = data.get('accion', 'cifrar')
            clave = data.get('clave', '')

            resultado = ""

            # Ejecutamos el algoritmo matemático correspondiente
            if metodo == 'cesar':
                if accion == 'bruteforce':
                    # Aritmética modular iterando los 26 desplazamientos posibles
                    lineas = [f"[{i:02d}] {cesar_decode(texto, i)}" for i in range(26)]
                    resultado = "\n".join(lineas)
                else:
                    k = int(clave) if str(clave).isdigit() or (str(clave).startswith('-') and str(clave)[1:].isdigit()) else 0
                    resultado = cesar_code(texto, k) if accion == 'cifrar' else cesar_decode(texto, k)
                
            elif metodo == 'vigenere':
                resultado = vigenere_code(texto, clave) if accion == 'cifrar' else vigenere_decode(texto, clave)
                
            elif metodo == 'xor':
                resultado = xor_code(texto, clave) if accion == 'cifrar' else xor_decode(texto, clave)
                
            else:
                return JsonResponse({'error': 'Método no válido'}, status=400)

            # Devolvemos el resultado al frontend
            return JsonResponse({'resultado': resultado})
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
            
    return JsonResponse({'error': 'Solo se aceptan peticiones POST'}, status=405)

def home(request):
    return render(request, 'index.html')