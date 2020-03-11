#include <iostream>
#include <vector>

using namespace std;


class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int head, tail, tmp, len;
        head = 0;
        tail = nums.size() - 1;
        len = 0;

        while (head <= tail){
            if (nums[head] != val){
                head ++;
                len ++;
            } else if (nums[tail] == val){
                tail --;
            } else{
                tmp = nums[head];
                nums[head] = nums[tail];
                nums[tail] = tmp;
                len ++;
                head ++;
                tail --;
            }

        }

        return len;
        
    }
};


int main()
{
    vector<int> nums = {3,2,2,3};
    int val = 3;
    Solution solu;
    cout << "Test!" << "\n";
    cout << solu.removeElement(nums, val) << "\n";
}