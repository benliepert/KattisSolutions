#include <iostream>

using namespace std;

int main()
{
    int lastHours = 0;
    int totalHours = 0;
    int totalDistance = 0;
    int speed = 0;
    int currentHours = 0;

    int input;
    cin >> input;
    while(input != -1)
    {
        for(int i = 0; i < input; i++)
        {
            cin >> speed >> totalHours;

            currentHours = totalHours - lastHours;
            totalDistance += speed * currentHours;

            lastHours = totalHours;
        }
        cin >> input;
        cout << totalDistance << " miles\n";
        totalDistance = 0;
        lastHours = 0;
        speed = 0;
        currentHours = 0;
        totalHours = 0;
    }

    return 0;
}
