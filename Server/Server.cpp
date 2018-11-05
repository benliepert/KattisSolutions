#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int numTasks, totalTime;
    cin >> numTasks >> totalTime;

    int sum = 0;
    int compareTime = 0;

    while (numTasks-- > 0)
    {
        int a;
        cin >> a;
        compareTime += a;
        if (compareTime <= totalTime)
        {
            sum++;
        }
        else
        {
            break;
        }
    }

    cout << sum;
    return 0;
}
