#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

int rest(int n, int k, string s)
{
    int res(0), dist(k); // we start in dist(k) to consider left border
    if (n <= k)          // special case
    {
        for (int i = 0; i < n; i++)
        {
            if (s[i] == '1')
                return 0;
        }
        return 1;
    }
    for (int i = 0; i < n; i++)
    {
        dist = (s[i] == '1') ? 0 : dist + 1;
        if (dist == k * 2 + 1)
        {
            res++;
            dist -= k + 1;
        }
    }
    res += (dist > k) ? 1 : 0;
    return res;
}

int main()
{
    int t;
    scanf("%i", &t);
    for (int i = 0; i < t; i++)
    {
        int n, k;
        string s;
        cin >> n >> k >> s;
        cout << rest(n, k, s) << endl;
    }
    return 0;
}