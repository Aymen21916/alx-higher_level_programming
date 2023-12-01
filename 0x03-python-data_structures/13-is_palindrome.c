#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 * Author - Tolulope Fakunle
 * Return: If the function fails - NULL.
 *         Otherwise - a pointer to the new node.
 */

int is_palindrome(listint_t **head) {
    listint_t *temp = *head;
    int length = 0;
    if(temp == NULL || temp->next == NULL){
        return 1;
    }
    while(temp != NULL){
        length++;
        temp = temp->next;
    }
    temp = *head;
    int list[length];
    for(int i = 0; i < length; i++){
        list[i] = temp->n;
        temp = temp->next;
    }
    int j = length - 1;
    temp = *head;
    while(temp != NULL){
        if(temp->n != list[j]){
            return 0;
        }
        temp = temp->next;
        j--;
    }
    return 1;
}
