class Solution {
public:
    int appendCharacters(string s, string t) {
        int i=0;
        int j=0;
        while(i<s.length()){
            if(s[i]==t[j]){
                i++;
                j++;
            }else{
                i++;
            }
         }
         int start =j;
        while(j<t.length()){
            s.push_back(t[j]);
            j++;
        }
        return t.length() - start;
    }
};