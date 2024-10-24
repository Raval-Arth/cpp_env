#include "bits/stdc++.h"

using namespace std;

int removeDuplicates(vector<int> &nums)
{
    vector<int>::iterator ip;
    ip = unique(nums.begin(), nums.end());
    return ip - nums.begin();
}

int main()
{
    vector<int> arr = {1, 2, 2, 3, 4, 4, 4, 5, 5};
    int n = removeDuplicates(arr);
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    return 0;
}
