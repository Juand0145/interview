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

/**
 * height_recursion - Function that calculates the height using recursion
 * @tree: node to find recursion
 * Return: the number of height nodes
 */
int height_recursion(const binary_tree_t *tree)
{
int left_count = 0, right_count = 0;

if (tree->left)
left_count = height_recursion(tree->left);
if (tree->right)
right_count = height_recursion(tree->right);
return ((left_count > right_count) ? left_count + 1 : right_count + 1);
}
