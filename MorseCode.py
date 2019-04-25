## COSC 2030

## Project 2: Morse Code

    # Tiago Araujo, Bailie Allemand, Connor Kasarda, Jeffrey Michaelis, Matt Sharp.

## In the morse code, the letters are separated by one space and the words are separated by 2 spaces
## This code allows capital and small letters
    # If the letter is capitalized, during the encode, one '*' is added before the morse code;
    # during the decode, the program verifies if the symbol before the morse code is a '*',
        # if it is the case, it prints the letter capitalized

# To run this program,
    # You will need to download the MorseTable.txt file on Wyocourses
    # You will need one txt file in english letters, to have it translated into morse code, or
    # You will need one txt file in morse code, to have it translated into english letters

## The program works even when symbols in the english file do not exist in the "MorseTable.txt" file
    # if that happens, this unkown symbol will be ignored

## The program works even when there are morse codes in the morse code file that does not exists in the "MorseTable.txt" file
    # if that happens, this unkown morse code will be ignored

## You can choose the symbols of the morse code by selecting 'change' at the main menu
    ## if you do not change it, the program will work with '.' and '-' by default
    ## The new symbols must be just one character and they must be different from each other and
        # different from '*' because it is the symbol that allows capitalized letters


## This first part is to allow to change the color of the output text

import sys
try:
    shell_connect = sys.stdout.shell
except AttributeError:
    print("idlecolors highlighting only works with IDLE")
    exit()

## this is the class of the tree

class Node:
    """The Node class is the class to work with the binary tree.
        This class has 3 methods:
            prinTree;
            insert;
            find_letter.
            """
    def __init__(self,letter):
        self.left = None
        self.right = None
        self.letter = letter

    ## function to print the entire tree in preorder
    def printTree(self):
        """Method that prints the binary tree."""
        print(self.letter)
        if self.left:
            self.left.PrintTree()
        if self.right:
            self.right.PrintTree()


    ## create a binary tree with letters in its nodes
        # if '.' -> go to the left
        # if '-' -> go to the right
        # at the end of the path, if the node already exists and it is an empty string (' '), turn the value of the node that letter 
         #if, at the end of the path, the node do note exists, create a new node with value that letter


    ## given a path (morse code) and a letter, insert the letter into the binary tree in its right position 
    def insert(self,path,letter):
        """Method that takes a morse code and a letter
            and insert the letter in the binary tree acording to the morse code."""
        # if it is a dot, go to the left
        if path[0] == var1:
            # if the path is not just one symbol, go to the left and try again 
            if len(path) > 1:
                path = path[1:]
                if self.left == None:
                    self.left = Node(' ')
                self.left.insert(path,letter)
            else:
                # if the path is just one symbol, insert the letter on the left
                if self.left == None:
                    self.left = Node(letter)
                else:
                    if self.left.letter == ' ':
                        self.left.letter = letter
                    else:
                         print('error: ja existe letra')
        # if it is a dash, go to the right
        elif path[0] == var2:
            # if the path is not just one symbol, go to the right and try again
            if len(path) > 1:
                path = path[1:]
                if self.right == None:
                    self.right = Node(' ')
                self.right.insert(path,letter)
            else:
                # if the path is just one symbol, insert the letter on the right
                if self.right == None:
                    self.right = Node(letter)
                else:
                    if self.right.letter == ' ':
                        self.right.letter = letter
                    else:
                        print('error: the letter already exists')

    # given a morse code, find the correspondence letter which is inside the binary tree
    def find_letter(self,hidden_letter_path):
        """Method that takes a morse code and finds the correspondent letter
            going through the binary tree."""
        if hidden_letter_path[0] == var1:
            if len(hidden_letter_path) > 1:
                hidden_letter_path = hidden_letter_path[1:]
                return self.left.find_letter(hidden_letter_path)
            else:
                return(self.left.letter)
        elif hidden_letter_path[0] == var2:
            if len(hidden_letter_path) > 1:
                hidden_letter_path = hidden_letter_path[1:]
                return self.right.find_letter(hidden_letter_path)
            else:
                return(self.right.letter)



## Function to translate a file from english letters to morse code
            
def English2Morse ():
    """Function that takes a file with
        english letters and creates another file
        with the morse code correspondents."""
    
    morse_word = ''
    morse_list = []
    why = ''
    excp2 = True
    excp3 = True
    global dictionary
    global Morse_dict
    
    ## This part is building the Table, which is an dictionary,
        # that shows for each letter (the key), the equivalent dot-dash string (the value)
    # if newM is True, that means that the user has changed the symbols of the morse code, so, we are going to use the new table
        # if it is False, that means the uer did not change the symbols, so we can use the table wiht dash and dots
    # also, if the variable dictionary is false, it means that the user have not used the English2Morse function yet, so,
        ## we need to create the dictionary, otherwise, if it is true, the user have already created the dictionary,
        ## so it is not necessary to create it again
        # but, if the user changed the morse symbol, it is going to create the new dictionary
    if newM:
        Morse_Table = open('new_MorseTable.txt','r')
    else:
        if not dictionary:
            try:
                Morse_Table = open('MorseTable.txt','r')
            except:
                shell_connect.write('MorseTable.txt not found. Download it to continue.\n','COMMENT')
                excp3 = False
    if excp3:
        if not dictionary or newM:
            for line in Morse_Table:
                Morse_dict.update({line[0]:line[2:-1]})
            Morse_Table.close()
            dictionary = True
        ## take the name of the file which has english letters to translate the text into morse code
            #try until the user enter a file that exists
        print(Morse_dict)
        while True:
            try:
                filename = input("Please, write the name of the file (with extension) which has letters: \n")
                E2M_file = open(filename,'r')
                break
            except:
                shell_connect.write('File does not exist, try again.\n','COMMENT')
        # creates the file which is going to have the message in morse code
        morse_hidden_file = open(filename[:-4]+'_hidden.txt','w')
        # for each line in the file, take each word. For each word, transform the letters into morse code
        # Invariant: line is always less than or equal to the number of lines in the english to morse file
        for line in E2M_file:
            # If the lines begins with a space, then write the spaces in the file being created and remove them from the line being read
            while line[0] == ' ':
                morse_hidden_file.write(' ')
                line = line[1:]
            words_list = line.split()
            if words_list != []:
                # if the user made a mistake and chose a file which is already in morse code, an error message is shown
                if words_list[0][0] == var1 or words_list[0][0] == var2 or words_list[0][0] == '*':
                    excp = False
                    excpwhy = 'The file is not a letter file'
                    shell_connect.write('\nThis is not a letter file!\n','COMMENT')
                    break
                else:
                    # for each letter in each word, print the correspondent morse code in the new file
                    # Invariant: word is always less than or equal to number of words in words_list
                    for word in words_list:
                        # Invariant: letter is always less than or equal to the number of letters in word
                        for letter in word:
                            # if the letter is uppercase, add a '*' symbol in front of the letter and transform the lowercase of that letter into morse code
                            try:
                                if not letter.isupper():
                                #transform the letter into morse code
                                    morse_word = morse_word + Morse_dict[letter] + ' '
                                else:
                                    letter = letter.lower()
                                    morse_word = morse_word +'*'+ Morse_dict[letter] + ' '
                            except:
                                ##letter not found
                                excp2 = False
                                why = letter + ', '
                                excpwhy = 'warning: {} not found and not printed'.format(why)
                        morse_hidden_file.write(morse_word)
                        morse_word = ''
                        morse_hidden_file.write('  ')
                        excp = True
                morse_hidden_file.write('\n')
            else:
                morse_hidden_file.write('\n')
        E2M_file.close()
        morse_hidden_file.close()
        # if excp is True, that means all went right, if it is False, that means that something went wrong
        if excp:
            if excp2:
                shell_connect.write('\nEnglish to Morse sucessful!','STRING')
            else:
                shell_connect.write('\nEnglish to Morse partially sucessful, some symbols not found were ignored.','KEYWORD')
            print('\nThe file {} was created.'.format(filename[:-4]+'_hidden.txt'))
        else:
            shell_connect.write('\nEnglish to Morse failed. '+excpwhy+'.\n','COMMENT')


# Function to translate a file from morse code to english letters

def Morse2English():
    """Function that takes a file with
        morse code and creates another file
        with the english letters correspondents."""
    
    count = 1
    excp = True
    excp2 = True
    excp3 = True
    global tree
    global root
    
    # creating the binary tree with the letters and symbols from the MorseTable file
    # also, if the variable tree is false, it means that the user have not used the Morse2English function yet, so,
        ## we need to create the binary tree, otherwise, if it is true, the user have already created the tree,
        ## so it is not necessary to create it again
    # But, if the use changed the morse symbols, it is necessary to clean the tree and build it again
    if newM:
        Morse_Table = open('new_MorseTable.txt','r')
        root = Node(' ')
    else:
        if not tree:
            try:
                Morse_Table = open('MorseTable.txt','r')
            except:
                shell_connect.write('MorseTable.txt not found. Download it to continue.\n','COMMENT')
                excp3 = False
    if excp3:
        if not tree or newM:
                # for each line (which has a letter and a morse code), insert the letter into the binary tree using the morse code as a path
            for line in Morse_Table:
                root.insert(line[2:-1],line[0])
            Morse_Table.close()
            tree = True
        ## take the name of the file (with morse code) to translate the code into english letters
            #try until the user enter a file that exists
        while True:
            try:
                filename = input('Please, write the name of the file (with extension) which has the morse code: \n')
                hidden_morse_file = open(filename,'r')
                break
            except:
                shell_connect.write('File does not exist, try again.\n','COMMENT')
        # creates the file which is going to have the message in english letters
        unhide_letter_file = open(filename[:-4]+'_unhidden.txt','w')
        # for each line of the file, take each morse code "path", for each morse code "path", go to the binary tree and
            # find which letter that morse code path represents
        # Invariant: line is always less than or equal to the number of lines in hidden_morse_file
        for line in hidden_morse_file:
            while line[0] == ' ':
                unhide_letter_file.write(' ')
                line = line[1:]
            morse_letter = line.split(' ')
            morse_letter[-1] = morse_letter[-1][:-1]
            if morse_letter != ['']:
                # if the user made a mistake and chose a file which is already in english letters, an error message is shown
                if morse_letter[0][0] == var1 or morse_letter[0][0] == var2 or morse_letter[0][0] == '*':
                    # for each dot/dash in the file, go to the binary tree and find what the correspondent
                        # letter is and write it in the new file
                    # Invariant: hidden_letter_path is always less than or equal to the number of dashes and dots in morse_letter
                    for hidden_letter_path in morse_letter:
                        try:
                            if hidden_letter_path != '':
                                # if it has a '*' symbol in front, print the letter capitalized
                                if hidden_letter_path [0] != '*':
                                    unhide_letter_file.write(root.find_letter(hidden_letter_path))
                                else:
                                    new_letter = root.find_letter(hidden_letter_path[1:])
                                    unhide_letter_file.write(new_letter.upper())
                            else:
                                count += 1
                                if count%2 == 0:
                                    # that's the end of a word, print one space
                                    unhide_letter_file.write(' ')
                                else:
                                    pass
                        except:
                            # morse code not found
                            shell_connect.write('Morse code not found.\n','COMMENT')
                            excp2 = False
                            excpwhy = 'Something is wrong with the morse code.'
                    unhide_letter_file.write('\n')
                    excp = True
                else:
                    excp = False
                    shell_connect.write('\nThis is not a morse code file!\n','COMMENT')
                    excpwhy = 'The file is not a morse code file.'
                    break
            else:
                unhide_letter_file.write('\n')
        hidden_morse_file.close()
        unhide_letter_file.close()
        if excp:
            if excp2:
                shell_connect.write('\nMorse to English sucessful!','STRING')
            else:
                shell_connect.write('\nMorse to English partially sucessful, some morse codes not found were ignored.','KEYWORD')
            print('\nThe file {} was created.'.format(filename[:-4]+'_unhidden.txt'))
        else:
            shell_connect.write('\nMorse to English failed. {}\n'.format(excpwhy),'COMMENT')


## This function allows the user to change the symbols of the morse code

def newMorseTable():
    """Function that takes the morse code table and new morse code symbols
        and creates a new morse code table with the new symbols."""
    excp3 = True
    global var1
    global var2
    global newM
    try:
        Morse_Table = open('MorseTable.txt','r')
    except:
        shell_connect.write('MorseTable.txt not found. Download it to continue.\n','COMMENT')
        excp3 = False
    if excp3:
        var1 = '*'
        # The symbol cannot be '*' because that is the symbol that allow the computer recognizes capital letters
        # The symbol must be just one character
        while var1 == '*' or len(var1)>1:
            var1 = input("\nPlease enter the first symbol in the morse code: ")
            if var1[0] == '*':
                shell_connect.write("\nThe symbol must be different from '*'!\n",'COMMENT')
            elif len(var1)>1:
                shell_connect.write("\nThe symbol must be ONE character!\n",'COMMENT')
        var2 = var1
        ## The symbols must be different from each other
        while var2 == var1 or var2[0] == '*' or len(var2)>1:
            var2 = input("\nPlease enter the second symbol in the morse code: ")
            if var2 == var1:
                shell_connect.write('\nThe second symbol must be different from the first one!\n','COMMENT')
            elif var2 == '*':
                shell_connect.write("\nThe symbol must be different from '*'!\n",'COMMENT')
            elif len(var2)>1:
                shell_connect.write("\nThe symbol must be ONE character!\n",'COMMENT')
            else:
                pass
        # another Morse Table file is created using the new symbols
        new_Morse_Table = open('new_MorseTable.txt','w')
        # Invariant: line is always less than or equal to the number of lines in the Morse_Table file
        for line in Morse_Table:
            new_Morse_Table.write(line[:2])
            # Invariant: i is always a dash or a dot
            for i in line[2:-1]:
                if i == '.':
                    new_Morse_Table.write(var1)
                elif i == '-':
                    new_Morse_Table.write(var2)
                else:
                    pass
            new_Morse_Table.write('\n')
        Morse_Table.close()
        new_Morse_Table.close()
        # if the user changed the symbols, the variable newM is going to be True
        newM = True
        # you change the morse symbols, you have to go immediately to the E2M function
            # because the other morse code symbols wont work anymore
            # until you changed it to the same symbols like before
        print("\nEnglish to Morse function: \n")
        English2Morse()    


## this is the initial running function

if __name__ == "__main__":
    var1 = '.'
    var2 = '-'
    newM = False
    dictionary = False
    tree = False
    Morse_dict = {}
    root = Node(' ')
    print('\t-------------------------------------------------------------')
    print("\t    Hello, Welcome to the Morse Code Project")
    print('\t-------------------------------------------------------------')
    while True:
        choice = input("\nPlease select:\n\t'M2E' if you want to decode a morse code file into english;\n\t'E2M' if you want to encode a message into morse code;\n\t'change' if you want to chnage the morse code symbols;\n\t'e' to exit: \n") 
        if choice.lower() == 'm2e':
            Morse2English()
        elif choice.lower() == 'e2m':
            English2Morse()
        elif choice[0].lower() == 'e':
            print('\nThank you.\nGood Bye. \n')
            break
        elif choice[0].lower() == 'c':
            newMorseTable()
        else:
            shell_connect.write('\nError:Try again','COMMENT')
