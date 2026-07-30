class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
         if (k <= 1) return 0;                 
        long long prod = 1;
        int left = 0;
        int ans = 0;
        for (int right = 0; right < (int)nums.size(); ++right) {
            prod *= nums[right];
            while (prod >= k && left <= right) {
                prod /= nums[left++];
            }
            ans += right - left + 1;         
        }
        return ans;
    }
};
        
   