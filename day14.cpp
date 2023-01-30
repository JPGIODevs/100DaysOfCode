#include <iostream>
#include <vector>
#include <string>

using namespace std;

//diy tryout of a function
string saySomething(string intake)
{
    return intake + "hello im the frog";
}

//main function
int main()
{
    //running parameters
    int counter = 0;
    bool running = true;
    int array[5] = {10,20,30,40,50};

    //while loop... duh
    while(running)
    {

        counter++;
        cout << "Counter is at " << counter << "\n";



        //for loop... duh
        for(int i = 0; i < 5; i++){

        cout << i << " Is the current number" << "\n";



        //if loop meant to break sequence at 5th counter cycle
        if(counter >= 1)
        {
            cout << "While loop finished lol \n";
            running = false;
            break;
        }
        }
    }
    //calling string function
    string completeString = saySomething("goosey ");
    cout << completeString;
    
}
