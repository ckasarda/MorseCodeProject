//Project 2: Morse Code Binary Tree Example
//C++: Connor Kasarda
//Python: Tiago Araujo
//Coder Reviewer: Bailie Allemand 
//Coder Reviewer: Jeffrey Michaelis
//Coder Reviewer: Matt Sharp

#include "pch.h"
#include <iostream> //Allows for cin and cout
#include <string> //Allows increased functionality with strings
#include <fstream> //Allows for input and output with text files

using namespace std;

char lSymbol = '.';//Symbol of the morse code, representing the left branching in the decode tree
char rSymbol = '-';//Symbol of the morse code, representing the right branching in the decode tree

bool test_file(string file) {//Tests to see if the file can be opened, returning a boolean value based on result
	ifstream input(file);
	return input.good();
}

struct Node {//Creates the nodes that will build up the decode binary tree
	char letter = ' ';
	struct Node * leftNode = NULL;
	struct Node * rightNode = NULL;
};

void decodeTreeConstructor(string, Node *);//Constructs the decode information for morse code into a binary tree
void addLetter(char, string, Node *);//Used to add desired letter into the binary decode tree
void findLetter(string, Node *);//Finds the equivalent letter for the morse code string passed in
void E2M(string, string);//Converts an English word file into Morse code
void M2E(Node *, string);//Converts a Morse code file into English words

int main()
{

	//Root of decode tree with no value
	Node * DecodeTree = new Node;

	char langc = ' ';//stores choice of the user for Morse or English file to be opened
	char again = ' ';//stores the answer for whether the user wants to use the program again or not
	string mtxt = "";//stores the file name for the Morse code text file
	string etxt = "";//stores the file name for the English code text file

	//Constructs the morse code keys into the decode binary tree
	decodeTreeConstructor("MorseTable.txt", DecodeTree);

	//Ask the user if they want to open a Morse file or an English file, repeating as many times as the user wants to run the program
	do {

		//Asks the user whether they would like to open a Morse text file or an English text file
		cout << "\nWould you like to open a Morse code file or an English file? (m for Morse, e for English): ";
		cin >> langc;

		//Loops until user enters valid input
		while (langc != 'm' && langc != 'M' && langc != 'e' && langc != 'E') {

			cout << "\nInvalid Entry!" << endl;//Displays error message
			cout << "\nWould you like to open a Morse code file or an English file? (m for Morse, e for English): ";
			cin >> langc;

		}

		//Depending on user input, checks if text file is Morse or English
		if (langc == 'm' || langc == 'M') {
			cout << "\nType in the name of the Morse file (1. Make sure it is a Morse file! 2. Make sure it is in the same location as the program!)" << endl;
			cout << "Example: SecretMorse.txt" << endl;
			cout << "Enter file name here: ";
			cin >> mtxt;
			if (test_file(mtxt))//Tests if the file exists
				M2E(DecodeTree, mtxt);
			else {
				cout << "\nNot found! Try again!" << endl;
				while (!test_file(mtxt)) {
					cout << "\nType in the name of the Morse file (1. Make sure it is a Morse file! 2. Make sure it is in the same location as the program!)" << endl;
					cout << "Example: SecretMorse.txt" << endl;
					cout << "Enter file name here: ";
					cin >> mtxt;
				}
				M2E(DecodeTree, mtxt);
			}

		}
		else {
			cout << "\nType in the name of the English file (1. Make sure it is an English file! 2. Make sure it is in the same location as the program!):" << endl;
			cout << "Example: SecretEnglish.txt" << endl;
			cout << "Enter file name here: ";
			cin >> etxt;
			if (test_file(etxt))//Tests if the file exists
				E2M("MorseTable.txt", etxt);
			else {
				cout << "\nNot found! Try again!" << endl;
				while (!test_file(etxt)) {
					cout << "\nType in the name of the Morse file (1. Make sure it is a Morse file! 2. Make sure it is in the same location as the program!)" << endl;
					cout << "Example: SecretMorse.txt" << endl;
					cout << "Enter file name here: ";
					cin >> etxt;
				}
				E2M("MorseTable.txt", etxt);
			}
		}

		cout << "\n\nWould you like to run the program again? (Please enter a y or Y to run again, press anything else otherwise): ";
		cin >> again;

	} while (again == 'y' || again == 'Y');//Loop Invariant: langc is always going to be m, for Morse, or e, for English, and DecodeTree is always the same binary tree stored with Morse code translation information
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

		cout << "Commence Decode Binary Tree construction!\n" << endl;

		//Invariant: letter always has first letter of line, or letter to be represented, and morse has rest of same line from position 2, the morse string equivalent
		while (getline(morsedata, line)) {

			//Store letter to be inserted into decode binary tree
			letter = line.front();
			cout << "Added character: " << letter << endl;

			//Store morse code equivalent into string
			morse = line.substr(2);
			cout << "Equivalent morse: " << morse << endl;

			//Add letter into proper location of decode binary tree
			addLetter(letter, morse, Parent);

		}

		cout << "\nDecode Binary Tree construction complete!" << endl;

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
	else if (morse[0] == lSymbol) {//If a dot is encountered, 
							   //moves to the node's left child and
							   //calls the function recursively

		if (root->leftNode == NULL) {//Creates an empty left child node
									 //incase one does not already exist there

			root->leftNode = new Node;

		}

		addLetter(letter_c, morse.substr(1), root->leftNode);

	}
	else if (morse[0] == rSymbol) {//If a dash is encountered, 
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
		cout << letter_c;

	}
	else if (morse[0] == lSymbol) {//If a dot encountered, 
							   //call function recursivly on left child node

		if (root->leftNode == NULL) {//If node does not exist along path to value,
									 //the symbol does not exist so display a message
									 //saying it is not found

			cout << "(Error: Letter not found!)" << endl;

		}
		else {

			findLetter(morse_code.substr(1), root->leftNode);

		}

	}
	else if (morse[0] == rSymbol) {//If a dash encountered, 
							   //call function recursivly on right child node

		if (root->rightNode == NULL) {//If node does not exist along path to value,
									  //the symbol does not exist so display a message
									  //saying it is not found

			cout << "(Error: Letter not found!)" << endl;

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
	morse_table.read(table_buffer, table_length);

	//Prints english message as morse equivalent
	//Invariant: i is always less than character length of text in message file
	for (int i = 0; i < message_length; i++) {

		//Invariant: j is always less than character length of text in morse table file
		for (int j = 0; j < table_length; j++) {

			if (tolower(message_buffer[i]) == table_buffer[j]) {//Checks to see if same letter is found in morse table file

				//initializes variable z with 2, the starting point of the morse code equivalent of the letter in the morse table file
				int z = 2;

				//Invariant: morse_string is either part of or the entirety of the morse string equivalent of the letter so far
				while (table_buffer[j + z] == lSymbol || table_buffer[j + z] == rSymbol) {//Tanslates letter to morse equivalent

					//Adds dot or dash to morse string variable according to morse table file
					if (table_buffer[j + z] == lSymbol)
						morse_string += lSymbol;
					else if (table_buffer[j + z] == rSymbol)
						morse_string += rSymbol;

					//Increments variable z
					z++;

				}

				cout << morse_string << " ";
				morse_string = "";
				break;

			}
			else if (tolower(message_buffer[i]) == ' ') {//If there is a space, 3 spaces are printed

				cout << "   ";
				morse_string = "";
				break;

			}

			morse_string = "";//Resets the morse string variable

		}

	}

	//Closes morse message and table file
	morse_message.close();
	morse_table.close();

}

void M2E(Node * root, string engfile) {

	//Declares and initializes string variable to hold morse code
	string morse = "";

	//Opens file with English words
	ifstream eng_message;
	eng_message.open(engfile);

	//Finds length of morse message
	eng_message.seekg(0, eng_message.end);
	streamoff eng_length = eng_message.tellg();
	eng_message.seekg(0, eng_message.beg);

	//Creates a buffer for morse message text
	char * eng_buffer = new char[int(eng_length)];

	//Read morse message text as block
	eng_message.read(eng_buffer, eng_length);

	//Invariant: morse is always either part of or the entirety of the morse code string equivalent to be decoded to english
	for (int i = 0; i < eng_length; i++) {//Siphens through the entire buffer of the English word file

		if (eng_buffer[i] == lSymbol)//Adds a dot to the morse code string to be decoded to English
			morse += lSymbol;
		else if (eng_buffer[i] == rSymbol)//Adds a dash to the morse code string to be decoded to English
			morse += rSymbol;
		else if (eng_buffer[i] == ' ' && eng_buffer[i + 1] == ' ' && eng_buffer[i + 2] == ' ') {//If three spaces, indicates a space and beginning of new word.
																								//Finds the letter from morse code string then prints a space
																								//before reseting the morse code string

			findLetter(morse, root);
			cout << " ";
			morse = "";

		}
		else if (eng_buffer[i] == ' ') {//If just one space, find the letter from the morse code string then reset the morse string

			findLetter(morse, root);
			morse = "";

		}
	}

	findLetter(morse, root);
	morse = "";

	eng_message.close();

}
