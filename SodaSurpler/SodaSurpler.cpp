#include <iostream>

using namespace std;

int main()
{
    int a[3];

    for (int i = 0; i < 3; i++)
    {
        cin >> a[i];
    }

    int numEmptyStart = a[0];
    int numEmptyFound = a[1];
    int toBuy = a[2];

    int sodas = (numEmptyStart + numEmptyFound) / toBuy;

    int rem = (numEmptyStart + numEmptyFound) % toBuy;

    int emptys = sodas + rem ;

    while (emptys >= toBuy) //
    {
        int justDrank = emptys / toBuy;
        sodas += justDrank;
        emptys -= justDrank * toBuy;
        emptys += justDrank;
    }

    cout << sodas << endl;

    return 0;
}
