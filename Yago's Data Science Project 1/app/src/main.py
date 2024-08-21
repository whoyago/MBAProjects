"""
Este módulo fornece funcionalidades para decodificar mensagens em código Morse e salvar os resultados em um arquivo.

Importa:
    - conf: Módulo para carregar variáveis de ambiente.
    - datetime: Para manipulação de data e hora.

Variáveis:
    - MORSE_CODE_DICT (dict): Dicionário que mapeia códigos Morse para letras e números, obtido das variáveis de ambiente.
    - file_path (str): Caminho do arquivo onde as mensagens decodificadas serão salvas, obtido das variáveis de ambiente.

Funções:
    - decode_morse(morse_message): Decodifica uma mensagem em código Morse e retorna a mensagem decodificada como uma string.
        Parâmetros:
            morse_message (str): A mensagem em código Morse para ser decodificada.
        Retorna:
            str: A mensagem decodificada em texto normal.

    - main(): Função principal que lê uma mensagem em código Morse do usuário, decodifica-a e salva a mensagem decodificada
      juntamente com a data e hora da decodificação em um arquivo.
"""

import conf as conf
import datetime

MORSE_CODE_DICT = conf.get_env("DIC_MORSE")
file_path = conf.get_env("FILE_PATH")

def decode_morse(morse_message):
    """
    Decodifica uma mensagem em código Morse e retorna a mensagem decodificada como uma string.

    Parâmetros:
        morse_message (str): A mensagem em código Morse para ser decodificada.

    Retorna:
        str: A mensagem decodificada em texto normal.
    """
    words = morse_message.strip().split('   ')
    decoded_message = []
    for word in words:
        letters = word.split(' ')
        decoded_word = ''.join(MORSE_CODE_DICT.get(letter, '') for letter in letters)
        decoded_message.append(decoded_word)
    return ' '.join(decoded_message)

def main():
    """
    Função principal que lê uma mensagem em código Morse do usuário, decodifica-a e salva a mensagem decodificada
    juntamente com a data e hora da decodificação em um arquivo.
    """
    morse_message = input("Digite a mensagem em Morse (letras separadas por espaço, palavras por três espaços): ")

    decoded_message = decode_morse(morse_message)

    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, 'a') as file:
        file.write(f"Mensagem decodificada: {decoded_message}\n")
        file.write(f"Data e hora da decodificação: {current_datetime}\n\n")

    print("Mensagem decodificada e salva com sucesso.")

if __name__ == "__main__":
    main()
