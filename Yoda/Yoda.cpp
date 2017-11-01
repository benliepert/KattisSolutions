#include <iostream>
#include <math.h>

using namespace std;

int max(int, int);


int main()
{
    int iNum1, iNum2;
    cin >> iNum1 >> iNum2;

    string sNumOne = to_string(iNumOne);
    string sNumTwo = to_string(iNumTwo);

    int iLen1 = sNumOne.size();
    int iLen2 = sNumTwo.size();

    int iMaxLen = max(iLen1, iLen2);
    

    return 0;
}

int main(int a, int b)
{
    return a > b ? a : b;
}
