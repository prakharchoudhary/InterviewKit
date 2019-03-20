// Complete the reverse function below.

/*
 * For your reference:
 *
 * DoublyLinkedListNode {
 *     int data;
 *     DoublyLinkedListNode* next;
 *     DoublyLinkedListNode* prev;
 * };
 *
 */
DoublyLinkedListNode* reverse(DoublyLinkedListNode* head) {
    DoublyLinkedListNode *h1, *h2, *h3;
    h1 = head;
    h2 = head;
    while (h1 != NULL) {
        h3 = h1->prev;
        h1->prev = h1->next;
        h1->next = h3;
        h2 = h1;
        h1 = h1->prev;
    }  
    return h2;
}