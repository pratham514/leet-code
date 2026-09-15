class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int i=0;
        int j=nums.size();
        while (i<j){
            nums[i]=nums[i]*nums[i];
            i++;
            

        }
        sort(nums.begin(),nums.end());
        return nums;
    }
};