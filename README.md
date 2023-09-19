**Name of Program** 


MadLibs Assignment - Have the program read a file that creates a game of MadLibs
Initialize
What items need to be initialized at the beginning of the program? Importing something? Defining a file name?
Creating an empty list or dictionary? Etc.
- Creating an empty list called ‘Sentences’
- Importing Random to randomize the sentences chosen
- Setting a variable, ‘Text’, to be the name of the MadLib file
  
**Functions**



● MadLibsFile - It takes the MadLib file and an empty list called ‘Sentences’, The function returns a list of
each sentence appended to the list




● ComputerWants- It takes the list of sentences and returns one of them as a random choice




● PromptList- Takes the Random Choice of Sentence and returns a list of the words in the brackets that
will be replaced




● PromptChange- Takes the Random Choice of sentence and the list of words in brackets to make a
dictionary where the elements of a list are the keys and user's input is the value. Replaces the word if
it matches the dictionary keys with the key's value and returns the new sentence.




**Control Flows**
What control flows will you need to use and how? Will you need conditionals? What will they do? While loops?
Why while loops? Etc.



- There will be for loops in ¾ of the functions. The for loop in the MadLibs file function will split the
MadLibs file line by line.



- For loops for the PromptList function to pick out the specific word from the sentence that the user’s
input will be replaced. The conditionals will check for weather or not there is a ‘>’ in the sentence



- For loops for the PromptChange function are necessary to switch the user input with the correct noun
from the original MadLib sentence. The conditionals will check if the key in the dictionary is equal to a
word in the sentence. So it knows to replace the word with the corresponding dictionary value.

**Expected Outputs**
What will the user see when running your program? Will they be prompted to do something? What will print? In
what order will it print?



- The user will be prompted to enter a word that will replace the specific noun in the sentence, this will
happen numerous times depending on how many words there are to replace.



- The user will not see the sentence beforehand.


- After the user has put in all the input necessary, the sentence with the user’s input will be shown to the
user and the program will end.
