class Solution {
public:
    string reverseWords(string s) {
        stringstream ss(s);

        vector<string> arr;
        string word;

        while(ss>>word){
            arr.push_back(word);
        }
        int i=0;
        int j=arr.size()-1;
        while(i<j){
            swap(arr[i],arr[j]);
            i++;
            j--;
        }
        string ans="";
        for (int k = 0; k < arr.size(); k++) {
            ans += arr[k];

            if (k != arr.size() - 1)
                ans += " ";
        }

        return ans;
    }
};