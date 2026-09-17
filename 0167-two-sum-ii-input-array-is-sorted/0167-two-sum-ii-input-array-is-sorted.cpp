class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int t=target;
        int n=numbers.size();
        int l=n-1;
        int s=0;
        while(s<l){
            int total=numbers[s]+numbers[l];
            if(total==t){
                return {s+1,l+1};
            }else if(total<t){
                s++;

            }else{
                l--;
            }
        }
        return {};
            
        
    }
};