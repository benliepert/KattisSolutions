#include <iostream>

using namespace std;

int main()
{
    int input[9];
    int output[7]; //some set of 7 indices
    for(int i = 0; i < 9; i++)
    {
        cin >> input[i];
        if(i < 7)
        {
            output[i] = input[i];
        }
    }
    //=========================================
    // sum is of the first 7 things
    while(sum(ouptut) != 100)
    {
        // switch up output
        


    }
    //=========================================
    for (int i = 0; i < 7; i++)
    {
        cout << output[i] << endl;
    }

    return 0;
}

int sum(int a[7])
{
    int sum = 0;
    for(int i = 0; i < 7; i++)
    {
        sum += a[i];
    }
    return sum;
}
