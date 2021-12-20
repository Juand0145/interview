#include "binary_trees.h"
/**
 * binary_tree_node - Function that creates a binary tree node
 * @parent: Pointer to the head node of the binary tree
 * @value: Value of the node
 * Return: Pointer to new node or NULL if fail
 */
binary_tree_t *binary_tree_node(binary_tree_t *parent, int value)
{
binary_tree_t *new;

new = malloc(sizeof(binary_tree_t));
if (new == NULL)
return (NULL);

new->n = value;
new->parent = parent;
new->left = NULL;
new->right = NULL;

return (new);
}
