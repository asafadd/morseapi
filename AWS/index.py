# text to morse code translator
# Test by Asaf Add

import json

# rosseta table
morse_dict={'A': '.-',  'B': '-...',  'C': '-.-.',  'D': '-..',  'E': '.',
            'F': '..-.',  'G': '--.',  'H': '....',  'I': '..',  'J': '.---',
            'K': '-.-',  'L': '.-..',  'M': '--',  'N': '-.',  'O': '---',  
            'P': '.--.',  'Q': '--.-',  'R': '.-.',  'S': '...',  'T': '-',  
            'U': '..-',  'V': '...-',  'W': '.--',  'X': '-..-',  'Y': '-.--',  
            'Z': '--..',  '0': '-----',  '1': '.----',  '2': '..---',  '3': '...--',  
            '4': '....-',  '5': '.....',  '6': '-....',  '7': '--...',  '8': '---..',  
            '9': '----.',  '.': '.-.-.-',  ',': '--..--',  "'": '.----.',  '?': '..--..',  
            ':': '---...',  '-': '-....-',  '/': '-..-.',  '[': '-.--.',  '(': '-.--.',  
            ']': '-.--.-',  ')': '-.--.-',  '"': '.-..-.',  '_': '..--.-',  '=': '-...-',  
            '+': '.-.-.', '@': '.--.-.'}

# Lambda handler
def lambda_handler(event, context):    
    result = translate_morse(event["queryStringParameters"])
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }

# Translator code
def translate_morse (event):
    result = ""
    if 'text' in event:
        text = event["text"]
        text = text.upper()
        for letter in text:
            if letter in morse_dict:
                result += morse_dict[letter] + ' '
            else:
                if letter == ' ':
                    result += ' '
    else:
        result = "No text parameter sent"
    return result.strip()

# Tests
if __name__ == "__main__":
    assert translate_morse({"text":"Hello world"}) == ".... . .-.. .-.. ---  .-- --- .-. .-.. -.."
    assert translate_morse({"text":"שלום עולם"}) == ""
    assert translate_morse({"text":""}) == ""
    assert translate_morse({"text":"You're such a !@#$$#@**@#"}) == "-.-- --- ..- .----. .-. .  ... ..- -.-. ....  .-  .--.-. .--.-. .--.-."
    