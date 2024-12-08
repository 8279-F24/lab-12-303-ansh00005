import time

# Morse code dictionary for letters and numbers
MORSE_CODE_DICT = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
    'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
    'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
    'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
    'z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----'
}

# Function to clean and filter the input sentence
def clean_sentence(sentence):
    sentence = sentence.lower()
    return ''.join([char for char in sentence if char in MORSE_CODE_DICT or char == ' '])

# Convert a sentence to Morse code
def sentence_to_morse(sentence):
    morse_list = []
    for word in sentence.split():
        word_morse = ' '.join([MORSE_CODE_DICT[char] for char in word])
        morse_list.append(word_morse)
    return morse_list

# Prompt the user for a valid unit length
def prompt_unit_length():
    while True:
        try:
            unit_length = float(input("Enter the unit length in seconds (0 - 1s): "))
            if 0 < unit_length <= 1:
                return unit_length
            else:
                print("Please enter a value between 0 and 1.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Display Morse code with timing delays
def display_morse_code(morse_list, unit_length):
    for word in morse_list:
        for char in word:
            if char == '.':
                print("Dot", end=" ", flush=True)
                time.sleep(unit_length)
            elif char == '-':
                print("Dash", end=" ", flush=True)
                time.sleep(3 * unit_length)
            else:  # Space between letters
                time.sleep(3 * unit_length)
            time.sleep(unit_length)  # Space between parts of the same letter
        print("\nSpace between words\n")
        time.sleep(7 * unit_length)  # Space between words

# Main program function
def main():
    sentence = input("Enter a sentence: ")
    cleaned_sentence = clean_sentence(sentence)
    if not cleaned_sentence:
        print("No valid characters entered.")
        return
    
    unit_length = prompt_unit_length()
    morse_list = sentence_to_morse(cleaned_sentence)
    
    print("Morse code representation:", ' / '.join(morse_list))
    display_morse_code(morse_list, unit_length)

if __name__ == "__main__":
    main()
