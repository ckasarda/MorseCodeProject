The proposal is accessible.  MorseCodeProject_proposal, it is currently a .docx file when we have completed it we can export it as a .pdf for when we submit it. See you all on Tuesday at 8:30 am. :) 

Pseudo code is complete. Will leave it up for a few hours on here before I turn it it in case anyone would like to review or change it at all.
    
   Bailie: They look good to me, I am starting to work on the Design layout so I will post it on here for review asap. 

# MorseCodeProject

## **Meetings: **

*Time:* 9:00 AM at eng computer lab 4072

## **Preparation:**

*ADT* -> encodes and decodes English letters to and from string codes of two symbols, like "." and "-" from Morse code.

*Required Elements*  
-> data items  
                  -> operations

*Optional Elements*  
-> examples  
                  -> illustrations

*Intended Audience*  
-> client or in-house project director

## **Implementation:**

*Language* -> C++ and Python

*Objective* -> translate Morse to and from English letters

*Input* -> user-entered file name, asking for more file names until termination message sent by user

*Output* -> translated message appearing on fil with similar name

## **Decoding:**

*Decoding Mechanism*  
-> Binary Tree  
                   -> includes 26 letters, 9 digits, and 7 punctuation marks  
                   -> example: letter "v" translates to "...-", meaning left-left-left-right in binary tree
                   
## **Programming:**

*Full Code*  
-> MorseTable.txt  
          -> used by program to perform encode and decode of messages

*English2Morse*  
-> build code table: shows equivalent dot-dash string for each letter  
              -> encode English text file: letter "v" generates "...-"

*Morse2English*  
-> build decode tree: contains insert operations into binary tree

                     1. read in letter from code table  
                     2. read Morse code string  
                     3. start from root, following either left or right branch (depending on whether dot or dash) until end of Morse code string file  
                     4. Letter belongs at current node  
                     
   -> decode Morse code file: dot-dash string "...-" generates letter "v"
              
                     1. start at root of decode tree  
                     2. depending on input character, follow dot or dash branch  
                     3. end at space, indicating end of Morse code string for single letter  
                     4. English letter to be written is letter value at current node  

*Additional Characters*  
-> add six or seven new characters, symbols, foreign language characters, or emojis  
                      -> assign these to unused dot-dash Morse code strings  
                      -> incorporate into test files and run  
                      
## **Enhancement:**

*Enchancement*  
-> at least once enhancement to appendix to the ADT  
             -> provide description  
             -> no implementation required  
             -> suggestions on Project2Morse.pdf on WyoCourses  
             

## **Deliverables:**

1. ADT Document -> cover page (title, names, date, optional features: team name or logo, and others specified)

2. Source Code -> code from programming section including additional characters

3. IO Files -> input and outputfiles for test run revealing results for all program options
