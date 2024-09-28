alphabet_string = "abcdefghijklmnopqrstuvwxyz1234567890"
alphabet = [char for char in alphabet_string]
alphabet.append(" ")
morse_code = ['._', '_...', '_._.', '_..', '.', '.._.', '__.', '....', '..',
              '.___', '_._', '._..', '__', '_.', '___', '.__.', '__._', '._.',
              '...', '_', '.._', '..._', '.__', '_.._', '_.__', '__..', '.____',
              '..___', '...__', '...._', '.....', '_....', '__...', '___..',
              '____.', '_____', '.......']


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


print("Welcome to Text to Morse Code Converter!")
more_text_to_convert = True
while more_text_to_convert:
    text_to_convert = input("Type the text you'll like to convert:\n").lower()
    text_to_morse_code_converter(text_to_convert)
    want_to_continue = input("Do you have any more text to convert? "
                             "type 'yes' or 'no':\n").lower()
    if want_to_continue == 'no':
        print("Thank you for using Text to Morse Code Converter. Feel free to "
              "come back again.")
        more_text_to_convert = False


