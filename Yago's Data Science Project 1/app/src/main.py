import conf as conf
import datetime
MORSE_CODE_DICT = conf.get_env("DIC_MORSE")
file_path = conf.get_env("FILE_PATH")

def decode_morse(morse_message):
    words = morse_message.strip().split('   ')
    decoded_message = []
    for word in words:
        letters = word.split(' ')
        decoded_word = ''.join(MORSE_CODE_DICT.get(letter, '') for letter in letters)
        decoded_message.append(decoded_word)
    return ' '.join(decoded_message)

def main():
    morse_message = input("Digite a mensagem em Morse (letras separadas por espaço, palavras por três espaços): ")
    
    decoded_message = decode_morse(morse_message)
    
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(file_path, 'a') as file:
        file.write(f"Mensagem decodificada: {decoded_message}\n")
        file.write(f"Data e hora da decodificação: {current_datetime}\n\n")

    print("Mensagem decodificada e salva com sucesso.")

if __name__ == "__main__":
    main()