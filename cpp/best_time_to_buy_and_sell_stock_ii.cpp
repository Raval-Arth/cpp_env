#include "bits/stdc++.h"

using namespace std;

long getMaximumProfit(vector<int> &prices)
{
    int profit = 0;

    for (int itr = 1; itr < prices.size(); itr++)
    {
        if (prices[itr] > prices[itr - 1])
        {
            profit += (prices[itr] - prices[itr - 1]);
        }
    }
    return profit;
}

int main()
{
    vector<int> Arr = {7, 1, 5, 3, 6, 4};

    // Call the getMaximumProfit function and print the result
    cout << "The maximum profit that can be generated is " << getMaximumProfit(Arr);

    return 0;
}
