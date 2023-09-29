import base64

texto = input("Digite o texto a ser codificado em base64: ")

texto_codificado = base64.b64encode(texto.encode('utf-8'))

print("Texto codificado em base64:", texto_codificado.decode('utf-8'))
       
    