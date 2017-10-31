#include <iostream>

using namespace std;

int main()
{
    int iNumLines;
    cin >> iNumLines;
    string line = "";
    string sNewString = "";
    string outputString = "";
    getline(cin, line);
    for(int i = 0; i < iNumLines; i++)
    {
        getline(cin, line);
        if (line.length() > 10)
        {
            for (int j = 0; j < 10; j++)
            {
                sNewString += line[j];
            }

            if (sNewString == "Simon says")
            {
                for(int k = 10; k < line.length(); k++)
                {
                    outputString += line[k];
                }
                cout << outputString << endl;
            }
            outputString = "";
            sNewString = "";
        }

    }

    return 0;
}
