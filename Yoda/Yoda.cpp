#include <iostream>
#include <math.h>

using namespace std;

string reverse(string);

int main()
{
    string sNum1, sNum2;
    cin >> sNum1 >> sNum2;

    string sNum1Rev = reverse(sNum1);
    string sNum2Rev = reverse(sNum2);

    int iLen1 = sNum1.size();
    int iLen2 = sNum2.size();

    string sNewNum1 = "";
    string sNewNum2 = "";

    int iMinLen = iLen1 < iLen2 ? iLen1 : iLen2;
    for(int i = 0; i < iMinLen; i++)
    {
        char cLSD1 = sNum1Rev[i];
        char cLSD2 = sNum2Rev[i];

        if(cLSD1 > cLSD2)
        {
            sNewNum1 += cLSD1;
        }
        else if(cLSD2 > cLSD1)
        {
            sNewNum2 += cLSD2;
        }
        else
        {
            sNewNum1 += cLSD1;
            sNewNum2 += cLSD2;
        }
    }

    if(sNewNum1 != "" && stoi(sNewNum1) == 0)
    {
        sNewNum1 = "0";
    }
    if(sNewNum2 != "" && stoi(sNewNum2) == 0)
    {
        sNewNum2 = "0";
    }

    sNewNum1 = reverse(sNewNum1);
    sNewNum2 = reverse(sNewNum2);

    string sAppendMe = "";

    for(int i = 0; i < sNum1.size() - iMinLen; i++)
    {
        sAppendMe += sNum1[i];
    }
    sNewNum1 = sAppendMe + sNewNum1;

    sAppendMe = "";
    for(int i = 0; i < sNum2.size() - iMinLen; i++)
    {
        sAppendMe += sNum2[i];
    }
    sNewNum2 = sAppendMe + sNewNum2;


    if(sNewNum1 == "")
    {
        cout << "YODA" << endl << sNewNum2 << endl;
    }
    else if (sNewNum2 == "")
    {
        cout << sNewNum1 << endl << "YODA" << endl;
    }
    else
    {
        cout << sNewNum1 << endl << sNewNum2 << endl;
    }

    return 0;
}

string reverse(string s)
{
    string rev = "";
    for (int i = 0 ; i < s.size(); i++)
    {
        rev = s[i] + rev;
    }
    return rev;
}
