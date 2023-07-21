#Chiasm Test 

from itertools import count
import os                                       #uses os library for its functions

directory = 'C:/Users/New PC/Desktop/Repos/Chiasm Project'      #directory for the location of the file "Chiasm_Test.txt"
filename = 'Chiasm_Test.txt'                    #name of the file
file_path = os.path.join(directory, filename)   #joins path and file

print(file_path)                                #ensures the intended file and file path
############################################################################################################################################

try:                                            #used try in case of any expected errors 
    
    file = open(file_path, 'r', encoding = 'utf-8')     #opens filepath in read mode, also uses encoding to avoid the Error
    file_contents = file.read()                 #reads the file 
    file.close()                                #closes the file

    print(file_contents)                        #ensures intended contents of the file 

except FileNotFoundError:                       #ensures that any error wont stop the whole code 
    print('file not found, please find the correct path and filename :)')   #this is a nice way fo me telling them to try again

############################################################################################################################################

from collections import Counter                 #imports counter for its commands 

def count_repeating_words(file_path):           #creates a brand new command
    with open(file_path, 'r', encoding = 'utf-8') as file:      #reopening the file for the sake of word counting 
        file_contents = file.read()             #reads the file 

        exclude_words = ['the', 'and', 'in', 'a', 'to', 'it', 'it.', 'it,']     #list for exlusion words (might make a seperate text file for redudant words)

        words = file_contents.split()           #turns the file into individual words 

        word_counts = Counter(word.lower() for word in words if word.lower() not in exclude_words)      #lower or upper case no longer matters  
        repeating_words = [(word, count) for word, count in word_counts.items() if count > 1]           #only counts words that occur more than once 
        repeating_words.sort(key=lambda x: x[1], reverse=True)                                          #tbh idk what this does, my guess is sorts it but not totally sure about the criteria 

        file.close()                            #closes the file  
        return repeating_words                  #ends the function 

repeating_words = count_repeating_words(file_path)      #recalls the funciton

for word, count in repeating_words:             #idk what this does tbh
    print(f'{word}: {count}')                   #prints reoccuring words and number of occurances 

############################################################################################################################################
