 
"""
The Morse code encodes every character as a sequence of "dots" and "dashes". For example, the letter A is coded as ·−, letter Q is coded as −−·−, and digit 1 is coded as ·−−−−. The Morse code is case-insensitive, traditionally capital letters are used. When the message is written in Morse code, a single space is used to separate the character codes and 3 spaces are used to separate words. 
For example, the message HEY JUDE in Morse code is ···· · −·−−   ·−−− ··− −·· ·.
NOTE: Extra spaces before or after the code have no meaning and should be ignored.

"""
def decode_morse(morse_code):
    """
    Takes a string of dots and dashes 
    and returns the decoded morse code.  
    """
    # First lets make a dictionary containing all the morse code
    morse = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.',
         'F':'..-.','G':'--.','H':'....','I':'..','J':'.---',
         'K':'-.-','L':'.-..','M':'--','N':'-.','O':'---',
         'P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-',
         'U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--',
         'Z':'--..', ' ':'.....'}

    decoded_msg = ""
    # Now swap the values from the dictionary
    msg_swap = dict([(v, k) for k, v in morse.items()])
    morse_code = morse_code.split(' ')
    for i in range(len(morse_code)-1):
        item = morse_code[(i + 1) % len(morse_code)]
        if morse_code[i] == '' and item == '':
            del morse_code[i]

    print(morse_code)
    for i in morse_code:
        if msg_swap.get(i) == None:
            decoded_msg += " "
        else:
             decoded_msg += msg_swap.get(i)
    # Due to the probable bug i will do it this way....
    return decoded_msg
    
def decodeMorse(morseCode):
    morse = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.',
         'F':'..-.','G':'--.','H':'....','I':'..','J':'.---',
         'K':'-.-','L':'.-..','M':'--','N':'-.','O':'---',
         'P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-',
         'U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--',
         'Z':'--..', ' ':'.....'}
    return ' '.join(''.join(morse[letter] for letter in word.split(' ')) for word in morseCode.strip().split('   '))

def main():
    example_1 = '.... . -.--   .--- ..- -.. .' # Expected Hey Jude
    example_2 = '... --- ...' # Expected SOS
    print(decode_morse(example_1))
    print(decode_morse(example_2))
    

if __name__ =="__main__":
    main()