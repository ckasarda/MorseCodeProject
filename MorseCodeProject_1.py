## Project 2: Morse Code

## This first part is just to allow to change the color of the output text

# You need to download the MorseTable.txt file on Wyocourses

import sys
try:
    shell_connect = sys.stdout.shell
except AttributeError:
    print("idlecolors highlighting only works with IDLE")
    exit()

## this is the tree class

class Node:
    def __init__(self,letter):
        self.left = None
        self.right = None
        self.letter = letter

    ## function to print the entire tree in preorder
    def PrintTree(self):
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
        # if it is a dot, go to the left
        if path[0] == '.':
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
        elif path[0] == '-':
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
                        print('error: ja existe letra')

    # given a morse code, find the correspondence letter which is inside the binary tree
    def find_letter(self,hidden_letter_path):
        if hidden_letter_path[0] == '.':
            if len(hidden_letter_path) > 1:
                hidden_letter_path = hidden_letter_path[1:]
                return self.left.find_letter(hidden_letter_path)
            else:
                return(self.left.letter)
        elif hidden_letter_path[0] == '-':
            if len(hidden_letter_path) > 1:
                hidden_letter_path = hidden_letter_path[1:]
                return self.right.find_letter(hidden_letter_path)
            else:
                return(self.right.letter)



## Function to translate a file from english letters to morse code
            
def English2Morse ():
    Morse_dict = {}
    morse_word = ''
    morse_list = []
    why = ''
    ## This part is building the Table, which is an dictionary,
        # that shows for each letter (the key), the equivalent dot-dash string (the value) 
    Morse_Table = open('MorseTable.txt','r')
    for line in Morse_Table:
        Morse_dict.update({line[0]:line[2:-1]})
    Morse_Table.close()
    ## take the name of the file (with letters) to translate the text into morse code
    while True:
        try:
            filename = input("Please, write the name of the file (with extension) which has letters: \n")
            E2M_file = open(filename,'r')
            break
        except:
            shell_connect.write('File does not exist, try again.\n','COMMENT')
    # creates the file which is going to have the message in morse code
    morse_hidden_file = open(filename[:-4]+'_hidden.txt','w')
    # for each letter in the file, print the correspondent morse code in the new file
        # if the user made a mistake and chose a file which is already in morse code, an error message is shown
    for line in E2M_file:
        words_list = line.split()
        if words_list != []:
            if words_list[0][0] == '.' or words_list[0][0] == '-':
                excp = False
                excpwhy = 'The file is not a letter file'
                shell_connect.write('\nThis is not a letter file!\n','COMMENT')
                break
            else:
                for word in words_list:
                    for letter in word:
                        try:
                            letter = letter.lower() 
                            #transform the letter into morse code
                            morse_word = morse_word + Morse_dict[letter] + ' '
                        except:
                            pass
                            #excp = False
                            ##letter not found
                            #why = letter + ', '
                            #excpwhy = 'warning: {} not found and not printed'.format(why)
                    morse_hidden_file.write(morse_word)
                    morse_word = ''
                    morse_hidden_file.write('  ')
                    excp = True
            morse_hidden_file.write('\n')
        else:
            morse_hidden_file.write('\n')
    E2M_file.close()
    morse_hidden_file.close()
    if excp:
        shell_connect.write('\nEnglish to Morse sucessful!','STRING')
        print('\nThe file {} was created.'.format(filename[:-4]+'_hidden.txt'))
    else:
        shell_connect.write('\nEnglish to Morse fail. '+excpwhy+'.\n','COMMENT')


# Function to translate a file from morse code to english letters

def Morse2English():
    Morse_Table = open('MorseTable.txt','r')
    root = Node(' ')
    count = 1
    # creating the binary tree with the letters and symbols from the MorseTable file
    for line in Morse_Table:
        root.insert(line[2:-1],line[0])
    Morse_Table.close()
    ## take the name of the file (with morse code) to translate the code into english letters
    while True:
        try:
            filename = input('Please, write the name of the file (with extension) which has the morse code: \n')
            hidden_morse_file = open(filename,'r')
            break
        except:
            shell_connect.write('File does not exist, try again.\n','COMMENT')
    # creates the file which is going to have the message in english letters
    unhide_letter_file = open(filename[:-4]+'_unhidden.txt','w')
     # for each dot/dash in the file, go to the binary tree and find what the correspondent letter is and write it in the new file
        # if the user made a mistake and chose a file which is already in english letters, an error message is shown
    for line in hidden_morse_file:
        morse_letter = line.split(' ')
        morse_letter[-1] = morse_letter[-1][:-1]
        if morse_letter != ['']:
            if morse_letter[0][0] == '.' or morse_letter[0][0] == '-':
                for hidden_letter_path in morse_letter:
                    if hidden_letter_path != '':
                        unhide_letter_file.write(root.find_letter(hidden_letter_path))
                    else:
                        count += 1
                        if count%2 == 0:
                            unhide_letter_file.write(' ')
                        else:
                            pass
                unhide_letter_file.write('\n')
                excp = True
            else:
                excp = False
                shell_connect.write('\nThis is not a morse code file!\n','COMMENT')
                break
        else:
            unhide_letter_file.write('\n')
    hidden_morse_file.close()
    unhide_letter_file.close()
    if excp:
        shell_connect.write('\nMorse to English sucess!','STRING')
        print('\nThe file {} was created.'.format(filename[:-4]+'_unhidden.txt'))
    else:
        shell_connect.write('\nMorse to English fail. The file is not a morse code file.\n','COMMENT')



## this is the initial running function
        
if __name__ == "__main__":
    print('\t-------------------------------------------------------------')
    print("\t    Hello, Welcome to the Morse Code Project")
    print('\t-------------------------------------------------------------')
    while True:
        choice = input("\nPlease select:\n\t'M2E' if you want to decode a morse code file into english;\n\t'E2M' if you want to encode a message into morse code;\n\t'e' to exit: \n") 
        if choice == 'M2E':
            Morse2English()
        elif choice == 'E2M':
            English2Morse()
        elif choice[0].lower() == 'e':
            print('\nThank you.\nGood Bye. \n')
            break
        else:
            shell_connect.write('\nError:Try again','COMMENT')
