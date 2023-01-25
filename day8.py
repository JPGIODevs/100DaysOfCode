#morse challenge


#running parameters
running = True
char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}


#input and initiation function, defined to aid in try-catch scenario
def init_morse():
    choice_word = str(input("Please enter a phrase in morse of alphabet to convert: ")).upper()
    choice_opt = int(input("type 0 to convert to morse, 1 to convert to alphabet: "))

    #convert to something prettier, try return arguements to aid defensive coding
    morse(choice_opt, choice_word)

def morse(option: int, words: str):

    #variable to be returned as conversion
    final = str("")

    #encrypt
    if(option == 0):

        for letter in words:
            
            if letter != " ":
                final += char_to_dots[letter] + " "
                

            else:
                final += " "

        
        print(final)
        


    #decrypt
    elif(option == "1"):
        print("hello")

    return(final)


while(running == True):

    printout = init_morse()
    print(printout)
    running = False
    #try:
        #init_morse()
        #print(final)
        #running = False
    #except:
        #print("wip")

    
