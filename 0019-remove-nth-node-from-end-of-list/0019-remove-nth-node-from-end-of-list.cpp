/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* dummy=new ListNode(0);
        dummy->next=head;
        int len=0;
        ListNode* l=head;

        while(l!=nullptr){
            len++;
            l=l->next;
        }
        int d=len-n+1;
        int j=d-1;
        ListNode* prev=dummy;
        ListNode* cur=head;
        int i=0;
        while(i<j){
            cur=cur->next;
            prev=prev->next;
            i++;
        }
        prev->next=cur->next;


        return dummy->next;
    }
};