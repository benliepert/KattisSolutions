#include <iostream>
#include <vector>

using namespace std;

int sum(vector<int> a)
{
    int sum = 0;
    for(int i = 0; i < 7; i++)
    {
        sum += a[i];
    }
    return sum;
}

int main()
{
    int input[9];
    vector<int> output; //some set of 7 indices
    for(int i = 0; i < 9; i++)
    {
        cin >> input[i];
    }

    // generate a, b = the integers of numbers we WON'T include in the calc
    for(int i = 0; i < 8; i++)
    {
            for(int j = i+1; j < 9; j++)
            {
                for (int k = 0; k < 9; k++) //build the output
                {
                    if (k != i && k != j)
                    {
                        output.push_back(input[k]);
                    }
                }

                if(sum(output) == 100)
                {
                    break;
                }

                output.clear();
            }
    }

    for (int i = 0; i < 7; i++)
    {
        cout << output[i] << endl;
    }

    return 0;
}
