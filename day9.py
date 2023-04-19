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
    return_print = morse(choice_opt, choice_word)

    #returns string to print function at call
    return return_print

def morse(option: int, words: str):

    #variable to be returned as conversion
    final = str("")

    #encrypt
    if(option == 0):

        #iterate over letters in the word, translating agaisnt array
        for letter in words:
            
            #if letter isn't a space, convert against morse array
            if(letter != " "):
                final += char_to_dots[letter] + " "
                
            #if letter is a space, add space to final return string    
            else:
                final += " "

        #need I explain?
        return final


    #decrypt
    elif(option == 1):

        #set running variables such as empty string for temp and counter variable
        #also added space to words, such that the function can end the final read
        words += " "
        temp_text = ""
        counter = 0
        
        #iterate through the letters with a for loop
        for letter in words:
            
            #if the letter isnt a space, the counter is reset to show a new word has started
            #temp text is updated with the next letter/character
            if(letter != " "):

                counter = 0
                temp_text += letter

            #if the letter is then a space, the counter is increased
            else:

                counter += 1

                #if counter ends up as 2, the program guesses as the existance of a space and adds it
                #to the final output string
                if(counter == 2):
                    final += " "

                #final is added to
                #a list is created of the function of the morse array, by the keys
                #this list is then navigated through based on the values
                #these values themselves are navigated through by the temp text, effectivelty converting in reverse
                else:
                    final += list(char_to_dots.keys())[list(char_to_dots.values()).index(temp_text)]
                    temp_text = ""

        return final

    else:
        print("sumfing didnt work")


    

#simple while running loop
while(running == True):

    #try except loop to keep errors to a minimum and handle them in a pretty way
    try:
        print(init_morse())
        #running ended when a successful run is achieved in the primary functions
        running = False

    except:
        print("Something in the code didn't work :(")

    
