import base64
import sys


# Função para codificar texto em base64
def texto_para_base64(texto):
    # Codifica o texto para bytes
    texto_bytes = texto.encode('utf-8')

    # Codifica os bytes em base64
    texto_base64 = base64.b64encode(texto_bytes)

    # Converte os bytes codificados em base64 de volta para uma string
    texto_base64_str = texto_base64.decode('utf-8')

    return texto_base64_str


# Função para decodificar base64 em texto
def base64_para_texto(base64_str):
    # Decodifica a string base64 para bytes
    base64_bytes = base64_str.encode('utf-8')

    # Decodifica os bytes em texto
    texto_bytes = base64.b64decode(base64_bytes)

    # Converte os bytes de volta para uma string
    texto = texto_bytes.decode('utf-8')

    return texto


while True:
    # Pergunta ao usuário qual conversão ele deseja realizar
    escolha = input(
        "Escolha uma opção:\n1 - Converter texto em base64\n2 - Converter base64 em texto\n3 - Finalizar o programa\n")

    # Verifica a escolha do usuário
    if escolha == '1':
        # Pede ao usuário para inserir o texto a ser codificado em base64
        texto = input("Digite o texto a ser codificado em base64: ")

        # Converte o texto de entrada em base64
        texto_codificado = texto_para_base64(texto)

        # Imprime o resultado
        print("Texto Original: ", texto)
        print("Texto Codificado em Base64: ", texto_codificado)
    elif escolha == '2':
        # Pede ao usuário para inserir o texto base64 a ser decodificado
        texto_base64 = input("Digite o texto base64 a ser decodificado: ")

        # Converte o texto base64 em texto
        texto_decodificado = base64_para_texto(texto_base64)

        # Imprime o resultado
        print("Texto Codificado em Base64: ", texto_base64)
        print("Texto Decodificado: ", texto_decodificado)
    elif escolha == '3':
        # Finaliza o programa
        print("Programa finalizado.")
        break
    else:
        print("Escolha inválida. Por favor, escolha 1, 2 ou 3 para a conversão ou finalização do programa.")