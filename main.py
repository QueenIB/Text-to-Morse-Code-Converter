alphabet_string = "abcdefghijklmnopqrstuvwxyz1234567890"
alphabet = [char for char in alphabet_string]
alphabet.append(" ")
morse_code = ['._', '_...', '_._.', '_..', '.', '.._.', '__.', '....', '..',
              '.___', '_._', '._..', '__', '_.', '___', '.__.', '__._', '._.',
              '...', '_', '.._', '..._', '.__', '_.._', '_.__', '__..', '.____',
              '..___', '...__', '...._', '.....', '_....', '__...', '___..',
              '____.', '_____', ' ']


def text_to_morse_code_converter(text):
    code = ""
    code_list = []
    text_list = [char for char in text]
    text_index = [alphabet.index(item) for item in text_list]
    for item in text_index:
        code_list.append(morse_code[item])
        code_list.append(" ")
    code = "".join(code_list)
    print(f"This is the equivalent of your text in Morse Code:\n{code}")


print("\nWelcome to Text to Morse Code Converter!")
more_text_to_convert = True
while more_text_to_convert:
    valid_input = False
    while not valid_input:
        text_to_convert = input("\nType the text you'll like to convert: ").lower()

        # Check if input contains only alphabets, numbers, and spaces
        if not all(char.isalnum() or char.isspace() for char in text_to_convert):
            print("That's an invalid input. You can only give alphabets A to Z and "
                  "numbers 0 to 9. Try again.")
        else:
            text_to_morse_code_converter(text_to_convert)
            break
    prompt = True
    while prompt:
        want_to_continue = input("\nDo you have any more text to convert? "
                                 "type 'yes' or 'no': ").lower()
        if want_to_continue != 'yes' and want_to_continue != 'no':
            print("That's an invalid input. Type yes or no.")
        elif want_to_continue == 'no':
            print("Thank you for using Text to Morse Code Converter. Feel free to "
                  "come back again.")
            prompt = False
            more_text_to_convert = False
        else:
            prompt = False
