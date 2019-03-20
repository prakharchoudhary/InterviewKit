// Complete the findMergeNode function below.

/*
 * For your reference:
 *
 * SinglyLinkedListNode {
 *     int data;
 *     SinglyLinkedListNode* next;
 * };
 *
 */
int findMergeNode(SinglyLinkedListNode* head1, SinglyLinkedListNode* head2) {
    SinglyLinkedListNode* currentA = head1;
    SinglyLinkedListNode* currentB = head2;

    while(currentA != currentB){
        if(currentA->next == NULL){
            currentA = head2;
        }else{
            currentA = currentA->next;
        }
        //currentB
        if(currentB->next == NULL){
            currentB = head1;
        }else{
            currentB = currentB->next;
        }
    }
    return currentB->data;    
}