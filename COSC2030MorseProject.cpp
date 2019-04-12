//Project 2: Morse Code Binary Tree Example
//Connor Kasarda

//The english to morse code works completely
//The morse to english is in the works

#include "pch.h"
#include <iostream>
#include <string>
#include <fstream>
#include <stddef.h>

using namespace std;

const string whitespace = "\t\f\v\n\r";

struct Node {
	char letter = ' ';
	struct Node * leftNode = NULL;
	struct Node * rightNode = NULL;
};

void decodeTreeConstructor(string, Node *);
void addLetter(char, string, Node *);
void findLetter(string, Node *);
void E2M(string, string);

int main()
{

	//Root of decode tree with no value
	Node * DecodeTree = new Node;

	//Constructs the morse code keys into the decode binary tree
	decodeTreeConstructor("MorseTable.txt", DecodeTree);

	//Attempts to find a letter from morse code string input and
	//displays correct letter
	string morseInput = " ";
	cout << "Type morse code equivalent of a letter: ";
	getline(cin, morseInput);

	findLetter(morseInput, DecodeTree);

	E2M("MorseTable.txt", "E2MTest1.txt");

}

void decodeTreeConstructor(string filename, Node * Parent) {

	//Create temporary variables
	string line = " ";
	string morse = " ";
	char letter = ' ';

	//Open file used for input
	ifstream morsedata;
	morsedata.open(filename);
	
	//Insert file data into decode tree
	if (morsedata.is_open()) {

		while (getline(morsedata, line)) {

			//Store letter to be inserted into decode binary tree
			letter = line.front();

			//Store morse code equivalent into string
			morse = line.substr(2);

			//Add letter into proper location of decode binary tree
			addLetter(letter, morse, Parent);

		}

	}

	//Closes input text file
	morsedata.close();

}

//Adds letter to the correct node in the decode tree
void addLetter(char letter_c, string morse, Node * root) {

		if (morse.size() == 0) {//End of the morse code string found,
								//place the letter value at current node

			root->letter = letter_c;

		}
		else if (morse[0] == '.') {//If a dot is encountered, 
								   //moves to the node's left child and
								   //calls the function recursively

			if (root->leftNode == NULL) {//Creates an empty left child node
										 //incase one does not already exist there

				root->leftNode = new Node;

			}

			addLetter(letter_c, morse.substr(1), root->leftNode);

		}
		else if (morse[0] == '-') {//If a dash is encountered, 
								   //moves to the node's right child and
								   //calls the function recursively

			if (root->rightNode == NULL) {//Creates an empty right child node
										  //incase one does not already exist there

				root->rightNode = new Node;

			}

			addLetter(letter_c, morse.substr(1), root->rightNode);

		}

}

//With morse code as input, outputs the letter represented by the morse code string
void findLetter(string morse, Node * root) {

	char letter_c;
	string morse_code = morse;
	
	if (morse.size() == 0) {//Found end of the morse code string,
							//displays letter found at current node
		letter_c = root->letter;
		cout << "The symbol represented is: " << letter_c << endl;

	}
	else if (morse[0] == '.') {//If a dot encountered, 
							   //call function recursivly on left child node

		if (root->leftNode == NULL) {//If node does not exist along path to value,
									 //the symbol does not exist so display a message
									 //saying it is not found

			cout << "Letter not found" << endl;

		}
		else {

			findLetter(morse_code.substr(1), root->leftNode);

		}

	}
	else if (morse[0] == '-') {//If a dash encountered, 
							   //call function recursivly on right child node

		if (root->rightNode == NULL) {//If node does not exist along path to value,
									  //the symbol does not exist so display a message
									  //saying it is not found

			cout << "Letter not found" << endl;

		}
		else {

			findLetter(morse_code.substr(1), root->rightNode);

		}

	}

}

void E2M(string morsetable, string morsefile) {

	string morse_string = "";

	ifstream morse_message;
	morse_message.open(morsefile);

	//Finds length of morse message
	morse_message.seekg(0, morse_message.end);
	streamoff message_length = morse_message.tellg();
	morse_message.seekg(0, morse_message.beg);

	//Creates a buffer for morse message text
	char * message_buffer = new char[int(message_length)];

	//Read morse message text as block
	morse_message.read(message_buffer, message_length);

	ifstream morse_table;
	morse_table.open(morsetable);
	
	//Finds length of morse table
	morse_table.seekg(0, morse_table.end);
	streamoff table_length = morse_table.tellg();
	morse_table.seekg(0, morse_table.beg);

	//Creates a buffer for morse table text
	char * table_buffer = new char[int(table_length)];

	//Read morse code table text as block
	morse_table.read(table_buffer,table_length);

	//Prints english message as morse equivalent
	for (int i = 0; i < message_length; i++) {

		for (int j = 0; j < table_length; j++) {

			if (tolower(message_buffer[i]) == table_buffer[j]) {

				int z = 2;

				while (table_buffer[j + z] == '.' || table_buffer[j + z] == '-') {

					if (table_buffer[j + z] == '.')
						morse_string += ".";
					else if (table_buffer[j + z] == '-')
						morse_string += "-";

					z++;

				}

				cout << morse_string << " ";
				morse_string = "";
				break;

			}
			else if (tolower(message_buffer[i]) == ' ') {

				cout << "   ";
				morse_string = "";
				break;

			}

			morse_string = "";

		}

	}

	//Closes morse message and table file
	morse_message.close();
	morse_table.close();

}
