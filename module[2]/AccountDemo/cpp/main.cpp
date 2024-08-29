#include <iostream>
#include <string>
#include "account.h"
using namespace std;

int main()
{
    Account testAccount{ "Test Name", "2314", 100.0f };

    testAccount.deposit("2314", 20.0f);
    cout << testAccount.checkBalance("2314") << endl;
    testAccount.withdraw("2314", -10.0f);
    cout << testAccount.checkBalance("2314") << endl;

    return 0;
}