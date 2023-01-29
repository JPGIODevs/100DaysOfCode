#include <iostream>
#include <vector>
#include <string>

using namespace std;

// function structure?
int main()
{
    //variable defined
    int number = 10;
    
    // comment syntax n below is print syntax
    cout << "Hello world, and the variable is " << number;

    // number variable changed after definition
    number = 10;
    // const makes immutable
    const int unchangableNumber = 20;
    cout << "enter a number to compare to 20: ";
    cin >> number;

    if(number < unchangableNumber){
        cout << unchangableNumber << " is the biggest number";
    } else{
        cout << number << " is the biggest number";
    }

    return 0;
}