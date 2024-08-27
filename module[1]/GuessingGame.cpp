#include <iostream>
#include <stdlib.h>
#include <time.h>
using namespace std;

int main()
{
	// Sets the random number generator seed
	srand((unsigned int)time(NULL));

	// Using updated variable initialization from C++11
	// Generates random number between 0-99
	int randomNumber{ rand() % 100 };

	// Initializes guess to -1 so that it is never equal to randomNumber
	int guess{ -1 };
	
	// Continues the guessing game until correct answer is given
	while (guess != randomNumber)
	{
		cout << "Enter your guess: ";
		cin >> guess;

		if (guess > randomNumber)
		{
			cout << "Your number is too big!\n";
		}
		else if (guess < randomNumber)
		{
			cout << "Your number is too small!\n";
		}
		else
		{
			cout << "You are correct!\n";
		}
	}
}