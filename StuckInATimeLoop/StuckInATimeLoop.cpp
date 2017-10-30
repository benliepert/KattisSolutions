#include <iostream>
#include <sstream>
#include <fstream>

using namespace std;

int main(int argc, char *argv[])
{
    //ifstream infile;
    //infile.open(argv[1]);
    int times;
    //infile >> times;
    cin >> times;
    for (int i = 0; i < times; i++)
    {
        cout << i+1 << " Abracadabra\n";
    }

    return 0;
}
