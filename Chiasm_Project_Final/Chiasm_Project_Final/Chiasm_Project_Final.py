#Chiasm Project Final

from collections import Counter
from itertools import count
import os

#list of libraries for follwoing code 

############################################################################################################################################

directory_EW = 'C:/Users/New PC/Desktop/Repos/Chiasm Project'
filename_EW = 'Exclusion_Words.txt'
file_path_EW = os.path.join(directory_EW, filename_EW)

directory_BV = 'C:/Users/New PC/Desktop/Repos/Chiasm Project'   
filename_BV = 'Chiasm_Test.txt'                 
file_path_BV = os.path.join(directory_BV, filename_BV)

#filepath for both exlucsion word list and bible verse
#might have to edit depending on user's file location 

print(file_path_BV) 
print()
print(file_path_EW)
print()
print()

############################################################################################################################################

try:                                           
    
    file_BV = open(file_path_BV, 'r', encoding = 'utf-8')     
    file_contents_BV = file_BV.read()              
    file_BV.close()                               

    #reads using utf-8 to avoid unrecognizable characters 

    print(file_contents_BV)   
    print()
    print()
      
    ############################################################################################################################################

    with open(file_path_EW, 'r') as file_EW:
        content = file_EW.read()
        exclude_words = content.split()
        file_EW.close()

        #the exlusion list can be altered anytime

        print("'Below is a list for common words in sentences'")
        print (exclude_words)
        print()
        print()

    ############################################################################################################################################

    def count_repeating_words(file_path_BV):                   
        words = file_contents_BV.split() 

        word_counts = Counter(word.lower() for word in words if word.lower() not in exclude_words)      
        repeating_words = [(word, count) for word, count in word_counts.items() if count > 1]         
        repeating_words.sort(key=lambda x: x[1], reverse=True)
        
        #does not discriminate for upper nor lower case 
        #must occur more than once
        #organizes in descending order 

        file_BV.close()
        return repeating_words

    repeating_words = count_repeating_words(file_path_BV)
    for word, count in repeating_words:
        print(f'{word}: {count}')

        #counter for the words found

    ############################################################################################################################################

    url = "https://reasonsforhopejesus.com/the-meaning-of-numbers-in-the-bible/"
    link_text = "   numbers in the bible explained"

    #hyperlink to a the number meanings 

    print()
    print()
    print(f"{url}{link_text}")
    print()
    print()

############################################################################################################################################



############################################################################################################################################
except FileNotFoundError:                       
    print('file not found, please find the correct path and filename :)')
    print('common mistakes: incorrect file path, mispelling of filename, file type not in .txt format, etc.')

    #if no correct filepath is found, code will end 
    