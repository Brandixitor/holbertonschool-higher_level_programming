#include "lists.h"
#include <stdio.h>
#include <string.h>
/**
* check_cycle - checks if a singly linked list has a cycle in it or not.
* @list: Takes a listint_t as an argument.
* Return: either 0 or 1.
**/

int check_cycle(listint_t *list)
{
	int i = 0, checkn = 0, b = 0;
	listint_t *check = NULL, *tmp = NULL;

	if (list == NULL)
		return (0);
	check = list;
	tmp = list;
	while (check->next != NULL)
	{
		check = check->next;
		i++;
		if (i > 100)
			return (1);
	}
	checkn = check->n;
	i = 0;
	while (tmp)
	{
		if (checkn == tmp->n)
			b++;
		if (b == 2)
			return (1);
		if (i > 100)
			return (0);
		tmp = tmp->next;
		i++;
	}
	return (0);
}
