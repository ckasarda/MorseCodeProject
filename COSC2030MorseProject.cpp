//Project 2: Morse Code Binary Tree Example
//Connor Kasarda

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

int main()
{

	//Root of decode tree with no value
	Node * DecodeTree = new Node;

	//Constructs the decode binary tree
	decodeTreeConstructor("MorseTable.txt", DecodeTree);
	
	//Attempts to find the letter associated with "...-", which is the letter v, and returns the letter v
	findLetter("...-", DecodeTree);

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

}

//Adds letter to the correct node in the decode tree
void addLetter(char letter_c, string morse, Node * root) {

		if (morse.size() == 0) {//End of recursion, stores letter from node into variable that stores letter
			
			root->letter = letter_c;

		}
		else if (morse[0] == '.') {//When a dot, add a new left node if no existing node, then recursively call function until end of morse string found

			if (root->leftNode == NULL) {

				root->leftNode = new Node;

			}

			addLetter(letter_c, morse.substr(1), root->leftNode);

		}
		else if (morse[0] == '-') {//When a dash, add a new right node if no existing node, then recursively call function until end of morse string found

			if (root->rightNode == NULL) {

				root->rightNode = new Node;

			}

			addLetter(letter_c, morse.substr(1), root->rightNode);

		}

}

//With morse code as input, outputs the letter represented by the morse code string
void findLetter(string morse, Node * root) {

	char letter_c;
	string morse_code = morse;
	
	if (morse.size() == 0) {//Letter has been found, prints out statement with desired letter if working properly

		letter_c = root->letter;
		cout << "The letter represented is: " << letter_c << endl;

	}
	else if (morse[0] == '.') {//If a dot, recursively call function for node's left child until size of morse string equals 0

		findLetter(morse_code.substr(1), root->leftNode);

	}
	else if (morse[0] == '-') {//If a dot, recursively call function for node's right child until size of morse string equals 0

		findLetter(morse_code.substr(1), root->rightNode);

	}

}
