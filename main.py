
MORSE_CODE_DICT = { 'A': '.-', 'B': '-...',
                    'C': '-.-.', 'D': '-..', 'E': '.',
                    'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-',
                    'L': '.-..', 'M': '--', 'N': '-.',
                    'O': '---', 'P': '.--.', 'Q': '--.-',
                    'R': '.-.', 'S': '...', 'T': '-',
                    'U': '..-', 'V': '...-', 'W': '.--',
                    'X': '-..-', 'Y': '-.--', 'Z': '--..',
                    '1': '.----', '2': '..---', '3': '...--',
                    '4': '....-', '5': '.....', '6': '-....',
                    '7': '--...', '8': '---..', '9': '----.',
                    '0': '-----', ', ': '--..--', '.': '.-.-.-',
                    '?': '..--..', '/': '-..-.', '-': '-....-',
                    '(': '-.--.', ')': '-.--.-'}


def encode(message):
    result = ''
    for letter in message:
        if letter != ' ':
            result += MORSE_CODE_DICT[letter.upper()] + ' '
        else:
            result += ' '
    result += ' '
    print(result)


def decode(morse_code):
    result = ''
    space = 0
    text = ''
    for letter in morse_code:

        if letter != ' ':
            space = 0
            text += letter
        else:
            space += 1
            # print(text)
            # print(list(MORSE_CODE_DICT.values()).index(text))
            if text != '':
                result += str(list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(text)]).lower()
            text = ''
            if space == 2:
                result += ' '
    print(result)


if __name__ == '__main__':
    text_to_morse = input("Enter your text: ")
    encode(text_to_morse)
    decode_text = input("Enter Morse Code: ")
    decode(decode_text)

